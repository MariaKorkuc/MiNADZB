from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt

def print_statistics(states):

    client = MongoClient(
            "mongodb+srv://admin:Password123@covid.7imo3.mongodb.net/MINADZB?retryWrites=true&w=majority")
    db = client.get_default_database('MINADZB')
    records = db.covid
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


    #rysowanie plotow
    dfUS.set_index(['date']).drop(['deaths', 'confirmed_cases', 'confirmed_deaths'], axis=1).plot(figsize=(20,20), title='Total cases in US in millions')
    plt.show()


    newCases = []
    newCases.append(0)
    n = len(dfUS.index)-1
    for x in range(n):
        newCases.append(dfUS['cases'].loc[n] - dfUS['cases'].loc[n-1] )
        n = n - 1
    dfUS['newCases'] = newCases
    print('new cases in us today: ' + str(newCases[len(newCases)-1]))

    dfUS.set_index(['date'])['newCases'].plot(figsize=(20,20), title='Total new cases in US')
    plt.show()


    for x in range(len(states)):
        dfStates.loc[dfStates['state'] == states[x]].set_index(['date'])['cases'].plot(figsize=(20, 20), title='Total cases in '+states[x]+' in millions')
        plt.show()

