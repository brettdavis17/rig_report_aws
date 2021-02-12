import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

from application import server
from application import app
from apps import north_america, usa_land

# external_stylesheets = [
#     dbc.themes.COSMO
# ]

# app = dash.Dash(
#     __name__,
#     external_stylesheets=external_stylesheets
# )
# server = app.server
#
# app.config['suppress_callback_exceptions'] = True

navbar = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("North America", href="/north_america"),
                dbc.DropdownMenuItem("USA Land", href="/usa_land")
                # dbc.DropdownMenuItem("International", href="/international"),
            ],
            nav=True,
            in_navbar=True,
            label="Explore",
        ),
    ],
    brand="RigCountDashboard",
    brand_href="#",
    color="black",
    dark=True,
)


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/north_america':
        return north_america.layout
    else:
        return usa_land.layout


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)