import random as arsapi
import pandas as pd
import webbrowser
pd.set_option('max_rows',20)
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "browser"
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
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
    fig = px.line(df, y='Total', x=df.index, title='Daily confirmed cases trend for {}'.format(country),height=600,color_discrete_sequence =['RED'])
    fig.update_layout(title_x=0.5,plot_bgcolor='WHITE',paper_bgcolor='#F2DFCE',xaxis_title="Date",yaxis_title=yaxis_title)
    return fig

external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = '12_ARSSITE'


colors = {
    'select':'WHITE',
    'background': '#FAA004',
    'bodyColor':'BLACK',
    'graphbody':'pink',
    'text': 'BLACK',
    'desc':'BLACK'
}

def titlebg():
    return {'backgroundColor': colors['background']}


def titlee():
    return html.H1(children='MY COVID-19 CARE CENTER DASHBOARD',
                                        style={
                                        'textAlign': 'center',
                                        'color': colors['text']
                                    })


def HEADING():
    main_header =  dbc.Row(
                            [
                                dbc.Col(titlee(),md=12)
                            ],
                            align="center",
                            style=titlebg()
                        )
    subtitle_header = dbc.Row(
                            [
                                dbc.Col(VCETHACK(),md=12)
                            ],
                            align="center",
                            style=titlebg()
                        )
    header = (main_header,subtitle_header)
    return header



def PLACE():
    return activedata['Country/Region'].unique()

def DROPDOWN(country_list):
    dropdown_list = []
    for country in sorted(country_list):
        tmp_dict = {'label':country,'value':country}
        dropdown_list.append(tmp_dict)
    return dropdown_list





def get_country_dropdown(id):
    return html.Div([
                        html.Label('Select Country',style={
                                          'color': colors['select']
                                    }),
                        dcc.Dropdown(id='my-id'+str(id),
                            options=DROPDOWN(PLACE()),
                            value='INDIA'
                        ),
                        html.Div(id='my-div'+str(id)),
                        html.Br(),
                        
                    ])




            

def graph1():
    return dcc.Graph(id='graph1',figure=EARTH('US'))

def CIRCLETXT(card_header,card_value,overall_value):
    card_head_style = {'textAlign':'center','fontSize':'150%','fontColor':'black'}
    card_body_style = {'textAlign':'center','fontSize':'150%','fontColor':'black'}
    card_header = dbc.CardHeader(card_header,style=card_head_style)
    card_body = dbc.CardBody(
        [
            html.H5(f"{int(card_value):,}", className="card-title",style=card_body_style),
            html.P(
                "Worldwide: {:,}".format(overall_value),
                className="card-text",style={'textAlign':'center'}
            ),
        ]
    )
    card = [card_header,card_body]
    return card

def gene():
    vall=print(arsapi.randrange(5,78))

apu=gene()

def gena():
    vall=print(arsapi.randint(5,8))

gpu=gena()

def geno():
    vall=print(arsapi.randint(10,64))

ppu=geno()

def CIRCLETXT2(card_header,card_value,apu):
    card_head_style = {'textAlign':'center','fontSize':'150%'}
    card_body_style = {'textAlign':'center','fontSize':'150%'}
    card_header = dbc.CardHeader(card_header,style=card_head_style)
    card_body = dbc.CardBody(
        [
            html.H5(apu, className="card-title",style=card_body_style),
           
        ]
    )
    card = [card_header,card_body]
    return card

def CIR(card_header,card_value,gpu):
    card_head_style = {'textAlign':'center','fontSize':'150%'}
    card_body_style = {'textAlign':'center','fontSize':'150%'}
    card_header = dbc.CardHeader(card_header,style=card_head_style)
    card_body = dbc.CardBody(
        [
            html.H5(gpu, className="card-title",style=card_body_style),
           
        ]
    )
    card = [card_header,card_body]
    return card


