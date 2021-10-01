import pygame as pa
import pandas as pd
pd.set_option('max_rows',20)

def VCETHACK():
    return html.Div(children='12_ARSSITE PARTICIPANT AT VCET 2021 HACKATHON',
                                         style={
                                             'textAlign':'center',
                                             'color':colors['desc']
                                         })
activecases = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
activedata = pd.read_csv(activecases)
deadoccur = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
deaddata = pd.read_csv(deadoccur)
def casesdata(data,country='INDIA',window=3):
    actived = data
    actdesh = actived[actived['Country/Region']==country]
    apidata = actdesh.T[4:].sum(axis='columns').diff().rolling(window=window).mean()[40:]
    df = pd.DataFrame(apidata,columns=['Total'])
    return df
def overalldata(df):
    return df.iloc[:,-1].sum()

activetotal = overalldata(activedata)
diestotal = overalldata(deaddata)

print('TOTAL CASES:',activetotal)
print('TOTAL DIES:',diestotal)

pa.time.wait(6000)
