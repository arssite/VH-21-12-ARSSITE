import pygame as pa
import pandas as pd
pd.set_option('max_rows',20)
import plotly.io as pio
pio.renderers.default = "browser"
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

def arssite_INDIA(df,country='INDIA'):
    return df[df['Country/Region']==country].iloc[:,-1].sum()
country = 'INDIA'
conf_country_total = arssite_INDIA(activedata,country)
dead_country_total = arssite_INDIA(deaddata,country)
print(f'{country} ACTIVE:',conf_country_total)
print(f'{country} DEAD:',dead_country_total)

def EARTH(country='INDIA',window=3):
    df = casesdata(data=activedata,country=country,window=window)
    df.head(10)
    if window==1:
        yaxis_title = ""
    else:
        yaxis_title = "Daily Cases ({}-day MA)".format(window)
    fig = px.line(df, y='Total', x=df.index, title='Daily confirmed cases trend for {}'.format(country),height=600,color_discrete_sequence =['maroon'])
    fig.update_layout(title_x=0.5,plot_bgcolor='black',paper_bgcolor='#F2DFCE',xaxis_title="Date",yaxis_title=yaxis_title)
    return fig


external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = '12_ARSSITE'


colors = {
    'select':'white',
    'background': '#FAA004',
    'bodyColor':'#000000',
    'text': 'BLACK',
    'desc':'red'
}

def titlebg():
    return {'backgroundColor': colors['background']}


def titlee():
    return html.H1(children='',
                                        style={
                                        'textAlign': 'center',
                                        'color': colors['text']
                                    })

def VCETOUTPUT(input_value1,input_value2):
    return EARTH(input_value1,input_value2),CIRCLE(input_value1)

app.run_server(host= '0.0.0.0',debug=False)

pa.time.wait(6000)