def buj(card_header,card_value,ppu):
    card_head_style = {'textAlign':'center','fontSize':'150%'}
    card_body_style = {'textAlign':'center','fontSize':'150%'}
    card_header = dbc.CardHeader(card_header,style=card_head_style)
    card_body = dbc.CardBody(
        [
            html.H5(ppu, className="card-title",style=card_body_style),
           
        ]
    )
    card = [card_header,card_body]
    return card


def CIRCLE(country='INDIA'):
    conf_country_total = arssite_INDIA(activedata,country)
    dead_country_total = arssite_INDIA(deaddata,country)
   
    cards = html.Div(
        [
            dbc.Row(
                [
                              dbc.Col(dbc.Card(CIRCLETXT("ACTIVE",conf_country_total,activetotal), color="RED", inverse=True),md=dict(size=2)),
                              
                                  dbc.Col(dbc.Card(CIRCLETXT("DEAD",dead_country_total,diestotal),color="GREEN ", inverse=True),md=dict(size=2)),
                              dbc.Col(dbc.Card(CIRCLETXT2("VACANT BEDS ",conf_country_total,activetotal), color="#e119f7 "),md=dict(size=2)),
                              html.Br(),
                                  dbc.Col(dbc.Card(CIRCLETXT("OXYGEN  (L)",dead_country_total,diestotal),color="#1972f7 ", inverse=False),md=dict(size=2)),
                                                          
                                 dbc.Col(dbc.Card(CIR("AMBULANCE AVAILABLE",conf_country_total,activetotal),color="#00edc6 ", inverse=True),md=dict(size=2)),
                              dbc.Col(dbc.Card(buj("STATUS 1:normal 4:alert",conf_country_total,activetotal),color=" #f76e19 ", inverse=True),md=dict(size=2)),
                ],
                className="mb-4",
            ),
        ],id='card1'
    )
    return cards


def TENSION():
    return html.Div([  
                        dcc.Slider(
                            id='my-slider',
                            min=1,
                            max=10,
                            step=None,
                            marks={
                                1: '1',
                                3: '3',
                                5: '5',
                                7: '7',
                                
                            },
                            value=3,
                        ),
                        html.Div([html.Label('Select Moving Average Window')],id='my-div'+str(id),style={'textAlign':'center'})
                    ])

def DESIGN():
    page_header = HEADING()
    layout = dbc.Container(
        [
            page_header[0],
            page_header[1],
            html.Hr(),
            CIRCLE(),
            html.Hr(),
            dbc.Row(
                [
                    dbc.Col(get_country_dropdown(id=1),md=dict(size=4,offset=4)),
                    
                ]
            
            ),
            
            dbc.Row(
                [                
                    
                    dbc.Col(graph1(),md=dict(size=6,offset=3))
        
                ],
                align="center",

            ),
            dbc.Row(
                [
                    dbc.Col(TENSION(),md=dict(size=4,offset=4))                    
                ]
            
            ),
        ],fluid=True,style={'backgroundColor': colors['bodyColor']}
    )
    return layout

    layout2 = dbc.Container(
        [
            page_header[2],
            page_header[3],
            html.Hr(),
            CIRCLE(),
            html.Hr(),
            dbc.Row(
                [
                    dbc.Col(get_country_dropdown2(id=2),md=dict(size=4,offset=4))                    
                ]
            
            ),
            
            dbc.Row(
                [                
                    
                    dbc.Col(graph1(),md=dict(size=6,offset=3))
        
                ],
                align="center",

            ),
            dbc.Row(
                [
                    dbc.Col(TENSION(),md=dict(size=4,offset=4))                    
                ]
            
            ),
        ],fluid=True,style={'backgroundColor': colors['bodyColor']}
    )
    return layout2


app.layout = DESIGN()

@app.callback(
    [Output(component_id='graph1',component_property='figure'),
    Output(component_id='card1',component_property='children')],
    [Input(component_id='my-id1',component_property='value'), 
     Input(component_id='my-slider',component_property='value')] 
)


def VCETOUTPUT(input_value1,input_value2):
    return EARTH(input_value1,input_value2),CIRCLE(input_value1)

app.run_server(host= '0.0.0.0',debug=False)







