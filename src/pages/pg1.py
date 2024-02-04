import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import pandas as pd

dash.register_page(__name__,
                    path='/',  # '/' is home page and it represents the url
                    )
layout = html.Div(
    [
        html.Img(src='assets/logo1.png'),
        html.Div(id="mydrop",children=[]),
        dcc.Graph(id='myfig1'),

    ]
)

@callback(Output('mydrop','children'),
              Input('mydata_stored', 'data'))
def populatemydrop(dimydata):
    dfmydata = pd.DataFrame(dimydata)
    lcol = list(dfmydata.columns)
    loptionscol = [{'label': str(option), 'value': option} for option in lcol]
    return dcc.Dropdown(id='mydrop',
                        options=loptionscol,
                        value='cola',)

@callback(Output('myfig1', 'figure'),
            [Input('mydrop', 'value'),
            Input('mydata_stored', 'data')])
def update_figure(option,dimydata):
    dfmydata = pd.DataFrame(dimydata)
    fig1 = px.bar(dfmydata[option])
    return fig1




