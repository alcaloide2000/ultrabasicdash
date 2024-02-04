from dash import dcc, html, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash

dash.register_page(__name__,
                   path='/page2')

layout = html.Div(
    [
        html.Img(src='assets/logo2.png'),
        dcc.Graph(id='myfig3')
    ]
)

@callback(Output('myfig3', 'figure'),
              Input('mydata_stored', 'data'))
def mygraf1(dimydata):
    dfmydata = pd.DataFrame(dimydata)
    fig3 = px.line(dfmydata)
    return fig3



