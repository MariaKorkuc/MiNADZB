#import report as report
import requests as requests
from pymongo import MongoClient
import pandas as pd
import gapandas as gp
from gilfoyle import report
import numpy as np
import matplotlib.pyplot as plt

def print_statistics():
    client = MongoClient(
            "mongodb+srv://admin:Password123@covid.7imo3.mongodb.net/MINADZB_cloud?retryWrites=true&w=majority")
    db = client.get_default_database('MINADZB_cloud')
    records = db.covid_records
    myCursor = records.find({})
    df = pd.DataFrame(list(records.find({})))

    #porzadkowanie danych
    del df[df.columns[0]]

    df.fillna(0, inplace=True)
    df.cases = df.cases.astype('int64')
    df.deaths = df.deaths.astype('int64')
    df.confirmed_cases = df.confirmed_cases.astype('int64')
    df.confirmed_deaths = df.confirmed_deaths.astype('int64')

    dfStates = df.drop(['county'], axis=1).groupby(['date', 'state']).sum().reset_index()
    dfUS = dfStates.drop(['state'], axis=1).groupby(['date']).sum().reset_index()

# pdf = report.Report(output='example.pdf')
# payload = pdf.get_payload()
#
#
#
# payload = pdf.add_page(payload,
#                        page_type='chapter',
#                        page_title='Covid report US',
#                        page_subheading='November 2021')
#
# #Add metrics
# metrics = [
#     pdf.add_metric_tile(
#         metric_title='cases',
#         metric_value_now=df['cases'].loc[5000],
#         metric_value_before=df['cases'].loc[5012],
#         metric_name='year'
#     ),
# ]


    #rysowanie plotow
    dfUS.set_index(['date']).drop(['deaths', 'confirmed_cases', 'confirmed_deaths'], axis=1).plot(figsize=(20,20), title='Total cases in US in milions')
    plt.show()

    newCases = []
    newCases.append(0)
    n = len(dfUS.index)-1
    for x in range(n):
        newCases.append(dfUS['cases'].loc[n] - dfUS['cases'].loc[n-1] )
        n = n - 1
    dfUS['newCases'] = newCases


    dfUS.set_index(['date'])['newCases'].plot(figsize=(20,20), title='Total new cases in US')
    plt.show()


    dfStates.loc[dfStates['state'] == 'California'].set_index(['date'])['cases'].plot(figsize=(20,20), title='Total cases in California in milions')
    plt.show()

    dfStates.loc[dfStates['state'] == 'Texas'].set_index(['date'])['cases'].plot(figsize=(20,20), title='Total cases in Texas in milions')
    plt.show()

    dfStates.loc[dfStates['state'] == 'Florida'].set_index(['date'])['cases'].plot(figsize=(20,20), title='Total cases in Florida in milions')
    plt.show()


# payload = pdf.add_page(payload,
#                        page_type='report',
#                        page_layout='simple',
#                        page_title='All channels',
#                        page_dataframe=dfUS.set_index(['date']).drop(['deaths', 'confirmed_cases', 'confirmed_deaths'], axis=1).plot(),
#                        #page_dataframe=dfUS['cases'].plot(),
#                        page_metrics=metrics)
#
# pdf.create_report(payload, verbose=False, output='pdf')