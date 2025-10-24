import pandas as pd
import requests
import json

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
                "name": dict["name"],
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

def get_indicator_data(indicator_data):
    """
    Gets and cleans the indicator data into a dataframe indexed by country id.
    """
    indicator_series_list = []

    for indicator in indicator_data.keys():
        indicator_dict = {}
        for country in indicator_data[indicator][1]:
            indicator_dict[country['country']['id']] = country['value']
        indicator_series = pd.Series(indicator_dict)
        indicator_series.name = indicator
        indicator_series_list.append(indicator_series)
    output = pd.DataFrame(indicator_series_list).transpose()
    return output

if __name__ == "__main__":
    get_country_data()

