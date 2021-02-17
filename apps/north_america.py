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


layout = html.Div([
    #header
    html.Div([
        html.H2('NORTH AMERICA RIG DASHBOARD')
    ], className='header', style={'color': 'black'}
    ),
    #dropdowns
    html.Div([
        html.Div([
            dbc.Button(
                'SUBMIT',
                id='na-submit-button',
                style={
                    'backgroundColor': 'black',
                    'color': 'white'
                }
            ),
            dcc.Dropdown(
                id='na-date-dropdown',
                options=[{'label': x, 'value': x} for x in functions.get_date_list()],
                multi=False,
                value=functions.get_date_list()[0],
                placeholder='Select a date',
                persistence=True
            ),
            dcc.Dropdown(
                id='na-reference-dropdown',
                options=[
                    {'label': 'Rig Count View', 'value': 'rig_count_view'},
                    {'label': '1 Week +/- View', 'value': '1w'},
                    {'label': '1 Month +/- View', 'value': '1m'},
                    {'label': '3 Month +/- View', 'value': '3m'},
                    {'label': '6 Month +/- View', 'value': '6m'},
                    {'label': '1 Year +/- View', 'value': '1y'},
                    {'label': '3 Year +/- View', 'value': '3y'},
                    {'label': '5 Year +/- View', 'value': '5y'}
                ],
                value='rig_count_view',
                placeholder='Select view'
            ),
            html.Details([
                html.Summary('Country'),
                html.Div([
                    dbc.Button(
                        'SELECT ALL',
                        id='na-country-select-all',
                        size='sm',
                        style={
                            'backgroundColor': 'black',
                            'color': 'white'
                        }
                    ),
                    dbc.Button(
                        'CLEAR ALL',
                        id='na-country-clear-all',
                        size='sm',
                        style={
                            'backgroundColor': 'black',
                            'color': 'white'
                        }
                    ),
                    dcc.Checklist(
                        id='na-country-checklist',
                        options=[{'label': x, 'value': x} for x in functions.get_country_list()],
                        value=functions.get_country_list(),
                        persistence=True
                    )
                ])
            ]),
            html.Details([
                html.Summary('States'),
                html.Div([
                    dbc.Button(
                        'SELECT ALL',
                        id='na-state-select-all',
                        size='sm',
                        style={
                            'backgroundColor': 'black',
                            'color': 'white'
                        }
                    ),
                    dbc.Button(
                        'CLEAR ALL',
                        id='na-state-clear-all',
                        size='sm',
                        style={
                            'backgroundColor': 'black',
                            'color': 'white'
                        }
                    ),
                    dcc.Checklist(
                        id='na-state-checklist',
                        options=[{'label': x, 'value': x} for x in functions.get_state_list()],
                        value=functions.get_state_list(),
                        persistence=True
                    )
                ])
            ]),
            html.Details([
                html.Summary('Basins'),
                html.Div([
                    dbc.Button(
                        'SELECT ALL',
                        id='na-basin-select-all',
                        size='sm'
                    ),
                    dbc.Button(
                        'CLEAR ALL',
                        id='na-basin-clear-all',
                        size='sm'
                    ),
                    dcc.Checklist(
                        id='na-basin-checklist',
                        options=[{'label': x, 'value': x} for x in functions.get_basin_list()],
                        value=functions.get_basin_list(),
                        persistence=True
                    )
                ])
            ]),
            html.Details([
                html.Summary('Drill For'),
                html.Div([
                    dbc.Button(
                        'SELECT ALL',
                        id='na-drill-for-select-all',
                        size='sm'
                    ),
                    dbc.Button(
                        'CLEAR ALL',
                        id='na-drill-for-clear-all',
                        size='sm'
                    ),
                    dcc.Checklist(
                        id='na-drill-for-checklist',
                        options=[{'label': x, 'value': x} for x in functions.get_drill_for_list()],
                        value=functions.get_drill_for_list(),
                        persistence=True
                    )
                ])
            ]),
            html.Details([
                html.Summary('Location'),
                html.Div([
                    dbc.Button(
                        'SELECT ALL',
                        id='na-location-select-all',
                        size='sm'
                    ),
                    dbc.Button(
                        'CLEAR ALL',
                        id='na-location-clear-all',
                        size='sm'
                    ),
                    dcc.Checklist(
                        id='na-location-checklist',
                        options=[{'label': x, 'value': x} for x in functions.get_location_list()],
                        value=functions.get_location_list(),
                        persistence=True
                    )
                ])
            ]),
            html.Details([
                html.Summary('Trajectory'),
                html.Div([
                    dbc.Button(
                        'SELECT ALL',
                        id='na-trajectory-select-all',
                        size='sm'
                    ),
                    dbc.Button(
                        'CLEAR ALL',
                        id='na-trajectory-clear-all',
                        size='sm'
                    ),
                    dcc.Checklist(
                        id='na-trajectory-checklist',
                        options=[{'label': x, 'value': x} for x in functions.get_trajectory_list()],
                        value=functions.get_trajectory_list(),
                        persistence=True
                    )
                ])
            ]),
            html.Details([
                html.Summary('Well Depth'),
                html.Div([
                    dbc.Button(
                        'SELECT ALL',
                        id='na-well-depth-select-all',
                        size='sm'
                    ),
                    dbc.Button(
                        'CLEAR ALL',
                        id='na-well-depth-clear-all',
                        size='sm'
                    ),
                    dcc.Checklist(
                        id='na-well-depth-checklist',
                        options=[{'label': x, 'value': x} for x in functions.get_well_depth_list()],
                        value=functions.get_well_depth_list(),
                        persistence=True
                    )
                ])
            ])
        ], className='two columns'
        )
        ###,###
    ])
    ### get rid of this after test ###
])
### get rid of this after test ###
#         html.Div([
#             html.Div([
#                 html.Div([
#                     html.Div([
#                         dcc.Graph(
#                             id='na-indicator',
#                             config={
#                                 'displayModeBar': False
#                             }
#                         )
#                     ], className='graph_container'
#                     ),
#                     html.Div([
#                         dash_table.DataTable(
#                             id='na-country-table',
#                             style_data_conditional=[
#                                 {
#                                     'if': {'row_index': 'even'},
#                                     'textAlign': 'left',
#                                     'backgroundColor': '#686B6D',
#                                     'color': 'white'
#                                 },
#                                 {
#                                     'if': {'row_index': 'odd'},
#                                     'textAlign': 'left',
#                                     'backgroundColor': '#2C2D2E',
#                                     'color': 'white'
#                                 },
#                                 {
#                                     'if': {
#                                         'filter_query': '{+/-} > 0',
#                                         'column_id': '+/-'
#                                     },
#                                     'backgroundColor': 'green',
#                                     'color': 'white'
#                                 },
#                                 {
#                                     'if': {
#                                         'filter_query': '{+/-} < 0',
#                                         'column_id': '+/-'
#                                     },
#                                     'backgroundColor': 'red',
#                                     'color': 'white'
#                                 }
#                             ],
#                             style_header={
#                                 'backgroundColor': 'black',
#                                 'color': 'white',
#                                 'textAlign': 'left'
#                             }
#                         )
#                     ], style={'maxHeight': '120px', 'overflow': 'scroll'}
#                     ),
#                     html.Div([
#                         dash_table.DataTable(
#                             id='na-state-table',
#                             style_data_conditional=[
#                                 {
#                                     'if': {'row_index': 'even'},
#                                     'textAlign': 'left',
#                                     'backgroundColor': '#686B6D',
#                                     'color': 'white'
#                                 },
#                                 {
#                                     'if': {'row_index': 'odd'},
#                                     'textAlign': 'left',
#                                     'backgroundColor': '#2C2D2E',
#                                     'color': 'white'
#                                 },
#                                 {
#                                     'if': {
#                                         'filter_query': '{+/-} > 0',
#                                         'column_id': '+/-'
#                                     },
#                                     'backgroundColor': 'green',
#                                     'color': 'white'
#                                 },
#                                 {
#                                     'if': {
#                                         'filter_query': '{+/-} < 0',
#                                         'column_id': '+/-'
#                                     },
#                                     'backgroundColor': 'red',
#                                     'color': 'white'
#                                 }
#                             ],
#                             style_header={
#                                 'backgroundColor': 'black',
#                                 'color': 'white',
#                                 'textAlign': 'left'
#                             },
#                             style_cell={
#                                 'whiteSpace': 'normal',
#                                 'height': 'auto'
#                             }
#                         )
#                     ], style={'maxHeight': '230px', 'overflow': 'scroll'}
#                     )
#                 ], className='three columns'
#                 ),
#                 html.Div([
#                     html.Div([
#                         html.Div([
#                         ], className='nine columns'
#                         )
#                     ]),
#                     html.Div([
#                         dcc.Graph(
#                             id='na-rig-map'
#                         )
#                     ], className='graph_container'
#                     )
#                 ], className='seven columns'
#                 ),
#                 html.Div([
#                     html.Div([
#                         dcc.Graph(
#                             id='na-drill-for',
#                             config={
#                                 'displayModeBar': False
#                             }
#                         )
#                     ], className='graph_container'
#                     ),
#                     html.Div([
#                         dcc.Graph(
#                             id='na-depth',
#                             config={
#                                 'displayModeBar': False
#                             }
#                         )
#                     ], className='graph_container'
#                     ),
#                     html.Div([
#                         dcc.Graph(
#                             id='na-trajectory',
#                             config={
#                                 'displayModeBar': False
#                             }
#                         )
#                     ], className='graph_container'
#                     ),
#                     html.Div([
#                         dcc.Graph(
#                             id='na-location',
#                             config={
#                                 'displayModeBar': False
#                             }
#                         )
#                     ], className='graph_container'
#                     ),
#                 ], className='two columns'
#                 ),
#             ], className='twelve columns'
#             ),
#
#         ], className='ten columns'
#         )
#     ], className='twelve columns'
#     )
# ]
# )
#
#     # convert_dict = {'date': str}
#     # master_df = functions.get_overall_master_df().astype(convert_dict)
#
# # layout = serve_layout
#
# @app.callback(
#     Output(
#         'na-country-checklist',
#         'value'
#     ),
#     [
#         Input(
#             'na-country-select-all',
#             'n_clicks'
#         ),
#         Input(
#             'na-country-clear-all',
#             'n_clicks'
#         )
#     ],
# )
# def return_country_checklist(select_all, clear_all):
#     changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
#     if 'country-select-all' in changed_id:
#         return functions.get_state_list()
#     elif 'country-clear-all' in changed_id:
#         return []
#     else:
#         return functions.get_country_list()
#
# @app.callback(
#     Output(
#         'na-state-checklist',
#         'value'
#     ),
#     [
#         Input(
#             'na-state-select-all',
#             'n_clicks'
#         ),
#         Input(
#             'na-state-clear-all',
#             'n_clicks'
#         )
#     ],
# )
# def return_states_checklist(select_all, clear_all):
#     changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
#     if 'state-select-all' in changed_id:
#         return functions.get_state_list()
#     elif 'state-clear-all' in changed_id:
#         return []
#     else:
#         return functions.get_state_list()
#
# @app.callback(
#     Output(
#         'na-basin-checklist',
#         'value'
#     ),
#     [
#         Input(
#             'na-basin-select-all',
#             'n_clicks'
#         ),
#         Input(
#             'na-basin-clear-all',
#             'n_clicks'
#         )
#     ],
# )
# def return_basins_checklist(select_all, clear_all):
#     changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
#     if 'basin-select-all' in changed_id:
#         return functions.get_basin_list()
#     elif 'basin-clear-all' in changed_id:
#         return []
#     else:
#         return functions.get_basin_list()
#
# @app.callback(
#     Output(
#         'na-drill-for-checklist',
#         'value'
#     ),
#     [
#         Input(
#             'na-drill-for-select-all',
#             'n_clicks'
#         ),
#         Input(
#             'na-drill-for-clear-all',
#             'n_clicks'
#         )
#     ],
# )
# def return_drill_for_checklist(select_all, clear_all):
#     changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
#     if 'drill-for-select-all' in changed_id:
#         return functions.get_drill_for_list()
#     elif 'drill-for-clear-all' in changed_id:
#         return []
#     else:
#         return functions.get_drill_for_list()
#
# @app.callback(
#     Output(
#         'na-location-checklist',
#         'value'
#     ),
#     [
#         Input(
#             'na-location-select-all',
#             'n_clicks'
#         ),
#         Input(
#             'na-location-clear-all',
#             'n_clicks'
#         )
#     ],
# )
# def return_locations_checklist(select_all, clear_all):
#     changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
#     if 'location-select-all' in changed_id:
#         return functions.get_location_list()
#     elif 'location-clear-all' in changed_id:
#         return []
#     else:
#         return functions.get_location_list()
#
# @app.callback(
#     Output(
#         'na-trajectory-checklist',
#         'value'
#     ),
#     [
#         Input(
#             'na-trajectory-select-all',
#             'n_clicks'
#         ),
#         Input(
#             'na-trajectory-clear-all',
#             'n_clicks'
#         )
#     ],
# )
# def return_trajectory_checklist(select_all, clear_all):
#     changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
#     if 'trajectory-select-all' in changed_id:
#         return functions.get_trajectory_list()
#     elif 'trajectory-clear-all' in changed_id:
#         return []
#     else:
#         return functions.get_trajectory_list()
#
# @app.callback(
#     Output(
#         'na-well-depth-checklist',
#         'value'
#     ),
#     [
#         Input(
#             'na-well-depth-select-all',
#             'n_clicks'
#         ),
#         Input(
#             'na-well-depth-clear-all',
#             'n_clicks'
#         )
#     ],
# )
# def return_well_depth_checklist(select_all, clear_all):
#     changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
#     if 'well-depth-select-all' in changed_id:
#         return functions.get_well_depth_list()
#     elif 'well-depth-clear-all' in changed_id:
#         return []
#     else:
#         return functions.get_well_depth_list()
#
#
# @app.callback(
#     [
#         Output(
#             'na-indicator',
#             'figure'
#         ),
#         Output(
#             'na-rig-map',
#             'figure'
#         ),
#         Output(
#             'na-drill-for',
#             'figure'
#         ),
#         Output(
#             'na-depth',
#             'figure'
#         ),
#         Output(
#             'na-trajectory',
#             'figure'
#         ),
#         Output(
#             'na-location',
#             'figure'
#         ),
#         Output(
#             'na-state-table',
#             'columns'
#         ),
#         Output(
#             'na-state-table',
#             'data'
#         ),
#         Output(
#             'na-country-table',
#             'columns'
#         ),
#         Output(
#             'na-country-table',
#             'data'
#         )
#     ],
#     [
#         Input(
#             'na-submit-button',
#             'n_clicks'
#         )
#     ],
#     [
#         State(
#             'na-date-dropdown',
#             'value'
#         ),
#         State(
#             'na-reference-dropdown',
#             'value'
#         ),
#         State(
#             'na-country-checklist',
#             'value'
#         ),
#         State(
#             'na-state-checklist',
#             'value'
#         ),
#         State(
#             'na-basin-checklist',
#             'value'
#         ),
#         State(
#             'na-drill-for-checklist',
#             'value'
#         ),
#         State(
#             'na-location-checklist',
#             'value'
#         ),
#         State(
#             'na-trajectory-checklist',
#             'value'
#         ),
#         State(
#             'na-well-depth-checklist',
#             'value'
#         )
#     ]
# )
# def return_references(
#         click, date, dropdown_value, countries, states, basins, drill_for, locations, trajectories, well_depths
# ):
#     date_list = functions.get_date_list_asc()  # list of all unique dates
#
#     one_week_date = date_list[date_list.index(date) - 1]  # date 1 week before selected date
#     one_month_date = date_list[date_list.index(date) - 4]
#     three_month_date = date_list[date_list.index(date) - 13]
#     six_month_date = date_list[date_list.index(date) - 26]
#     one_year_date = date_list[date_list.index(date) - 52]
#     three_year_date = date_list[date_list.index(date) - 156]
#     five_year_date = date_list[date_list.index(date) - 260]
#
#     plus_minus_colorscale = [
#         '#660000', '#800000', '#990000', '#b30000', '#cc0000', '#e60000',
#         '#ff0000', '#ff1a1a', '#ff3333', '#ff4d4d', '#ff6666', '#ff8080',
#         '#ff9999', '#ffffff', '#99ffbb', '#80ffaa', '#66ff99', '#4dff88',
#         '#33ff77', '#1aff66', '#00ff55', '#00e64d', '#00cc44', '#00b33c',
#         '#009933', '#00802b', '#006622'
#     ]
#
#     if dropdown_value == 'rig_count_view':
#         reference_date = one_week_date
#         scatter_reference_date = one_year_date
#
#         df = functions.get_north_america_df(scatter_reference_date, date)
#
#         filtered_df = df[
#             df['country'].isin(countries) &
#             df['state'].isin(states) &
#             df['basin'].isin(basins) &
#             df['drill_for'].isin(drill_for) &
#             df['location'].isin(locations) &
#             df['trajectory'].isin(trajectories) &
#             df['well_depth'].isin(well_depths)
#         ]
#
#         current_df = filtered_df[filtered_df['date'] == date]
#         reference_df = filtered_df[filtered_df['date'] == reference_date]
#
#         scatter_df = filtered_df[['date', 'rig_count']].groupby('date').sum().reset_index()
#
#         # county_scatter_df = filtered_df[['date', 'county']].groupby(['date'])['county'].nunique().reset_index()
#
#
#         indicator_data = [
#             go.Indicator(
#                 mode='number+delta',
#                 value=current_df['rig_count'].sum(),
#                 delta={'reference': reference_df['rig_count'].sum()},
#             ),
#             go.Scatter(
#                 name='1-YEAR TREND',
#                 x=scatter_df['date'].tolist(),
#                 y=scatter_df['rig_count'].tolist()
#             )
#         ]
#
#         indicator_layout = go.Layout(
#             # title='COGS',
#             # height=100,
#             title_text='RIG COUNT AND TRENDS FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             height=177
#         )
#
#         indicator_fig = go.Figure(data=indicator_data, layout=indicator_layout)
#
#
#         s = open('/Users/brettdavis/Downloads/us_states.json')
#         p = open('/Users/brettdavis/Downloads/canada_provinces.json')
#
#         states = json.load(s)
#         provinces = json.load(p)
#
#         states_and_provinces = {"type": "FeatureCollection", "features": states['features'] + provinces['features']}
#
#         for feature in states_and_provinces['features']:
#             feature['id'] = feature['properties']['name'].upper()
#
#         map_df = current_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index()
#
#         map_data = go.Choropleth(
#             name='States & Provinces',
#             geojson=states_and_provinces,
#             locations=map_df['state'],
#             z=map_df['rig_count'],
#             colorscale='Oranges',
#             hovertemplate=map_df['state'] + '<br>Rigs: %{z}'
#         )
#
#         map_layout = go.Layout(
#             geo={
#                 'scope': 'north america',
#                 'showlakes': True,
#                 'fitbounds': 'locations'
#             },
#             title_text='STATE/PROVINCE-LEVEL HEAT MAP FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
#             titlefont={
#                 'size': 8
#             },
#             margin={
#                 'r': 0,
#                 't': 20,
#                 'l': 0,
#                 'b': 0
#             },
#             template="plotly_dark",
#             height=500
#         )
#
#         map_fig = go.Figure(data=map_data, layout=map_layout)
#
#         drill_for_df = current_df[[
#             'drill_for',
#             'rig_count'
#         ]].groupby('drill_for').sum().reset_index()
#
#         drill_for_pie_data = [
#             go.Pie(
#                 labels=drill_for_df['drill_for'].tolist(),
#                 values=drill_for_df['rig_count'].tolist(),
#                 textposition='inside',
#                 textinfo='label+percent',
#                 textfont={
#                     'size': 8
#                 }
#             )
#         ]
#
#         drill_for_pie_layout = go.Layout(
#                 title_text='DRILL-FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
#                 titlefont={
#                     'size': 8
#                 },
#                 template="plotly_dark",
#                 showlegend=False,
#                 height=118,
#                 margin={
#                     'r': 0,
#                     't': 20,
#                     'l': 0,
#                     'b': 0
#                 },
#             )
#
#         drill_for_fig = go.Figure(data=drill_for_pie_data, layout = drill_for_pie_layout)
#
#         well_depth_df = current_df[[
#             'well_depth', 'rig_count'
#         ]].groupby('well_depth').sum().reset_index()
#
#         well_depth_data = [
#             go.Pie(
#                 labels=well_depth_df['well_depth'].tolist(),
#                 values=well_depth_df['rig_count'].tolist(),
#                 textposition='inside',
#                 textinfo='label+percent',
#                 textfont={
#                     'size': 8
#                 }
#             )
#         ]
#
#         well_depth_layout = go.Layout(
#             title_text='WELL-DEPTH ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             showlegend=False,
#             height=118,
#             margin={
#                 'r': 0,
#                 't': 20,
#                 'l': 0,
#                 'b': 0
#             },
#         )
#
#         well_depth_fig = go.Figure(data=well_depth_data, layout=well_depth_layout)
#
#         trajectory_df = current_df[[
#             'trajectory', 'rig_count'
#         ]].groupby('trajectory').sum().reset_index()
#
#         trajectory_data = [
#             go.Pie(
#                 labels=trajectory_df['trajectory'].tolist(),
#                 values=trajectory_df['rig_count'].tolist(),
#                 textposition='inside',
#                 textinfo='label+percent',
#                 textfont={
#                     'size': 8
#                 }
#             )
#         ]
#
#         trajectory_layout = go.Layout(
#             title_text='TRAJECTORY ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             showlegend=False,
#             height=118,
#             margin={
#                 'r': 0,
#                 't': 20,
#                 'l': 0,
#                 'b': 0
#             },
#         )
#
#         trajectory_fig = go.Figure(data=trajectory_data, layout=trajectory_layout)
#
#         location_df = current_df[[
#             'location', 'rig_count'
#         ]].groupby('location').sum().reset_index()
#
#         location_data = [
#             go.Pie(
#                 labels=location_df['location'].tolist(),
#                 values=location_df['rig_count'].tolist(),
#                 textposition='inside',
#                 textinfo='label+percent',
#                 textfont={
#                     'size': 8
#                 }
#             )
#         ]
#
#         location_layout = go.Layout(
#             title_text='LOCATION ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             showlegend=False,
#             height=118,
#             margin={
#                 'r': 0,
#                 't': 20,
#                 'l': 0,
#                 'b': 0
#             },
#         )
#
#         location_fig = go.Figure(data=location_data, layout=location_layout)
#
#         state_table_df_raw = current_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})
#
#         state_table_df_ref_raw = reference_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})
#
#         state_table_df = state_table_df_raw.merge(
#             state_table_df_ref_raw,
#             'outer',
#             ['state']
#         )
#
#         state_table_df['rig_count_after'] = state_table_df['rig_count_after'].fillna(0)
#         state_table_df['rig_count_before'] = state_table_df['rig_count_before'].fillna(0)
#
#         state_table_df['rig_count_after'] = state_table_df['rig_count_after'].astype(int)
#         state_table_df['rig_count_before'] = state_table_df['rig_count_before'].astype(int)
#
#         state_table_df['difference'] = state_table_df['rig_count_after'] - state_table_df['rig_count_before']
#
#         state_table_df['rank'] = state_table_df['rig_count_after'].rank(method='min', ascending=False)
#
#         state_table_df_sort = state_table_df.sort_values(
#             by=['rig_count_after', 'difference'],
#             ascending=[False, False]
#         )
#
#         state_final_table_df = pd.DataFrame({
#             'RANK': [int(x) for x in state_table_df_sort['rank'].tolist()],
#             'STATE/PROVINCE': state_table_df_sort['state'].tolist(),
#             'RIGS': state_table_df_sort['rig_count_after'].tolist(),
#             '+/-': state_table_df_sort['difference'].tolist()
#         })
#
#         state_table_columns = [{
#             'name': i, 'id': i
#         } for i in state_final_table_df.columns]
#
#         state_table_data = state_final_table_df.to_dict('records')
#
#         country_table_df_raw = current_df[[
#             'country', 'rig_count'
#         ]].groupby(['country']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})
#
#         country_table_df_ref_raw = reference_df[[
#             'country', 'rig_count'
#         ]].groupby(['country']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})
#
#         country_table_df = country_table_df_raw.merge(
#             country_table_df_ref_raw,
#             'outer',
#             ['country']
#         )
#
#         country_table_df['rig_count_after'] = country_table_df['rig_count_after'].fillna(0)
#         country_table_df['rig_count_before'] = country_table_df['rig_count_before'].fillna(0)
#
#         country_table_df['rig_count_after'] = country_table_df['rig_count_after'].astype(int)
#         country_table_df['rig_count_before'] = country_table_df['rig_count_before'].astype(int)
#
#         country_table_df['difference'] = country_table_df['rig_count_after'] - country_table_df['rig_count_before']
#
#         country_table_df['rank'] = country_table_df['rig_count_after'].rank(method='min', ascending=False)
#
#         country_table_df_sort = country_table_df.sort_values(
#             by=['rig_count_after', 'difference'],
#             ascending=[False, False]
#         )
#
#         country_final_table_df = pd.DataFrame({
#             'RANK': [int(x) for x in country_table_df_sort['rank'].tolist()],
#             'COUNTRY': country_table_df_sort['country'].tolist(),
#             'RIGS': country_table_df_sort['rig_count_after'].tolist(),
#             '+/-': country_table_df_sort['difference'].tolist()
#         })
#
#         country_table_columns = [{
#             'name': i, 'id': i
#         } for i in country_final_table_df.columns]
#
#         country_table_data = country_final_table_df.to_dict('records')
#
#
#         return indicator_fig, map_fig, drill_for_fig, well_depth_fig, trajectory_fig, \
#             location_fig, state_table_columns, state_table_data, country_table_columns, country_table_data, \
#
#     elif dropdown_value == '1w':
#         reference_date = one_week_date
#         scatter_reference_date = one_year_date
#
#         df = functions.get_north_america_df(scatter_reference_date, date)
#
#         share_df = functions.get_df(reference_date, date)
#
#         filtered_df = df[
#             df['country'].isin(countries) &
#             df['state'].isin(states) &
#             df['basin'].isin(basins) &
#             df['drill_for'].isin(drill_for) &
#             df['location'].isin(locations) &
#             df['trajectory'].isin(trajectories) &
#             df['well_depth'].isin(well_depths)
#         ]
#
#         filtered_share_df = share_df[
#             share_df['state'].isin(states) &
#             share_df['basin'].isin(basins) &
#             share_df['drill_for'].isin(drill_for) &
#             share_df['location'].isin(locations) &
#             share_df['trajectory'].isin(trajectories) &
#             share_df['well_depth'].isin(well_depths)
#         ]
#
#         current_df = filtered_df[filtered_df['date'] == date]
#         reference_df = filtered_df[filtered_df['date'] == reference_date]
#
#         scatter_df = filtered_df[['date', 'rig_count']].groupby('date').sum().reset_index()
#
#         # county_scatter_df = filtered_df[['date', 'county']].groupby(['date'])['county'].nunique().reset_index()
#
#
#         indicator_data = [
#             go.Indicator(
#                 mode='number+delta',
#                 value=current_df['rig_count'].sum(),
#                 delta={'reference': reference_df['rig_count'].sum()},
#             ),
#             go.Scatter(
#                 name='1-YEAR TREND',
#                 x=scatter_df['date'].tolist(),
#                 y=scatter_df['rig_count'].tolist()
#             )
#         ]
#
#         indicator_layout = go.Layout(
#             # title='COGS',
#             # height=100,
#             title_text='RIG COUNT AND TRENDS FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             height=177
#         )
#
#         indicator_fig = go.Figure(data=indicator_data, layout=indicator_layout)
#
#
#         s = open('/Users/brettdavis/Downloads/us_states.json')
#         p = open('/Users/brettdavis/Downloads/canada_provinces.json')
#
#         states = json.load(s)
#         provinces = json.load(p)
#
#         states_and_provinces = {"type": "FeatureCollection", "features": states['features'] + provinces['features']}
#
#         for feature in states_and_provinces['features']:
#             feature['id'] = feature['properties']['name'].upper()
#
#         selected_week_df_raw = current_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index()
#
#         selected_week_df = selected_week_df_raw.rename(columns={'rig_count': 'rig_count_select'})
#
#         ref_week_df_raw = reference_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index()
#
#         ref_week_df = ref_week_df_raw.rename(columns={'rig_count': 'rig_count_ref'})
#
#         map_df = selected_week_df.merge(ref_week_df, 'outer', ['state'])
#
#         map_df['rig_count_ref'] = map_df['rig_count_ref'].fillna(0)
#         map_df['rig_count_select'] = map_df['rig_count_select'].fillna(0)
#
#         map_df['rig_count_ref'] = map_df['rig_count_ref'].astype(int)
#         map_df['rig_count_select'] = map_df['rig_count_select'].astype(int)
#
#         map_df['difference'] = map_df['rig_count_select'] - map_df['rig_count_ref']
#
#         # map_df = current_df[[
#         #     'state', 'rig_count'
#         # ]].groupby(['state']).sum().reset_index()
#
#         map_data = go.Choropleth(
#             name='States & Provinces',
#             geojson=states_and_provinces,
#             locations=map_df['state'],
#             z=map_df['difference'],
#             zmid=0,
#             colorscale=plus_minus_colorscale,
#             hovertemplate=map_df['state'] + '<br>Rig +/-: %{z}<br>Rig Count: ' + map_df['rig_count_select'].astype(str)
#         )
#
#         map_layout = go.Layout(
#             geo={
#                 'scope': 'north america',
#                 'showlakes': True,
#                 'fitbounds': 'locations'
#             },
#             title_text='STATE/PROVINCE-LEVEL 1-WEEK +/- HEAT MAP FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
#             titlefont={
#                 'size': 8
#             },
#             margin={
#                 'r': 0,
#                 't': 20,
#                 'l': 0,
#                 'b': 0
#             },
#             template="plotly_dark",
#             height=500
#         )
#
#         map_fig = go.Figure(data=map_data, layout=map_layout)
#
#         totals_df_raw = filtered_share_df[['date', 'rig_count']].groupby('date').sum().reset_index()
#         totals_df = totals_df_raw.rename(columns={'rig_count': 'overall_weekly_total'})
#
#         drill_for_df = filtered_share_df[[
#             'date',
#             'drill_for',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'drill_for'
#         ]).sum().reset_index()
#
#         drill_for_totals_df = drill_for_df.merge(totals_df, how='left', on='date')
#
#         drill_for_totals_df['share'] = (
#                     (drill_for_totals_df['rig_count']) / (drill_for_totals_df['overall_weekly_total']))
#
#         drill_for_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['date'],
#                 y=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in drill_for_totals_df['drill_for'].unique()
#         ]
#
#         drill_for_layout = go.Layout(
#             title_text='1W DRILL-FOR HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         drill_for_fig = go.Figure(data=drill_for_data, layout=drill_for_layout)
#
#         well_depth_df = filtered_share_df[[
#             'date',
#             'well_depth',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'well_depth'
#         ]).sum().reset_index()
#
#         well_depth_totals_df = well_depth_df.merge(totals_df, how='left', on='date')
#
#         well_depth_totals_df['share'] = (
#                 (well_depth_totals_df['rig_count']) / (well_depth_totals_df['overall_weekly_total'])
#         )
#
#         well_depth_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['date'],
#                 y=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in well_depth_totals_df['well_depth'].unique()
#         ]
#
#         well_depth_layout = go.Layout(
#             title_text='1W WELL-DEPTH HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         well_depth_fig = go.Figure(data=well_depth_data, layout=well_depth_layout)
#
#         trajectory_df = filtered_share_df[[
#             'date',
#             'trajectory',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'trajectory'
#         ]).sum().reset_index()
#
#         trajectory_totals_df = trajectory_df.merge(totals_df, how='left', on='date')
#
#         trajectory_totals_df['share'] = (
#                 (trajectory_totals_df['rig_count']) / (trajectory_totals_df['overall_weekly_total']))
#
#         trajectory_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['date'],
#                 y=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in trajectory_totals_df['trajectory'].unique()
#         ]
#
#         trajectory_layout = go.Layout(
#             title_text='1W TRAJECTORY HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         trajectory_fig = go.Figure(data=trajectory_data, layout=trajectory_layout)
#
#         location_df = filtered_share_df[[
#             'date',
#             'location',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'location'
#         ]).sum().reset_index()
#
#         location_totals_df = location_df.merge(totals_df, how='left', on='date')
#
#         location_totals_df['share'] = (
#                 (location_totals_df['rig_count']) / (location_totals_df['overall_weekly_total']))
#
#         location_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=location_totals_df[location_totals_df['location'] == i]['date'],
#                 y=location_totals_df[location_totals_df['location'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in location_totals_df['location'].unique()
#         ]
#
#         location_layout = go.Layout(
#             title_text='1W LOCATION HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         location_fig = go.Figure(data=location_data, layout=location_layout)
#
#
#         state_table_df_raw = current_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})
#
#         state_table_df_ref_raw = reference_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})
#
#         state_table_df = state_table_df_raw.merge(
#             state_table_df_ref_raw,
#             'outer',
#             ['state']
#         )
#
#         state_table_df['rig_count_after'] = state_table_df['rig_count_after'].fillna(0)
#         state_table_df['rig_count_before'] = state_table_df['rig_count_before'].fillna(0)
#
#         state_table_df['rig_count_after'] = state_table_df['rig_count_after'].astype(int)
#         state_table_df['rig_count_before'] = state_table_df['rig_count_before'].astype(int)
#
#         state_table_df['difference'] = state_table_df['rig_count_after'] - state_table_df['rig_count_before']
#
#         state_table_df['rank'] = state_table_df['difference'].rank(method='min', ascending=False)
#
#         state_table_df_sort = state_table_df.sort_values(
#             by=['difference', 'rig_count_after'],
#             ascending=[False, False]
#         )
#
#         state_final_table_df = pd.DataFrame({
#             'RANK': [int(x) for x in state_table_df_sort['rank'].tolist()],
#             'STATE/PROVINCE': state_table_df_sort['state'].tolist(),
#             'RIGS': state_table_df_sort['rig_count_after'].tolist(),
#             '+/-': state_table_df_sort['difference'].tolist()
#         })
#
#         state_table_columns = [{
#             'name': i, 'id': i
#         } for i in state_final_table_df.columns]
#
#         state_table_data = state_final_table_df.to_dict('records')
#
#         country_table_df_raw = current_df[[
#             'country', 'rig_count'
#         ]].groupby(['country']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})
#
#         country_table_df_ref_raw = reference_df[[
#             'country', 'rig_count'
#         ]].groupby(['country']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})
#
#         country_table_df = country_table_df_raw.merge(
#             country_table_df_ref_raw,
#             'outer',
#             ['country']
#         )
#
#         country_table_df['rig_count_after'] = country_table_df['rig_count_after'].fillna(0)
#         country_table_df['rig_count_before'] = country_table_df['rig_count_before'].fillna(0)
#
#         country_table_df['rig_count_after'] = country_table_df['rig_count_after'].astype(int)
#         country_table_df['rig_count_before'] = country_table_df['rig_count_before'].astype(int)
#
#         country_table_df['difference'] = country_table_df['rig_count_after'] - country_table_df['rig_count_before']
#
#         country_table_df['rank'] = country_table_df['difference'].rank(method='min', ascending=False)
#
#         country_table_df_sort = country_table_df.sort_values(
#             by=['difference', 'rig_count_after'],
#             ascending=[False, False]
#         )
#
#         country_final_table_df = pd.DataFrame({
#             'RANK': [int(x) for x in country_table_df_sort['rank'].tolist()],
#             'COUNTRY': country_table_df_sort['country'].tolist(),
#             'RIGS': country_table_df_sort['rig_count_after'].tolist(),
#             '+/-': country_table_df_sort['difference'].tolist()
#         })
#
#         country_table_columns = [{
#             'name': i, 'id': i
#         } for i in country_final_table_df.columns]
#
#         country_table_data = country_final_table_df.to_dict('records')
#
#
#         return indicator_fig, map_fig, drill_for_fig, well_depth_fig, trajectory_fig, \
#             location_fig, state_table_columns, state_table_data, country_table_columns, country_table_data, \
#
#
#     elif dropdown_value == '1m':
#         reference_date = one_month_date
#         scatter_reference_date = one_year_date
#
#         df = functions.get_north_america_df(scatter_reference_date, date)
#
#         share_df = functions.get_df(reference_date, date)
#
#         filtered_df = df[
#             df['country'].isin(countries) &
#             df['state'].isin(states) &
#             df['basin'].isin(basins) &
#             df['drill_for'].isin(drill_for) &
#             df['location'].isin(locations) &
#             df['trajectory'].isin(trajectories) &
#             df['well_depth'].isin(well_depths)
#         ]
#
#         filtered_share_df = share_df[
#             share_df['state'].isin(states) &
#             share_df['basin'].isin(basins) &
#             share_df['drill_for'].isin(drill_for) &
#             share_df['location'].isin(locations) &
#             share_df['trajectory'].isin(trajectories) &
#             share_df['well_depth'].isin(well_depths)
#         ]
#
#         current_df = filtered_df[filtered_df['date'] == date]
#         reference_df = filtered_df[filtered_df['date'] == reference_date]
#
#         scatter_df = filtered_df[['date', 'rig_count']].groupby('date').sum().reset_index()
#
#         # county_scatter_df = filtered_df[['date', 'county']].groupby(['date'])['county'].nunique().reset_index()
#
#
#         indicator_data = [
#             go.Indicator(
#                 mode='number+delta',
#                 value=current_df['rig_count'].sum(),
#                 delta={'reference': reference_df['rig_count'].sum()},
#             ),
#             go.Scatter(
#                 name='1-YEAR TREND',
#                 x=scatter_df['date'].tolist(),
#                 y=scatter_df['rig_count'].tolist()
#             )
#         ]
#
#         indicator_layout = go.Layout(
#             # title='COGS',
#             # height=100,
#             title_text='RIG COUNT AND TRENDS FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             height=177
#         )
#
#         indicator_fig = go.Figure(data=indicator_data, layout=indicator_layout)
#
#
#         s = open('/Users/brettdavis/Downloads/us_states.json')
#         p = open('/Users/brettdavis/Downloads/canada_provinces.json')
#
#         states = json.load(s)
#         provinces = json.load(p)
#
#         states_and_provinces = {"type": "FeatureCollection", "features": states['features'] + provinces['features']}
#
#         for feature in states_and_provinces['features']:
#             feature['id'] = feature['properties']['name'].upper()
#
#         selected_week_df_raw = current_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index()
#
#         selected_week_df = selected_week_df_raw.rename(columns={'rig_count': 'rig_count_select'})
#
#         ref_week_df_raw = reference_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index()
#
#         ref_week_df = ref_week_df_raw.rename(columns={'rig_count': 'rig_count_ref'})
#
#         map_df = selected_week_df.merge(ref_week_df, 'outer', ['state'])
#
#         map_df['rig_count_ref'] = map_df['rig_count_ref'].fillna(0)
#         map_df['rig_count_select'] = map_df['rig_count_select'].fillna(0)
#
#         map_df['rig_count_ref'] = map_df['rig_count_ref'].astype(int)
#         map_df['rig_count_select'] = map_df['rig_count_select'].astype(int)
#
#         map_df['difference'] = map_df['rig_count_select'] - map_df['rig_count_ref']
#
#         # map_df = current_df[[
#         #     'state', 'rig_count'
#         # ]].groupby(['state']).sum().reset_index()
#
#         map_data = go.Choropleth(
#             name='States & Provinces',
#             geojson=states_and_provinces,
#             locations=map_df['state'],
#             z=map_df['difference'],
#             zmid=0,
#             colorscale=plus_minus_colorscale,
#             hovertemplate=map_df['state'] + '<br>Rig +/-: %{z}<br>Rig Count: ' + map_df['rig_count_select'].astype(str)
#         )
#
#         map_layout = go.Layout(
#             geo={
#                 'scope': 'north america',
#                 'showlakes': True,
#                 'fitbounds': 'locations'
#             },
#             title_text='STATE/PROVINCE-LEVEL 1-MONTH +/- HEAT MAP FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
#             titlefont={
#                 'size': 8
#             },
#             margin={
#                 'r': 0,
#                 't': 20,
#                 'l': 0,
#                 'b': 0
#             },
#             template="plotly_dark",
#             height=500
#         )
#
#         map_fig = go.Figure(data=map_data, layout=map_layout)
#
#         totals_df_raw = filtered_share_df[['date', 'rig_count']].groupby('date').sum().reset_index()
#         totals_df = totals_df_raw.rename(columns={'rig_count': 'overall_weekly_total'})
#
#         drill_for_df = filtered_share_df[[
#             'date',
#             'drill_for',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'drill_for'
#         ]).sum().reset_index()
#
#         drill_for_totals_df = drill_for_df.merge(totals_df, how='left', on='date')
#
#         drill_for_totals_df['share'] = (
#                     (drill_for_totals_df['rig_count']) / (drill_for_totals_df['overall_weekly_total']))
#
#         drill_for_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['date'],
#                 y=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in drill_for_totals_df['drill_for'].unique()
#         ]
#
#         drill_for_layout = go.Layout(
#             title_text='1M DRILL-FOR HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         drill_for_fig = go.Figure(data=drill_for_data, layout=drill_for_layout)
#
#         well_depth_df = filtered_share_df[[
#             'date',
#             'well_depth',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'well_depth'
#         ]).sum().reset_index()
#
#         well_depth_totals_df = well_depth_df.merge(totals_df, how='left', on='date')
#
#         well_depth_totals_df['share'] = (
#                 (well_depth_totals_df['rig_count']) / (well_depth_totals_df['overall_weekly_total'])
#         )
#
#         well_depth_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['date'],
#                 y=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in well_depth_totals_df['well_depth'].unique()
#         ]
#
#         well_depth_layout = go.Layout(
#             title_text='1M WELL-DEPTH HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         well_depth_fig = go.Figure(data=well_depth_data, layout=well_depth_layout)
#
#         trajectory_df = filtered_share_df[[
#             'date',
#             'trajectory',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'trajectory'
#         ]).sum().reset_index()
#
#         trajectory_totals_df = trajectory_df.merge(totals_df, how='left', on='date')
#
#         trajectory_totals_df['share'] = (
#                 (trajectory_totals_df['rig_count']) / (trajectory_totals_df['overall_weekly_total']))
#
#         trajectory_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['date'],
#                 y=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in trajectory_totals_df['trajectory'].unique()
#         ]
#
#         trajectory_layout = go.Layout(
#             title_text='1M TRAJECTORY HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         trajectory_fig = go.Figure(data=trajectory_data, layout=trajectory_layout)
#
#         location_df = filtered_share_df[[
#             'date',
#             'location',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'location'
#         ]).sum().reset_index()
#
#         location_totals_df = location_df.merge(totals_df, how='left', on='date')
#
#         location_totals_df['share'] = (
#                 (location_totals_df['rig_count']) / (location_totals_df['overall_weekly_total']))
#
#         location_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=location_totals_df[location_totals_df['location'] == i]['date'],
#                 y=location_totals_df[location_totals_df['location'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in location_totals_df['location'].unique()
#         ]
#
#         location_layout = go.Layout(
#             title_text='1M LOCATION HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         location_fig = go.Figure(data=location_data, layout=location_layout)
#
#
#         state_table_df_raw = current_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})
#
#         state_table_df_ref_raw = reference_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})
#
#         state_table_df = state_table_df_raw.merge(
#             state_table_df_ref_raw,
#             'outer',
#             ['state']
#         )
#
#         state_table_df['rig_count_after'] = state_table_df['rig_count_after'].fillna(0)
#         state_table_df['rig_count_before'] = state_table_df['rig_count_before'].fillna(0)
#
#         state_table_df['rig_count_after'] = state_table_df['rig_count_after'].astype(int)
#         state_table_df['rig_count_before'] = state_table_df['rig_count_before'].astype(int)
#
#         state_table_df['difference'] = state_table_df['rig_count_after'] - state_table_df['rig_count_before']
#
#         state_table_df['rank'] = state_table_df['difference'].rank(method='min', ascending=False)
#
#         state_table_df_sort = state_table_df.sort_values(
#             by=['difference', 'rig_count_after'],
#             ascending=[False, False]
#         )
#
#         state_final_table_df = pd.DataFrame({
#             'RANK': [int(x) for x in state_table_df_sort['rank'].tolist()],
#             'STATE/PROVINCE': state_table_df_sort['state'].tolist(),
#             'RIGS': state_table_df_sort['rig_count_after'].tolist(),
#             '+/-': state_table_df_sort['difference'].tolist()
#         })
#
#         state_table_columns = [{
#             'name': i, 'id': i
#         } for i in state_final_table_df.columns]
#
#         state_table_data = state_final_table_df.to_dict('records')
#
#         country_table_df_raw = current_df[[
#             'country', 'rig_count'
#         ]].groupby(['country']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})
#
#         country_table_df_ref_raw = reference_df[[
#             'country', 'rig_count'
#         ]].groupby(['country']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})
#
#         country_table_df = country_table_df_raw.merge(
#             country_table_df_ref_raw,
#             'outer',
#             ['country']
#         )
#
#         country_table_df['rig_count_after'] = country_table_df['rig_count_after'].fillna(0)
#         country_table_df['rig_count_before'] = country_table_df['rig_count_before'].fillna(0)
#
#         country_table_df['rig_count_after'] = country_table_df['rig_count_after'].astype(int)
#         country_table_df['rig_count_before'] = country_table_df['rig_count_before'].astype(int)
#
#         country_table_df['difference'] = country_table_df['rig_count_after'] - country_table_df['rig_count_before']
#
#         country_table_df['rank'] = country_table_df['difference'].rank(method='min', ascending=False)
#
#         country_table_df_sort = country_table_df.sort_values(
#             by=['difference', 'rig_count_after'],
#             ascending=[False, False]
#         )
#
#         country_final_table_df = pd.DataFrame({
#             'RANK': [int(x) for x in country_table_df_sort['rank'].tolist()],
#             'COUNTRY': country_table_df_sort['country'].tolist(),
#             'RIGS': country_table_df_sort['rig_count_after'].tolist(),
#             '+/-': country_table_df_sort['difference'].tolist()
#         })
#
#         country_table_columns = [{
#             'name': i, 'id': i
#         } for i in country_final_table_df.columns]
#
#         country_table_data = country_final_table_df.to_dict('records')
#
#
#         return indicator_fig, map_fig, drill_for_fig, well_depth_fig, trajectory_fig, \
#             location_fig, state_table_columns, state_table_data, country_table_columns, country_table_data, \
#
#
#     elif dropdown_value == '3m':
#         reference_date = three_month_date
#         scatter_reference_date = one_year_date
#
#         df = functions.get_north_america_df(scatter_reference_date, date)
#
#         share_df = functions.get_df(reference_date, date)
#
#         filtered_df = df[
#             df['country'].isin(countries) &
#             df['state'].isin(states) &
#             df['basin'].isin(basins) &
#             df['drill_for'].isin(drill_for) &
#             df['location'].isin(locations) &
#             df['trajectory'].isin(trajectories) &
#             df['well_depth'].isin(well_depths)
#         ]
#
#         filtered_share_df = share_df[
#             share_df['state'].isin(states) &
#             share_df['basin'].isin(basins) &
#             share_df['drill_for'].isin(drill_for) &
#             share_df['location'].isin(locations) &
#             share_df['trajectory'].isin(trajectories) &
#             share_df['well_depth'].isin(well_depths)
#         ]
#
#         current_df = filtered_df[filtered_df['date'] == date]
#         reference_df = filtered_df[filtered_df['date'] == reference_date]
#
#         scatter_df = filtered_df[['date', 'rig_count']].groupby('date').sum().reset_index()
#
#         # county_scatter_df = filtered_df[['date', 'county']].groupby(['date'])['county'].nunique().reset_index()
#
#
#         indicator_data = [
#             go.Indicator(
#                 mode='number+delta',
#                 value=current_df['rig_count'].sum(),
#                 delta={'reference': reference_df['rig_count'].sum()},
#             ),
#             go.Scatter(
#                 name='1-YEAR TREND',
#                 x=scatter_df['date'].tolist(),
#                 y=scatter_df['rig_count'].tolist()
#             )
#         ]
#
#         indicator_layout = go.Layout(
#             # title='COGS',
#             # height=100,
#             title_text='RIG COUNT AND TRENDS FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             height=177
#         )
#
#         indicator_fig = go.Figure(data=indicator_data, layout=indicator_layout)
#
#
#         s = open('/Users/brettdavis/Downloads/us_states.json')
#         p = open('/Users/brettdavis/Downloads/canada_provinces.json')
#
#         states = json.load(s)
#         provinces = json.load(p)
#
#         states_and_provinces = {"type": "FeatureCollection", "features": states['features'] + provinces['features']}
#
#         for feature in states_and_provinces['features']:
#             feature['id'] = feature['properties']['name'].upper()
#
#         selected_week_df_raw = current_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index()
#
#         selected_week_df = selected_week_df_raw.rename(columns={'rig_count': 'rig_count_select'})
#
#         ref_week_df_raw = reference_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index()
#
#         ref_week_df = ref_week_df_raw.rename(columns={'rig_count': 'rig_count_ref'})
#
#         map_df = selected_week_df.merge(ref_week_df, 'outer', ['state'])
#
#         map_df['rig_count_ref'] = map_df['rig_count_ref'].fillna(0)
#         map_df['rig_count_select'] = map_df['rig_count_select'].fillna(0)
#
#         map_df['rig_count_ref'] = map_df['rig_count_ref'].astype(int)
#         map_df['rig_count_select'] = map_df['rig_count_select'].astype(int)
#
#         map_df['difference'] = map_df['rig_count_select'] - map_df['rig_count_ref']
#
#         # map_df = current_df[[
#         #     'state', 'rig_count'
#         # ]].groupby(['state']).sum().reset_index()
#
#         map_data = go.Choropleth(
#             name='States & Provinces',
#             geojson=states_and_provinces,
#             locations=map_df['state'],
#             z=map_df['difference'],
#             zmid=0,
#             colorscale=plus_minus_colorscale,
#             hovertemplate=map_df['state'] + '<br>Rig +/-: %{z}<br>Rig Count: ' + map_df['rig_count_select'].astype(str)
#         )
#
#         map_layout = go.Layout(
#             geo={
#                 'scope': 'north america',
#                 'showlakes': True,
#                 'fitbounds': 'locations'
#             },
#             title_text='STATE/PROVINCE-LEVEL 3-MONTH +/- HEAT MAP FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
#             titlefont={
#                 'size': 8
#             },
#             margin={
#                 'r': 0,
#                 't': 20,
#                 'l': 0,
#                 'b': 0
#             },
#             template="plotly_dark",
#             height=500
#         )
#
#         map_fig = go.Figure(data=map_data, layout=map_layout)
#
#         totals_df_raw = filtered_share_df[['date', 'rig_count']].groupby('date').sum().reset_index()
#         totals_df = totals_df_raw.rename(columns={'rig_count': 'overall_weekly_total'})
#
#         drill_for_df = filtered_share_df[[
#             'date',
#             'drill_for',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'drill_for'
#         ]).sum().reset_index()
#
#         drill_for_totals_df = drill_for_df.merge(totals_df, how='left', on='date')
#
#         drill_for_totals_df['share'] = (
#                     (drill_for_totals_df['rig_count']) / (drill_for_totals_df['overall_weekly_total']))
#
#         drill_for_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['date'],
#                 y=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in drill_for_totals_df['drill_for'].unique()
#         ]
#
#         drill_for_layout = go.Layout(
#             title_text='3M DRILL-FOR HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         drill_for_fig = go.Figure(data=drill_for_data, layout=drill_for_layout)
#
#         well_depth_df = filtered_share_df[[
#             'date',
#             'well_depth',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'well_depth'
#         ]).sum().reset_index()
#
#         well_depth_totals_df = well_depth_df.merge(totals_df, how='left', on='date')
#
#         well_depth_totals_df['share'] = (
#                 (well_depth_totals_df['rig_count']) / (well_depth_totals_df['overall_weekly_total'])
#         )
#
#         well_depth_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['date'],
#                 y=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in well_depth_totals_df['well_depth'].unique()
#         ]
#
#         well_depth_layout = go.Layout(
#             title_text='3M WELL-DEPTH HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         well_depth_fig = go.Figure(data=well_depth_data, layout=well_depth_layout)
#
#         trajectory_df = filtered_share_df[[
#             'date',
#             'trajectory',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'trajectory'
#         ]).sum().reset_index()
#
#         trajectory_totals_df = trajectory_df.merge(totals_df, how='left', on='date')
#
#         trajectory_totals_df['share'] = (
#                 (trajectory_totals_df['rig_count']) / (trajectory_totals_df['overall_weekly_total']))
#
#         trajectory_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['date'],
#                 y=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in trajectory_totals_df['trajectory'].unique()
#         ]
#
#         trajectory_layout = go.Layout(
#             title_text='3M TRAJECTORY HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         trajectory_fig = go.Figure(data=trajectory_data, layout=trajectory_layout)
#
#         location_df = filtered_share_df[[
#             'date',
#             'location',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'location'
#         ]).sum().reset_index()
#
#         location_totals_df = location_df.merge(totals_df, how='left', on='date')
#
#         location_totals_df['share'] = (
#                 (location_totals_df['rig_count']) / (location_totals_df['overall_weekly_total']))
#
#         location_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=location_totals_df[location_totals_df['location'] == i]['date'],
#                 y=location_totals_df[location_totals_df['location'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in location_totals_df['location'].unique()
#         ]
#
#         location_layout = go.Layout(
#             title_text='3M LOCATION HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         location_fig = go.Figure(data=location_data, layout=location_layout)
#
#
#         state_table_df_raw = current_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})
#
#         state_table_df_ref_raw = reference_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})
#
#         state_table_df = state_table_df_raw.merge(
#             state_table_df_ref_raw,
#             'outer',
#             ['state']
#         )
#
#         state_table_df['rig_count_after'] = state_table_df['rig_count_after'].fillna(0)
#         state_table_df['rig_count_before'] = state_table_df['rig_count_before'].fillna(0)
#
#         state_table_df['rig_count_after'] = state_table_df['rig_count_after'].astype(int)
#         state_table_df['rig_count_before'] = state_table_df['rig_count_before'].astype(int)
#
#         state_table_df['difference'] = state_table_df['rig_count_after'] - state_table_df['rig_count_before']
#
#         state_table_df['rank'] = state_table_df['difference'].rank(method='min', ascending=False)
#
#         state_table_df_sort = state_table_df.sort_values(
#             by=['difference', 'rig_count_after'],
#             ascending=[False, False]
#         )
#
#         state_final_table_df = pd.DataFrame({
#             'RANK': [int(x) for x in state_table_df_sort['rank'].tolist()],
#             'STATE/PROVINCE': state_table_df_sort['state'].tolist(),
#             'RIGS': state_table_df_sort['rig_count_after'].tolist(),
#             '+/-': state_table_df_sort['difference'].tolist()
#         })
#
#         state_table_columns = [{
#             'name': i, 'id': i
#         } for i in state_final_table_df.columns]
#
#         state_table_data = state_final_table_df.to_dict('records')
#
#         country_table_df_raw = current_df[[
#             'country', 'rig_count'
#         ]].groupby(['country']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})
#
#         country_table_df_ref_raw = reference_df[[
#             'country', 'rig_count'
#         ]].groupby(['country']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})
#
#         country_table_df = country_table_df_raw.merge(
#             country_table_df_ref_raw,
#             'outer',
#             ['country']
#         )
#
#         country_table_df['rig_count_after'] = country_table_df['rig_count_after'].fillna(0)
#         country_table_df['rig_count_before'] = country_table_df['rig_count_before'].fillna(0)
#
#         country_table_df['rig_count_after'] = country_table_df['rig_count_after'].astype(int)
#         country_table_df['rig_count_before'] = country_table_df['rig_count_before'].astype(int)
#
#         country_table_df['difference'] = country_table_df['rig_count_after'] - country_table_df['rig_count_before']
#
#         country_table_df['rank'] = country_table_df['difference'].rank(method='min', ascending=False)
#
#         country_table_df_sort = country_table_df.sort_values(
#             by=['difference', 'rig_count_after'],
#             ascending=[False, False]
#         )
#
#         country_final_table_df = pd.DataFrame({
#             'RANK': [int(x) for x in country_table_df_sort['rank'].tolist()],
#             'COUNTRY': country_table_df_sort['country'].tolist(),
#             'RIGS': country_table_df_sort['rig_count_after'].tolist(),
#             '+/-': country_table_df_sort['difference'].tolist()
#         })
#
#         country_table_columns = [{
#             'name': i, 'id': i
#         } for i in country_final_table_df.columns]
#
#         country_table_data = country_final_table_df.to_dict('records')
#
#
#         return indicator_fig, map_fig, drill_for_fig, well_depth_fig, trajectory_fig, \
#             location_fig, state_table_columns, state_table_data, country_table_columns, country_table_data, \
#
#     elif dropdown_value == '6m':
#         reference_date = six_month_date
#         scatter_reference_date = one_year_date
#
#         df = functions.get_north_america_df(scatter_reference_date, date)
#
#         share_df = functions.get_df(reference_date, date)
#
#         filtered_df = df[
#             df['country'].isin(countries) &
#             df['state'].isin(states) &
#             df['basin'].isin(basins) &
#             df['drill_for'].isin(drill_for) &
#             df['location'].isin(locations) &
#             df['trajectory'].isin(trajectories) &
#             df['well_depth'].isin(well_depths)
#         ]
#
#         filtered_share_df = share_df[
#             share_df['state'].isin(states) &
#             share_df['basin'].isin(basins) &
#             share_df['drill_for'].isin(drill_for) &
#             share_df['location'].isin(locations) &
#             share_df['trajectory'].isin(trajectories) &
#             share_df['well_depth'].isin(well_depths)
#         ]
#
#         current_df = filtered_df[filtered_df['date'] == date]
#         reference_df = filtered_df[filtered_df['date'] == reference_date]
#
#         scatter_df = filtered_df[['date', 'rig_count']].groupby('date').sum().reset_index()
#
#         # county_scatter_df = filtered_df[['date', 'county']].groupby(['date'])['county'].nunique().reset_index()
#
#
#         indicator_data = [
#             go.Indicator(
#                 mode='number+delta',
#                 value=current_df['rig_count'].sum(),
#                 delta={'reference': reference_df['rig_count'].sum()},
#             ),
#             go.Scatter(
#                 name='1-YEAR TREND',
#                 x=scatter_df['date'].tolist(),
#                 y=scatter_df['rig_count'].tolist()
#             )
#         ]
#
#         indicator_layout = go.Layout(
#             # title='COGS',
#             # height=100,
#             title_text='RIG COUNT AND TRENDS FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             height=177
#         )
#
#         indicator_fig = go.Figure(data=indicator_data, layout=indicator_layout)
#
#
#         s = open('/Users/brettdavis/Downloads/us_states.json')
#         p = open('/Users/brettdavis/Downloads/canada_provinces.json')
#
#         states = json.load(s)
#         provinces = json.load(p)
#
#         states_and_provinces = {"type": "FeatureCollection", "features": states['features'] + provinces['features']}
#
#         for feature in states_and_provinces['features']:
#             feature['id'] = feature['properties']['name'].upper()
#
#         selected_week_df_raw = current_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index()
#
#         selected_week_df = selected_week_df_raw.rename(columns={'rig_count': 'rig_count_select'})
#
#         ref_week_df_raw = reference_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index()
#
#         ref_week_df = ref_week_df_raw.rename(columns={'rig_count': 'rig_count_ref'})
#
#         map_df = selected_week_df.merge(ref_week_df, 'outer', ['state'])
#
#         map_df['rig_count_ref'] = map_df['rig_count_ref'].fillna(0)
#         map_df['rig_count_select'] = map_df['rig_count_select'].fillna(0)
#
#         map_df['rig_count_ref'] = map_df['rig_count_ref'].astype(int)
#         map_df['rig_count_select'] = map_df['rig_count_select'].astype(int)
#
#         map_df['difference'] = map_df['rig_count_select'] - map_df['rig_count_ref']
#
#         # map_df = current_df[[
#         #     'state', 'rig_count'
#         # ]].groupby(['state']).sum().reset_index()
#
#         map_data = go.Choropleth(
#             name='States & Provinces',
#             geojson=states_and_provinces,
#             locations=map_df['state'],
#             z=map_df['difference'],
#             zmid=0,
#             colorscale=plus_minus_colorscale,
#             hovertemplate=map_df['state'] + '<br>Rig +/-: %{z}<br>Rig Count: ' + map_df['rig_count_select'].astype(str)
#         )
#
#         map_layout = go.Layout(
#             geo={
#                 'scope': 'north america',
#                 'showlakes': True,
#                 'fitbounds': 'locations'
#             },
#             title_text='STATE/PROVINCE-LEVEL 6-MONTH +/- HEAT MAP FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
#             titlefont={
#                 'size': 8
#             },
#             margin={
#                 'r': 0,
#                 't': 20,
#                 'l': 0,
#                 'b': 0
#             },
#             template="plotly_dark",
#             height=500
#         )
#
#         map_fig = go.Figure(data=map_data, layout=map_layout)
#
#         totals_df_raw = filtered_share_df[['date', 'rig_count']].groupby('date').sum().reset_index()
#         totals_df = totals_df_raw.rename(columns={'rig_count': 'overall_weekly_total'})
#
#         drill_for_df = filtered_share_df[[
#             'date',
#             'drill_for',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'drill_for'
#         ]).sum().reset_index()
#
#         drill_for_totals_df = drill_for_df.merge(totals_df, how='left', on='date')
#
#         drill_for_totals_df['share'] = (
#                     (drill_for_totals_df['rig_count']) / (drill_for_totals_df['overall_weekly_total']))
#
#         drill_for_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['date'],
#                 y=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in drill_for_totals_df['drill_for'].unique()
#         ]
#
#         drill_for_layout = go.Layout(
#             title_text='6M DRILL-FOR HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         drill_for_fig = go.Figure(data=drill_for_data, layout=drill_for_layout)
#
#         well_depth_df = filtered_share_df[[
#             'date',
#             'well_depth',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'well_depth'
#         ]).sum().reset_index()
#
#         well_depth_totals_df = well_depth_df.merge(totals_df, how='left', on='date')
#
#         well_depth_totals_df['share'] = (
#                 (well_depth_totals_df['rig_count']) / (well_depth_totals_df['overall_weekly_total'])
#         )
#
#         well_depth_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['date'],
#                 y=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in well_depth_totals_df['well_depth'].unique()
#         ]
#
#         well_depth_layout = go.Layout(
#             title_text='6M WELL-DEPTH HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         well_depth_fig = go.Figure(data=well_depth_data, layout=well_depth_layout)
#
#         trajectory_df = filtered_share_df[[
#             'date',
#             'trajectory',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'trajectory'
#         ]).sum().reset_index()
#
#         trajectory_totals_df = trajectory_df.merge(totals_df, how='left', on='date')
#
#         trajectory_totals_df['share'] = (
#                 (trajectory_totals_df['rig_count']) / (trajectory_totals_df['overall_weekly_total']))
#
#         trajectory_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['date'],
#                 y=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in trajectory_totals_df['trajectory'].unique()
#         ]
#
#         trajectory_layout = go.Layout(
#             title_text='6M TRAJECTORY HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         trajectory_fig = go.Figure(data=trajectory_data, layout=trajectory_layout)
#
#         location_df = filtered_share_df[[
#             'date',
#             'location',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'location'
#         ]).sum().reset_index()
#
#         location_totals_df = location_df.merge(totals_df, how='left', on='date')
#
#         location_totals_df['share'] = (
#                 (location_totals_df['rig_count']) / (location_totals_df['overall_weekly_total']))
#
#         location_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=location_totals_df[location_totals_df['location'] == i]['date'],
#                 y=location_totals_df[location_totals_df['location'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in location_totals_df['location'].unique()
#         ]
#
#         location_layout = go.Layout(
#             title_text='6M LOCATION HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         location_fig = go.Figure(data=location_data, layout=location_layout)
#
#
#         state_table_df_raw = current_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})
#
#         state_table_df_ref_raw = reference_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})
#
#         state_table_df = state_table_df_raw.merge(
#             state_table_df_ref_raw,
#             'outer',
#             ['state']
#         )
#
#         state_table_df['rig_count_after'] = state_table_df['rig_count_after'].fillna(0)
#         state_table_df['rig_count_before'] = state_table_df['rig_count_before'].fillna(0)
#
#         state_table_df['rig_count_after'] = state_table_df['rig_count_after'].astype(int)
#         state_table_df['rig_count_before'] = state_table_df['rig_count_before'].astype(int)
#
#         state_table_df['difference'] = state_table_df['rig_count_after'] - state_table_df['rig_count_before']
#
#         state_table_df['rank'] = state_table_df['difference'].rank(method='min', ascending=False)
#
#         state_table_df_sort = state_table_df.sort_values(
#             by=['difference', 'rig_count_after'],
#             ascending=[False, False]
#         )
#
#         state_final_table_df = pd.DataFrame({
#             'RANK': [int(x) for x in state_table_df_sort['rank'].tolist()],
#             'STATE/PROVINCE': state_table_df_sort['state'].tolist(),
#             'RIGS': state_table_df_sort['rig_count_after'].tolist(),
#             '+/-': state_table_df_sort['difference'].tolist()
#         })
#
#         state_table_columns = [{
#             'name': i, 'id': i
#         } for i in state_final_table_df.columns]
#
#         state_table_data = state_final_table_df.to_dict('records')
#
#         country_table_df_raw = current_df[[
#             'country', 'rig_count'
#         ]].groupby(['country']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})
#
#         country_table_df_ref_raw = reference_df[[
#             'country', 'rig_count'
#         ]].groupby(['country']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})
#
#         country_table_df = country_table_df_raw.merge(
#             country_table_df_ref_raw,
#             'outer',
#             ['country']
#         )
#
#         country_table_df['rig_count_after'] = country_table_df['rig_count_after'].fillna(0)
#         country_table_df['rig_count_before'] = country_table_df['rig_count_before'].fillna(0)
#
#         country_table_df['rig_count_after'] = country_table_df['rig_count_after'].astype(int)
#         country_table_df['rig_count_before'] = country_table_df['rig_count_before'].astype(int)
#
#         country_table_df['difference'] = country_table_df['rig_count_after'] - country_table_df['rig_count_before']
#
#         country_table_df['rank'] = country_table_df['difference'].rank(method='min', ascending=False)
#
#         country_table_df_sort = country_table_df.sort_values(
#             by=['difference', 'rig_count_after'],
#             ascending=[False, False]
#         )
#
#         country_final_table_df = pd.DataFrame({
#             'RANK': [int(x) for x in country_table_df_sort['rank'].tolist()],
#             'COUNTRY': country_table_df_sort['country'].tolist(),
#             'RIGS': country_table_df_sort['rig_count_after'].tolist(),
#             '+/-': country_table_df_sort['difference'].tolist()
#         })
#
#         country_table_columns = [{
#             'name': i, 'id': i
#         } for i in country_final_table_df.columns]
#
#         country_table_data = country_final_table_df.to_dict('records')
#
#
#         return indicator_fig, map_fig, drill_for_fig, well_depth_fig, trajectory_fig, \
#             location_fig, state_table_columns, state_table_data, country_table_columns, country_table_data, \
#
#
#     elif dropdown_value == '1y':
#         reference_date = one_year_date
#         scatter_reference_date = reference_date
#
#         df = functions.get_north_america_df(scatter_reference_date, date)
#
#         share_df = functions.get_df(reference_date, date)
#
#         filtered_df = df[
#             df['country'].isin(countries) &
#             df['state'].isin(states) &
#             df['basin'].isin(basins) &
#             df['drill_for'].isin(drill_for) &
#             df['location'].isin(locations) &
#             df['trajectory'].isin(trajectories) &
#             df['well_depth'].isin(well_depths)
#         ]
#
#         filtered_share_df = share_df[
#             share_df['state'].isin(states) &
#             share_df['basin'].isin(basins) &
#             share_df['drill_for'].isin(drill_for) &
#             share_df['location'].isin(locations) &
#             share_df['trajectory'].isin(trajectories) &
#             share_df['well_depth'].isin(well_depths)
#         ]
#
#         current_df = filtered_df[filtered_df['date'] == date]
#         reference_df = filtered_df[filtered_df['date'] == reference_date]
#
#         scatter_df = filtered_df[['date', 'rig_count']].groupby('date').sum().reset_index()
#
#         # county_scatter_df = filtered_df[['date', 'county']].groupby(['date'])['county'].nunique().reset_index()
#
#
#         indicator_data = [
#             go.Indicator(
#                 mode='number+delta',
#                 value=current_df['rig_count'].sum(),
#                 delta={'reference': reference_df['rig_count'].sum()},
#             ),
#             go.Scatter(
#                 name='1-YEAR TREND',
#                 x=scatter_df['date'].tolist(),
#                 y=scatter_df['rig_count'].tolist()
#             )
#         ]
#
#         indicator_layout = go.Layout(
#             # title='COGS',
#             # height=100,
#             title_text='RIG COUNT AND TRENDS FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             height=177
#         )
#
#         indicator_fig = go.Figure(data=indicator_data, layout=indicator_layout)
#
#
#         s = open('/Users/brettdavis/Downloads/us_states.json')
#         p = open('/Users/brettdavis/Downloads/canada_provinces.json')
#
#         states = json.load(s)
#         provinces = json.load(p)
#
#         states_and_provinces = {"type": "FeatureCollection", "features": states['features'] + provinces['features']}
#
#         for feature in states_and_provinces['features']:
#             feature['id'] = feature['properties']['name'].upper()
#
#         selected_week_df_raw = current_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index()
#
#         selected_week_df = selected_week_df_raw.rename(columns={'rig_count': 'rig_count_select'})
#
#         ref_week_df_raw = reference_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index()
#
#         ref_week_df = ref_week_df_raw.rename(columns={'rig_count': 'rig_count_ref'})
#
#         map_df = selected_week_df.merge(ref_week_df, 'outer', ['state'])
#
#         map_df['rig_count_ref'] = map_df['rig_count_ref'].fillna(0)
#         map_df['rig_count_select'] = map_df['rig_count_select'].fillna(0)
#
#         map_df['rig_count_ref'] = map_df['rig_count_ref'].astype(int)
#         map_df['rig_count_select'] = map_df['rig_count_select'].astype(int)
#
#         map_df['difference'] = map_df['rig_count_select'] - map_df['rig_count_ref']
#
#         # map_df = current_df[[
#         #     'state', 'rig_count'
#         # ]].groupby(['state']).sum().reset_index()
#
#         map_data = go.Choropleth(
#             name='States & Provinces',
#             geojson=states_and_provinces,
#             locations=map_df['state'],
#             z=map_df['difference'],
#             zmid=0,
#             colorscale=plus_minus_colorscale,
#             hovertemplate=map_df['state'] + '<br>Rig +/-: %{z}<br>Rig Count: ' + map_df['rig_count_select'].astype(str)
#         )
#
#         map_layout = go.Layout(
#             geo={
#                 'scope': 'north america',
#                 'showlakes': True,
#                 'fitbounds': 'locations'
#             },
#             title_text='STATE/PROVINCE-LEVEL 1-YEAR +/- HEAT MAP FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
#             titlefont={
#                 'size': 8
#             },
#             margin={
#                 'r': 0,
#                 't': 20,
#                 'l': 0,
#                 'b': 0
#             },
#             template="plotly_dark",
#             height=500
#         )
#
#         map_fig = go.Figure(data=map_data, layout=map_layout)
#
#         totals_df_raw = filtered_share_df[['date', 'rig_count']].groupby('date').sum().reset_index()
#         totals_df = totals_df_raw.rename(columns={'rig_count': 'overall_weekly_total'})
#
#         drill_for_df = filtered_share_df[[
#             'date',
#             'drill_for',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'drill_for'
#         ]).sum().reset_index()
#
#         drill_for_totals_df = drill_for_df.merge(totals_df, how='left', on='date')
#
#         drill_for_totals_df['share'] = (
#                     (drill_for_totals_df['rig_count']) / (drill_for_totals_df['overall_weekly_total']))
#
#         drill_for_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['date'],
#                 y=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in drill_for_totals_df['drill_for'].unique()
#         ]
#
#         drill_for_layout = go.Layout(
#             title_text='1Y DRILL-FOR HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         drill_for_fig = go.Figure(data=drill_for_data, layout=drill_for_layout)
#
#         well_depth_df = filtered_share_df[[
#             'date',
#             'well_depth',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'well_depth'
#         ]).sum().reset_index()
#
#         well_depth_totals_df = well_depth_df.merge(totals_df, how='left', on='date')
#
#         well_depth_totals_df['share'] = (
#                 (well_depth_totals_df['rig_count']) / (well_depth_totals_df['overall_weekly_total'])
#         )
#
#         well_depth_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['date'],
#                 y=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in well_depth_totals_df['well_depth'].unique()
#         ]
#
#         well_depth_layout = go.Layout(
#             title_text='1Y WELL-DEPTH HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         well_depth_fig = go.Figure(data=well_depth_data, layout=well_depth_layout)
#
#         trajectory_df = filtered_share_df[[
#             'date',
#             'trajectory',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'trajectory'
#         ]).sum().reset_index()
#
#         trajectory_totals_df = trajectory_df.merge(totals_df, how='left', on='date')
#
#         trajectory_totals_df['share'] = (
#                 (trajectory_totals_df['rig_count']) / (trajectory_totals_df['overall_weekly_total']))
#
#         trajectory_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['date'],
#                 y=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in trajectory_totals_df['trajectory'].unique()
#         ]
#
#         trajectory_layout = go.Layout(
#             title_text='1Y TRAJECTORY HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         trajectory_fig = go.Figure(data=trajectory_data, layout=trajectory_layout)
#
#         location_df = filtered_share_df[[
#             'date',
#             'location',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'location'
#         ]).sum().reset_index()
#
#         location_totals_df = location_df.merge(totals_df, how='left', on='date')
#
#         location_totals_df['share'] = (
#                 (location_totals_df['rig_count']) / (location_totals_df['overall_weekly_total']))
#
#         location_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=location_totals_df[location_totals_df['location'] == i]['date'],
#                 y=location_totals_df[location_totals_df['location'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in location_totals_df['location'].unique()
#         ]
#
#         location_layout = go.Layout(
#             title_text='1Y LOCATION HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         location_fig = go.Figure(data=location_data, layout=location_layout)
#
#
#         state_table_df_raw = current_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})
#
#         state_table_df_ref_raw = reference_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})
#
#         state_table_df = state_table_df_raw.merge(
#             state_table_df_ref_raw,
#             'outer',
#             ['state']
#         )
#
#         state_table_df['rig_count_after'] = state_table_df['rig_count_after'].fillna(0)
#         state_table_df['rig_count_before'] = state_table_df['rig_count_before'].fillna(0)
#
#         state_table_df['rig_count_after'] = state_table_df['rig_count_after'].astype(int)
#         state_table_df['rig_count_before'] = state_table_df['rig_count_before'].astype(int)
#
#         state_table_df['difference'] = state_table_df['rig_count_after'] - state_table_df['rig_count_before']
#
#         state_table_df['rank'] = state_table_df['difference'].rank(method='min', ascending=False)
#
#         state_table_df_sort = state_table_df.sort_values(
#             by=['difference', 'rig_count_after'],
#             ascending=[False, False]
#         )
#
#         state_final_table_df = pd.DataFrame({
#             'RANK': [int(x) for x in state_table_df_sort['rank'].tolist()],
#             'STATE/PROVINCE': state_table_df_sort['state'].tolist(),
#             'RIGS': state_table_df_sort['rig_count_after'].tolist(),
#             '+/-': state_table_df_sort['difference'].tolist()
#         })
#
#         state_table_columns = [{
#             'name': i, 'id': i
#         } for i in state_final_table_df.columns]
#
#         state_table_data = state_final_table_df.to_dict('records')
#
#         country_table_df_raw = current_df[[
#             'country', 'rig_count'
#         ]].groupby(['country']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})
#
#         country_table_df_ref_raw = reference_df[[
#             'country', 'rig_count'
#         ]].groupby(['country']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})
#
#         country_table_df = country_table_df_raw.merge(
#             country_table_df_ref_raw,
#             'outer',
#             ['country']
#         )
#
#         country_table_df['rig_count_after'] = country_table_df['rig_count_after'].fillna(0)
#         country_table_df['rig_count_before'] = country_table_df['rig_count_before'].fillna(0)
#
#         country_table_df['rig_count_after'] = country_table_df['rig_count_after'].astype(int)
#         country_table_df['rig_count_before'] = country_table_df['rig_count_before'].astype(int)
#
#         country_table_df['difference'] = country_table_df['rig_count_after'] - country_table_df['rig_count_before']
#
#         country_table_df['rank'] = country_table_df['difference'].rank(method='min', ascending=False)
#
#         country_table_df_sort = country_table_df.sort_values(
#             by=['difference', 'rig_count_after'],
#             ascending=[False, False]
#         )
#
#         country_final_table_df = pd.DataFrame({
#             'RANK': [int(x) for x in country_table_df_sort['rank'].tolist()],
#             'COUNTRY': country_table_df_sort['country'].tolist(),
#             'RIGS': country_table_df_sort['rig_count_after'].tolist(),
#             '+/-': country_table_df_sort['difference'].tolist()
#         })
#
#         country_table_columns = [{
#             'name': i, 'id': i
#         } for i in country_final_table_df.columns]
#
#         country_table_data = country_final_table_df.to_dict('records')
#
#
#         return indicator_fig, map_fig, drill_for_fig, well_depth_fig, trajectory_fig, \
#             location_fig, state_table_columns, state_table_data, country_table_columns, country_table_data, \
#
#
#     elif dropdown_value == '5y':
#         reference_date = five_year_date
#         scatter_reference_date = reference_date
#
#         df = functions.get_north_america_df(scatter_reference_date, date)
#
#         share_df = functions.get_df(reference_date, date)
#
#         filtered_df = df[
#             df['country'].isin(countries) &
#             df['state'].isin(states) &
#             df['basin'].isin(basins) &
#             df['drill_for'].isin(drill_for) &
#             df['location'].isin(locations) &
#             df['trajectory'].isin(trajectories) &
#             df['well_depth'].isin(well_depths)
#         ]
#
#         filtered_share_df = share_df[
#             share_df['state'].isin(states) &
#             share_df['basin'].isin(basins) &
#             share_df['drill_for'].isin(drill_for) &
#             share_df['location'].isin(locations) &
#             share_df['trajectory'].isin(trajectories) &
#             share_df['well_depth'].isin(well_depths)
#         ]
#
#         current_df = filtered_df[filtered_df['date'] == date]
#         reference_df = filtered_df[filtered_df['date'] == reference_date]
#
#         scatter_df = filtered_df[['date', 'rig_count']].groupby('date').sum().reset_index()
#
#         # county_scatter_df = filtered_df[['date', 'county']].groupby(['date'])['county'].nunique().reset_index()
#
#
#         indicator_data = [
#             go.Indicator(
#                 mode='number+delta',
#                 value=current_df['rig_count'].sum(),
#                 delta={'reference': reference_df['rig_count'].sum()},
#             ),
#             go.Scatter(
#                 name='5-YEAR TREND',
#                 x=scatter_df['date'].tolist(),
#                 y=scatter_df['rig_count'].tolist()
#             )
#         ]
#
#         indicator_layout = go.Layout(
#             # title='COGS',
#             # height=100,
#             title_text='RIG COUNT AND TRENDS FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             height=177
#         )
#
#         indicator_fig = go.Figure(data=indicator_data, layout=indicator_layout)
#
#
#         s = open('/Users/brettdavis/Downloads/us_states.json')
#         p = open('/Users/brettdavis/Downloads/canada_provinces.json')
#
#         states = json.load(s)
#         provinces = json.load(p)
#
#         states_and_provinces = {"type": "FeatureCollection", "features": states['features'] + provinces['features']}
#
#         for feature in states_and_provinces['features']:
#             feature['id'] = feature['properties']['name'].upper()
#
#         selected_week_df_raw = current_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index()
#
#         selected_week_df = selected_week_df_raw.rename(columns={'rig_count': 'rig_count_select'})
#
#         ref_week_df_raw = reference_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index()
#
#         ref_week_df = ref_week_df_raw.rename(columns={'rig_count': 'rig_count_ref'})
#
#         map_df = selected_week_df.merge(ref_week_df, 'outer', ['state'])
#
#         map_df['rig_count_ref'] = map_df['rig_count_ref'].fillna(0)
#         map_df['rig_count_select'] = map_df['rig_count_select'].fillna(0)
#
#         map_df['rig_count_ref'] = map_df['rig_count_ref'].astype(int)
#         map_df['rig_count_select'] = map_df['rig_count_select'].astype(int)
#
#         map_df['difference'] = map_df['rig_count_select'] - map_df['rig_count_ref']
#
#         # map_df = current_df[[
#         #     'state', 'rig_count'
#         # ]].groupby(['state']).sum().reset_index()
#
#         map_data = go.Choropleth(
#             name='States & Provinces',
#             geojson=states_and_provinces,
#             locations=map_df['state'],
#             z=map_df['difference'],
#             zmid=0,
#             colorscale=plus_minus_colorscale,
#             hovertemplate=map_df['state'] + '<br>Rig +/-: %{z}<br>Rig Count: ' + map_df['rig_count_select'].astype(str)
#         )
#
#         map_layout = go.Layout(
#             geo={
#                 'scope': 'north america',
#                 'showlakes': True,
#                 'fitbounds': 'locations'
#             },
#             title_text='STATE/PROVINCE-LEVEL 3-YEAR +/- HEAT MAP FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
#             titlefont={
#                 'size': 8
#             },
#             margin={
#                 'r': 0,
#                 't': 20,
#                 'l': 0,
#                 'b': 0
#             },
#             template="plotly_dark",
#             height=500
#         )
#
#         map_fig = go.Figure(data=map_data, layout=map_layout)
#
#         totals_df_raw = filtered_share_df[['date', 'rig_count']].groupby('date').sum().reset_index()
#         totals_df = totals_df_raw.rename(columns={'rig_count': 'overall_weekly_total'})
#
#         drill_for_df = filtered_share_df[[
#             'date',
#             'drill_for',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'drill_for'
#         ]).sum().reset_index()
#
#         drill_for_totals_df = drill_for_df.merge(totals_df, how='left', on='date')
#
#         drill_for_totals_df['share'] = (
#                     (drill_for_totals_df['rig_count']) / (drill_for_totals_df['overall_weekly_total']))
#
#         drill_for_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['date'],
#                 y=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in drill_for_totals_df['drill_for'].unique()
#         ]
#
#         drill_for_layout = go.Layout(
#             title_text='5Y DRILL-FOR HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         drill_for_fig = go.Figure(data=drill_for_data, layout=drill_for_layout)
#
#         well_depth_df = filtered_share_df[[
#             'date',
#             'well_depth',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'well_depth'
#         ]).sum().reset_index()
#
#         well_depth_totals_df = well_depth_df.merge(totals_df, how='left', on='date')
#
#         well_depth_totals_df['share'] = (
#                 (well_depth_totals_df['rig_count']) / (well_depth_totals_df['overall_weekly_total'])
#         )
#
#         well_depth_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['date'],
#                 y=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in well_depth_totals_df['well_depth'].unique()
#         ]
#
#         well_depth_layout = go.Layout(
#             title_text='5Y WELL-DEPTH HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         well_depth_fig = go.Figure(data=well_depth_data, layout=well_depth_layout)
#
#         trajectory_df = filtered_share_df[[
#             'date',
#             'trajectory',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'trajectory'
#         ]).sum().reset_index()
#
#         trajectory_totals_df = trajectory_df.merge(totals_df, how='left', on='date')
#
#         trajectory_totals_df['share'] = (
#                 (trajectory_totals_df['rig_count']) / (trajectory_totals_df['overall_weekly_total']))
#
#         trajectory_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['date'],
#                 y=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in trajectory_totals_df['trajectory'].unique()
#         ]
#
#         trajectory_layout = go.Layout(
#             title_text='5Y TRAJECTORY HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         trajectory_fig = go.Figure(data=trajectory_data, layout=trajectory_layout)
#
#         location_df = filtered_share_df[[
#             'date',
#             'location',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'location'
#         ]).sum().reset_index()
#
#         location_totals_df = location_df.merge(totals_df, how='left', on='date')
#
#         location_totals_df['share'] = (
#                 (location_totals_df['rig_count']) / (location_totals_df['overall_weekly_total']))
#
#         location_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=location_totals_df[location_totals_df['location'] == i]['date'],
#                 y=location_totals_df[location_totals_df['location'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in location_totals_df['location'].unique()
#         ]
#
#         location_layout = go.Layout(
#             title_text='5Y LOCATION HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         location_fig = go.Figure(data=location_data, layout=location_layout)
#
#
#         state_table_df_raw = current_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})
#
#         state_table_df_ref_raw = reference_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})
#
#         state_table_df = state_table_df_raw.merge(
#             state_table_df_ref_raw,
#             'outer',
#             ['state']
#         )
#
#         state_table_df['rig_count_after'] = state_table_df['rig_count_after'].fillna(0)
#         state_table_df['rig_count_before'] = state_table_df['rig_count_before'].fillna(0)
#
#         state_table_df['rig_count_after'] = state_table_df['rig_count_after'].astype(int)
#         state_table_df['rig_count_before'] = state_table_df['rig_count_before'].astype(int)
#
#         state_table_df['difference'] = state_table_df['rig_count_after'] - state_table_df['rig_count_before']
#
#         state_table_df['rank'] = state_table_df['difference'].rank(method='min', ascending=False)
#
#         state_table_df_sort = state_table_df.sort_values(
#             by=['difference', 'rig_count_after'],
#             ascending=[False, False]
#         )
#
#         state_final_table_df = pd.DataFrame({
#             'RANK': [int(x) for x in state_table_df_sort['rank'].tolist()],
#             'STATE/PROVINCE': state_table_df_sort['state'].tolist(),
#             'RIGS': state_table_df_sort['rig_count_after'].tolist(),
#             '+/-': state_table_df_sort['difference'].tolist()
#         })
#
#         state_table_columns = [{
#             'name': i, 'id': i
#         } for i in state_final_table_df.columns]
#
#         state_table_data = state_final_table_df.to_dict('records')
#
#         country_table_df_raw = current_df[[
#             'country', 'rig_count'
#         ]].groupby(['country']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})
#
#         country_table_df_ref_raw = reference_df[[
#             'country', 'rig_count'
#         ]].groupby(['country']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})
#
#         country_table_df = country_table_df_raw.merge(
#             country_table_df_ref_raw,
#             'outer',
#             ['country']
#         )
#
#         country_table_df['rig_count_after'] = country_table_df['rig_count_after'].fillna(0)
#         country_table_df['rig_count_before'] = country_table_df['rig_count_before'].fillna(0)
#
#         country_table_df['rig_count_after'] = country_table_df['rig_count_after'].astype(int)
#         country_table_df['rig_count_before'] = country_table_df['rig_count_before'].astype(int)
#
#         country_table_df['difference'] = country_table_df['rig_count_after'] - country_table_df['rig_count_before']
#
#         country_table_df['rank'] = country_table_df['difference'].rank(method='min', ascending=False)
#
#         country_table_df_sort = country_table_df.sort_values(
#             by=['difference', 'rig_count_after'],
#             ascending=[False, False]
#         )
#
#         country_final_table_df = pd.DataFrame({
#             'RANK': [int(x) for x in country_table_df_sort['rank'].tolist()],
#             'COUNTRY': country_table_df_sort['country'].tolist(),
#             'RIGS': country_table_df_sort['rig_count_after'].tolist(),
#             '+/-': country_table_df_sort['difference'].tolist()
#         })
#
#         country_table_columns = [{
#             'name': i, 'id': i
#         } for i in country_final_table_df.columns]
#
#         country_table_data = country_final_table_df.to_dict('records')
#
#
#         return indicator_fig, map_fig, drill_for_fig, well_depth_fig, trajectory_fig, \
#             location_fig, state_table_columns, state_table_data, country_table_columns, country_table_data, \
#
#
#     elif dropdown_value == '3y':
#         reference_date = three_year_date
#         scatter_reference_date = reference_date
#
#         df = functions.get_north_america_df(scatter_reference_date, date)
#
#         share_df = functions.get_df(reference_date, date)
#
#         filtered_df = df[
#             df['country'].isin(countries) &
#             df['state'].isin(states) &
#             df['basin'].isin(basins) &
#             df['drill_for'].isin(drill_for) &
#             df['location'].isin(locations) &
#             df['trajectory'].isin(trajectories) &
#             df['well_depth'].isin(well_depths)
#         ]
#
#         filtered_share_df = share_df[
#             share_df['state'].isin(states) &
#             share_df['basin'].isin(basins) &
#             share_df['drill_for'].isin(drill_for) &
#             share_df['location'].isin(locations) &
#             share_df['trajectory'].isin(trajectories) &
#             share_df['well_depth'].isin(well_depths)
#         ]
#
#         current_df = filtered_df[filtered_df['date'] == date]
#         reference_df = filtered_df[filtered_df['date'] == reference_date]
#
#         scatter_df = filtered_df[['date', 'rig_count']].groupby('date').sum().reset_index()
#
#         # county_scatter_df = filtered_df[['date', 'county']].groupby(['date'])['county'].nunique().reset_index()
#
#
#         indicator_data = [
#             go.Indicator(
#                 mode='number+delta',
#                 value=current_df['rig_count'].sum(),
#                 delta={'reference': reference_df['rig_count'].sum()},
#             ),
#             go.Scatter(
#                 name='3-YEAR TREND',
#                 x=scatter_df['date'].tolist(),
#                 y=scatter_df['rig_count'].tolist()
#             )
#         ]
#
#         indicator_layout = go.Layout(
#             # title='COGS',
#             # height=100,
#             title_text='RIG COUNT AND TRENDS FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             height=177
#         )
#
#         indicator_fig = go.Figure(data=indicator_data, layout=indicator_layout)
#
#
#         s = open('/Users/brettdavis/Downloads/us_states.json')
#         p = open('/Users/brettdavis/Downloads/canada_provinces.json')
#
#         states = json.load(s)
#         provinces = json.load(p)
#
#         states_and_provinces = {"type": "FeatureCollection", "features": states['features'] + provinces['features']}
#
#         for feature in states_and_provinces['features']:
#             feature['id'] = feature['properties']['name'].upper()
#
#         selected_week_df_raw = current_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index()
#
#         selected_week_df = selected_week_df_raw.rename(columns={'rig_count': 'rig_count_select'})
#
#         ref_week_df_raw = reference_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index()
#
#         ref_week_df = ref_week_df_raw.rename(columns={'rig_count': 'rig_count_ref'})
#
#         map_df = selected_week_df.merge(ref_week_df, 'outer', ['state'])
#
#         map_df['rig_count_ref'] = map_df['rig_count_ref'].fillna(0)
#         map_df['rig_count_select'] = map_df['rig_count_select'].fillna(0)
#
#         map_df['rig_count_ref'] = map_df['rig_count_ref'].astype(int)
#         map_df['rig_count_select'] = map_df['rig_count_select'].astype(int)
#
#         map_df['difference'] = map_df['rig_count_select'] - map_df['rig_count_ref']
#
#         # map_df = current_df[[
#         #     'state', 'rig_count'
#         # ]].groupby(['state']).sum().reset_index()
#
#         map_data = go.Choropleth(
#             name='States & Provinces',
#             geojson=states_and_provinces,
#             locations=map_df['state'],
#             z=map_df['difference'],
#             zmid=0,
#             colorscale=plus_minus_colorscale,
#             hovertemplate=map_df['state'] + '<br>Rig +/-: %{z}<br>Rig Count: ' + map_df['rig_count_select'].astype(str)
#         )
#
#         map_layout = go.Layout(
#             geo={
#                 'scope': 'north america',
#                 'showlakes': True,
#                 'fitbounds': 'locations'
#             },
#             title_text='STATE/PROVINCE-LEVEL 3-YEAR +/- HEAT MAP FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
#             titlefont={
#                 'size': 8
#             },
#             margin={
#                 'r': 0,
#                 't': 20,
#                 'l': 0,
#                 'b': 0
#             },
#             template="plotly_dark",
#             height=500
#         )
#
#         map_fig = go.Figure(data=map_data, layout=map_layout)
#
#         totals_df_raw = filtered_share_df[['date', 'rig_count']].groupby('date').sum().reset_index()
#         totals_df = totals_df_raw.rename(columns={'rig_count': 'overall_weekly_total'})
#
#         drill_for_df = filtered_share_df[[
#             'date',
#             'drill_for',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'drill_for'
#         ]).sum().reset_index()
#
#         drill_for_totals_df = drill_for_df.merge(totals_df, how='left', on='date')
#
#         drill_for_totals_df['share'] = (
#                     (drill_for_totals_df['rig_count']) / (drill_for_totals_df['overall_weekly_total']))
#
#         drill_for_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['date'],
#                 y=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in drill_for_totals_df['drill_for'].unique()
#         ]
#
#         drill_for_layout = go.Layout(
#             title_text='3Y DRILL-FOR HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         drill_for_fig = go.Figure(data=drill_for_data, layout=drill_for_layout)
#
#         well_depth_df = filtered_share_df[[
#             'date',
#             'well_depth',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'well_depth'
#         ]).sum().reset_index()
#
#         well_depth_totals_df = well_depth_df.merge(totals_df, how='left', on='date')
#
#         well_depth_totals_df['share'] = (
#                 (well_depth_totals_df['rig_count']) / (well_depth_totals_df['overall_weekly_total'])
#         )
#
#         well_depth_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['date'],
#                 y=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in well_depth_totals_df['well_depth'].unique()
#         ]
#
#         well_depth_layout = go.Layout(
#             title_text='3Y WELL-DEPTH HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         well_depth_fig = go.Figure(data=well_depth_data, layout=well_depth_layout)
#
#         trajectory_df = filtered_share_df[[
#             'date',
#             'trajectory',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'trajectory'
#         ]).sum().reset_index()
#
#         trajectory_totals_df = trajectory_df.merge(totals_df, how='left', on='date')
#
#         trajectory_totals_df['share'] = (
#                 (trajectory_totals_df['rig_count']) / (trajectory_totals_df['overall_weekly_total']))
#
#         trajectory_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['date'],
#                 y=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in trajectory_totals_df['trajectory'].unique()
#         ]
#
#         trajectory_layout = go.Layout(
#             title_text='3Y TRAJECTORY HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         trajectory_fig = go.Figure(data=trajectory_data, layout=trajectory_layout)
#
#         location_df = filtered_share_df[[
#             'date',
#             'location',
#             'rig_count'
#         ]].groupby([
#             'date',
#             'location'
#         ]).sum().reset_index()
#
#         location_totals_df = location_df.merge(totals_df, how='left', on='date')
#
#         location_totals_df['share'] = (
#                 (location_totals_df['rig_count']) / (location_totals_df['overall_weekly_total']))
#
#         location_data = [
#             go.Scatter(
#                 name=i[:4],
#                 x=location_totals_df[location_totals_df['location'] == i]['date'],
#                 y=location_totals_df[location_totals_df['location'] == i]['share'],
#                 hovertemplate='%{x}<br>' + i + '<br>%{y}'
#             ) for i in location_totals_df['location'].unique()
#         ]
#
#         location_layout = go.Layout(
#             title_text='3Y LOCATION HISTORY',
#             titlefont={
#                 'size': 8
#             },
#             template="plotly_dark",
#             xaxis={
#                 'showgrid': False,
#                 'showticklabels': False
#             },
#             yaxis={
#                 'showgrid': False,
#                 'showticklabels': True,
#                 'tickformat': ',.0%',
#                 'tickfont': {
#                     'size': 8
#                 }
#             },
#             margin={
#                 't': 20,
#                 'r': 0,
#                 'b': 0,
#                 'l': 0
#             },
#             showlegend=False,
#         )
#
#         location_fig = go.Figure(data=location_data, layout=location_layout)
#
#
#         state_table_df_raw = current_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})
#
#         state_table_df_ref_raw = reference_df[[
#             'state', 'rig_count'
#         ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})
#
#         state_table_df = state_table_df_raw.merge(
#             state_table_df_ref_raw,
#             'outer',
#             ['state']
#         )
#
#         state_table_df['rig_count_after'] = state_table_df['rig_count_after'].fillna(0)
#         state_table_df['rig_count_before'] = state_table_df['rig_count_before'].fillna(0)
#
#         state_table_df['rig_count_after'] = state_table_df['rig_count_after'].astype(int)
#         state_table_df['rig_count_before'] = state_table_df['rig_count_before'].astype(int)
#
#         state_table_df['difference'] = state_table_df['rig_count_after'] - state_table_df['rig_count_before']
#
#         state_table_df['rank'] = state_table_df['difference'].rank(method='min', ascending=False)
#
#         state_table_df_sort = state_table_df.sort_values(
#             by=['difference', 'rig_count_after'],
#             ascending=[False, False]
#         )
#
#         state_final_table_df = pd.DataFrame({
#             'RANK': [int(x) for x in state_table_df_sort['rank'].tolist()],
#             'STATE/PROVINCE': state_table_df_sort['state'].tolist(),
#             'RIGS': state_table_df_sort['rig_count_after'].tolist(),
#             '+/-': state_table_df_sort['difference'].tolist()
#         })
#
#         state_table_columns = [{
#             'name': i, 'id': i
#         } for i in state_final_table_df.columns]
#
#         state_table_data = state_final_table_df.to_dict('records')
#
#         country_table_df_raw = current_df[[
#             'country', 'rig_count'
#         ]].groupby(['country']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})
#
#         country_table_df_ref_raw = reference_df[[
#             'country', 'rig_count'
#         ]].groupby(['country']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})
#
#         country_table_df = country_table_df_raw.merge(
#             country_table_df_ref_raw,
#             'outer',
#             ['country']
#         )
#
#         country_table_df['rig_count_after'] = country_table_df['rig_count_after'].fillna(0)
#         country_table_df['rig_count_before'] = country_table_df['rig_count_before'].fillna(0)
#
#         country_table_df['rig_count_after'] = country_table_df['rig_count_after'].astype(int)
#         country_table_df['rig_count_before'] = country_table_df['rig_count_before'].astype(int)
#
#         country_table_df['difference'] = country_table_df['rig_count_after'] - country_table_df['rig_count_before']
#
#         country_table_df['rank'] = country_table_df['difference'].rank(method='min', ascending=False)
#
#         country_table_df_sort = country_table_df.sort_values(
#             by=['difference', 'rig_count_after'],
#             ascending=[False, False]
#         )
#
#         country_final_table_df = pd.DataFrame({
#             'RANK': [int(x) for x in country_table_df_sort['rank'].tolist()],
#             'COUNTRY': country_table_df_sort['country'].tolist(),
#             'RIGS': country_table_df_sort['rig_count_after'].tolist(),
#             '+/-': country_table_df_sort['difference'].tolist()
#         })
#
#         country_table_columns = [{
#             'name': i, 'id': i
#         } for i in country_final_table_df.columns]
#
#         country_table_data = country_final_table_df.to_dict('records')
#
#
#         return indicator_fig, map_fig, drill_for_fig, well_depth_fig, trajectory_fig, \
#             location_fig, state_table_columns, state_table_data, country_table_columns, country_table_data, \
#
#
# # if __name__ == '__main__':
#     app.run_server(host='0.0.0.0', port=8050, debug=True)