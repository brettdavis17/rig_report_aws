import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

from application import server
from application import app
from apps import north_america, usa_land, international

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

location = dcc.Location(id='url', refresh=False)

navbar = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("North America", href="/north_america"),
                dbc.DropdownMenuItem("USA Land", href="/usa_land"),
                dbc.DropdownMenuItem("International", href="/international"),
            ],
            nav=True,
            in_navbar=True,
            label="Explore",
        ),
    ],
    brand="RigCountDashboard",
    brand_href="/",
    color="black",
    dark=True,
)

body = html.Div(id='page-content')

def serve_layout():
    return html.Div([
        location,
        navbar,
        body
    ])

app.layout = serve_layout

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/usa_land':
        return usa_land.page_layout
    elif pathname == '/international':
        return international.page_layout
    else:
        return north_america.page_layout


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)