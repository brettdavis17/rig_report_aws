import json
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import dash_table
import pandas as pd
from urllib.request import urlopen
from dateutil.relativedelta import relativedelta
import apps.functions as functions
from application import app

# external_stylesheets = [
#     dbc.themes.CYBORG
# ]
#
# app = dash.Dash(
#     __name__,
#     # external_stylesheets=external_stylesheets
# )
# server = app.server
#
# app.config['suppress_callback_exceptions'] = True

# app.layout = \

layout = html.Div('International Page Coming Soon')