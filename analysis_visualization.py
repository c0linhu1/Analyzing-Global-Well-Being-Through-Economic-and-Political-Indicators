# analysis_visualization.py

# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio

# Set Plotly to render charts in the browser
pio.renderers.default = "browser"

# Load the CSV file into a DataFrame
df = pd.read_csv('world_bank_data_2023.csv', index_col=0)


# Chart 1: Economic Prosperity vs Political Voice

# Clean the data for relevant columns
df_clean1 = df.dropna(subset=['NY.GNP.PCAP.CD', 'VA.EST', 'SP.POP.TOTL'])

# Create the scatter plot
fig1 = px.scatter(
    df_clean1,
    x='NY.GNP.PCAP.CD',
    y='VA.EST',
    size='SP.POP.TOTL',
    color='region',
    hover_name=df_clean1.index,
    hover_data={
        'NY.GNP.PCAP.CD': ':,.0f',
        'VA.EST': ':.3f',
        'SP.POP.TOTL': ':,.0f',
        'incomeLevel': True,
        'region': False
    },
    labels={
        'NY.GNP.PCAP.CD': 'GDP per Capita (USD)',
        'VA.EST': 'Voice and Accountability Score',
        'SP.POP.TOTL': 'Population',
        'region': 'Region',
        'incomeLevel': 'Income Level'
    },
    title='Economic Prosperity vs. Political Voice in 2023',
    size_max=60,
    opacity=0.7
)

# Format layout and log scale for GDP
fig1.update_layout(
    width=1200,
    height=700,
    font=dict(size=12),
    legend=dict(
        title=dict(text='Region', font=dict(size=14)),
        orientation='v',
        yanchor='top',
        y=1,
        xanchor='left',
        x=1.02
    ),
    hovermode='closest'
)
fig1.update_xaxes(type='log', title='GDP per Capita (USD, log scale)')

fig1.show()



# Chart 2: Voice & Accountability vs Military Spending

# Clean the data for relevant columns
df_clean2 = df.dropna(subset=['VA.EST', 'MS.MIL.XPND.GD.ZS', 'NY.GNP.PCAP.CD'])

# Create the scatter plot
fig2 = px.scatter(
    df_clean2,
    x='MS.MIL.XPND.GD.ZS',
    log_x=True,
    y='VA.EST',
    color='region',
    size='NY.GNP.PCAP.CD',
    hover_name=df_clean2.index,
    hover_data={
        'MS.MIL.XPND.GD.ZS': ':.2f',
        'VA.EST': ':.2f',
        'NY.GNP.PCAP.CD': ':,.0f',
        'incomeLevel': True,
        'region': False
    },
    labels={
        'MS.MIL.XPND.GD.ZS': 'Military Expenditure (% of GDP)',
        'VA.EST': 'Voice & Accountability Score',
        'NY.GNP.PCAP.CD': 'GDP per Capita'
    },
    title='Voice & Accountability vs Military Spending (sized by GDP per Capita)',
    color_discrete_sequence=px.colors.qualitative.Prism
)

fig2.update_layout(
    height=600,
    plot_bgcolor='white',
    xaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgray'),
    yaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgray')
)

fig2.show()

