import pandas as pd
import requests
import json



indicators = {
    'SP.POP.TOTL': 'Population, total',
    'NY.GNP.PCAP.CD': 'GDP Per Capita',
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


def get_country_data():
    """
    Gets country region and income level as a dataframe indexed by country id.

    Args: 
        None

    Returns:
        DataFrame with country id as index and region/incomeLevel as columns

    """
    response = requests.get("https://api.worldbank.org/v2/country?format=json&per_page=296")
    country_data = json.loads(response.text)[1]

    country_dct = {}

    for dict in country_data:
        if dict["region"]["value"] != "Aggregates":
            country_dct[dict["iso2Code"]] = {
                "region": dict["region"]["value"],
                "incomeLevel": dict["incomeLevel"]["value"],
            }
    df = pd.DataFrame.from_dict(country_dct, orient = "index")
                
    #print(df)

    return df

def get_indicator_data(indicators):
    """
    Gets and cleans the indicator data into a dataframe indexed by country id.

    Args:
        indicator: the indicator ID string

    Returns:
        Dataframe with country id as index and the indicators as columns

    """


    indicator_data = {}
    #Loop through each indicator and make an API call for each. Unfortunately, each API call can only return data for 1 indicator.
    for indicator in indicators.keys():
        indicator_data[indicator] = json.loads(requests.get(get_api_url(indicator, params)).text)

    indicator_series_list = []

    for indicator in indicator_data.keys():
        indicator_dict = {}
        for country in indicator_data[indicator][1]:
            country_id = country['country']['id']
            if len(country_id) == 2 and country_id.isalpha() and country_id.isupper():
                indicator_dict[country_id] = country['value']

        indicator_series = pd.Series(indicator_dict)
        indicator_series.name = indicator
        indicator_series_list.append(indicator_series)
    output = pd.DataFrame(indicator_series_list).transpose()
    #print(output)
    return output


def merge_data(country_df, indicator_df):
    """
    Merges country dataframe with indicator dataframe based on the country id index.
    
    Args:
        country_df: DataFrame with region/income data
        indicator_df: DataFrame with indicator data
        
    Returns:
        finalized merged dataframe containing country and indicator data
    """
    merge_df = pd.merge(indicator_df, country_df, left_index = True,
                         right_index = True, how = "right")
    return merge_df



if __name__ == "__main__":
    country_df = get_country_data()
    indicator_df = get_indicator_data(indicators)
    merged_data = merge_data(country_df, indicator_df)
    print(merged_data)

    merged_data.to_csv('world_bank_data_2023.csv')