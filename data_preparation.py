import pandas as pd
import requests
import json

indicators = {
    'SP.POP.TOTL': 'Population, total',
    'NY.GNP.PCAP.CD': 'GDP Per Captia',
    'SI.POV.DDAY': 'Poverty headcount ratio at $3.00 a day (2021 PPP)',
    'SI.POV.GINI': 'Gini index',
    'MS.MIL.XPND.GD.ZS': 'Military expenditure (% of GDP)',
    'VA.EST': 'Voice and Accountability: Estimate'
}

params = {
    'format': 'json',
    'per_page': '300', # This makes sure all countries are returned
    'date': '2023' #Query just one year
}


def get_api_url(indicator, params):
    """
    Constructs a URL for the API call, to query a given indicator and with a given set of parameters.

    Args:
        indicator: the indicator ID string
        params: a dictionary containing the API call parameters

    Returns:
        A URL to send an HTTP request to to get the API data
    """
    baseurl = 'https://api.worldbank.org/v2/country/all/indicator/'

    url = baseurl + indicator + '?'
    for param in params.keys():
        url = url + param + '=' + params[param] + '&'
    return url

"""
You said you want the region only - are you thinking that were gonna group the countries by region and 
use one of the indicators and then get like the mean of that indicator for each region and then do like a 
grouped bar plot
- if so then after we merge, ill groupby region 

"""
def get_country_data():
    """
    
    """
    response = requests.get("https://api.worldbank.org/v2/country?format=json&per_page=296")
    country_data = json.loads(response.text)[1]

    country_dct = []

    for dict in country_data:
        if dict["region"]["value"] != "Aggregates":
            country_dct.append({
                "name_id": dict["id"],
                "region": dict["region"]["value"],
                "region_id": dict["region"]["id"],
                "incomeLevel": dict["incomeLevel"]["value"],
                "incomeLevel_id": dict["incomeLevel"]["id"]
            })

    df = pd.DataFrame(country_dct)
    df.set_index("name_id")
    print(df)

    return df

def get_indicator_data(indicators):
    """
    Gets and cleans the indicator data into a dataframe indexed by country id.

    Args:
        indicator: the indicator ID string

    """


    indicator_data = {}
    #Loop through each indicator and make an API call for each. Unfortunately, each API call can only return data for 1 indicator.
    for indicator in indicators.keys():
        indicator_data[indicator] = json.loads(requests.get(get_api_url(indicator, params)).text)

    indicator_series_list = []

    for indicator in indicator_data.keys():
        indicator_dict = {}
        for country in indicator_data[indicator][1]:
            indicator_dict[country['country']['id']] = country['value']
        indicator_series = pd.Series(indicator_dict)
        indicator_series.name = indicator
        indicator_series_list.append(indicator_series)
    output = pd.DataFrame(indicator_series_list).transpose()
    print(output)
    return output


def merge_data(country_df, indicator_df):
    """
    """
    



if __name__ == "__main__":
    get_country_data()
    get_indicator_data(indicators)
