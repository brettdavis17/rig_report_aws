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

layout = html.Div([
    #header
    html.Div([
        html.H2('USA LAND RIG DASHBOARD')
    ], className='header', style={'color': 'black'}
    ),
    #dropdowns
    html.Div([
        html.Div([
            dbc.Button(
                'SUBMIT',
                id='us-submit-button',
                style={
                    'backgroundColor': 'black',
                    'color': 'white'
                }
            ),
            dcc.Dropdown(
                id='us-date-dropdown',
                options=[{'label': x, 'value': x} for x in functions.get_date_list()],
                multi=False,
                value=functions.get_date_list()[0],
                placeholder='Select a date',
                persistence=True
            ),
            dcc.Dropdown(
                id='us-reference-dropdown',
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
                html.Summary('States'),
                html.Div([
                    dbc.Button(
                        'SELECT ALL',
                        id='us-state-select-all',
                        size='sm',
                        style={
                            'backgroundColor': 'black',
                            'color': 'white'
                        }
                    ),
                    dbc.Button(
                        'CLEAR ALL',
                        id='us-state-clear-all',
                        size='sm',
                        style={
                            'backgroundColor': 'black',
                            'color': 'white'
                        }
                    ),
                    dcc.Checklist(
                        id='us-state-checklist',
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
                        id='us-basin-select-all',
                        size='sm'
                    ),
                    dbc.Button(
                        'CLEAR ALL',
                        id='us-basin-clear-all',
                        size='sm'
                    ),
                    dcc.Checklist(
                        id='us-basin-checklist',
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
                        id='us-drill-for-select-all',
                        size='sm'
                    ),
                    dbc.Button(
                        'CLEAR ALL',
                        id='us-drill-for-clear-all',
                        size='sm'
                    ),
                    dcc.Checklist(
                        id='us-drill-for-checklist',
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
                        id='us-location-select-all',
                        size='sm'
                    ),
                    dbc.Button(
                        'CLEAR ALL',
                        id='us-location-clear-all',
                        size='sm'
                    ),
                    dcc.Checklist(
                        id='us-location-checklist',
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
                        id='us-trajectory-select-all',
                        size='sm'
                    ),
                    dbc.Button(
                        'CLEAR ALL',
                        id='us-trajectory-clear-all',
                        size='sm'
                    ),
                    dcc.Checklist(
                        id='us-trajectory-checklist',
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
                        id='us-well-depth-select-all',
                        size='sm'
                    ),
                    dbc.Button(
                        'CLEAR ALL',
                        id='us-well-depth-clear-all',
                        size='sm'
                    ),
                    dcc.Checklist(
                        id='us-well-depth-checklist',
                        options=[{'label': x, 'value': x} for x in functions.get_well_depth_list()],
                        value=functions.get_well_depth_list(),
                        persistence=True
                    )
                ])
            ])
        ], className='two columns'
        ),
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        dcc.Graph(
                            id='us-indicator',
                            config={
                                'displayModeBar': False
                            }
                        )
                    ], className='graph_container'
                    ),
                    html.Div([
                        dcc.Graph(
                            id='us-county-indicator',
                            config={
                                'displayModeBar': False
                            }
                        )
                    ], className='graph_container'
                    )
                ], className='three columns'
                ),
                html.Div([
                    html.Div([
                        html.Div([
                        ], className='nine columns'
                        )
                    ]),
                    html.Div([
                        dcc.Graph(
                            id='us-rig-map'
                        )
                    ], className='graph_container'
                    )
                ], className='seven columns'
                ),
                html.Div([
                    html.Div([
                        dcc.Graph(
                            id='us-drill-for',
                            config={
                                'displayModeBar': False
                            }
                        )
                    ], className='graph_container'
                    ),
                    html.Div([
                        dcc.Graph(
                            id='us-depth',
                            config={
                                'displayModeBar': False
                            }
                        )
                    ], className='graph_container'
                    ),
                    html.Div([
                        dcc.Graph(
                            id='us-trajectory',
                            config={
                                'displayModeBar': False
                            }
                        )
                    ], className='graph_container'
                    ),
                ], className='two columns'
                ),
            ], className='twelve columns'
            ),
            html.Div([
                html.Div([
                    dash_table.DataTable(
                        id='us-state-table',
                        style_data_conditional=[
                            {
                                'if': {'row_index': 'even'},
                                'textAlign': 'left',
                                'backgroundColor': '#686B6D',
                                'color': 'white'
                            },
                            {
                                'if': {'row_index': 'odd'},
                                'textAlign': 'left',
                                'backgroundColor': '#2C2D2E',
                                'color': 'white'
                            },
                            {
                                'if': {
                                    'filter_query': '{+/-} > 0',
                                    'column_id': '+/-'
                                },
                                'backgroundColor': 'green',
                                'color': 'white'
                            },
                            {
                                'if': {
                                    'filter_query': '{+/-} < 0',
                                    'column_id': '+/-'
                                },
                                'backgroundColor': 'red',
                                'color': 'white'
                            }
                        ],
                        style_header={
                            'backgroundColor': 'black',
                            'color': 'white',
                            'textAlign': 'left'
                        }
                    )
                ], className='graph_container four columns', style={'maxHeight': '300px', 'overflow': 'scroll'}
                ),
                html.Div([
                    dash_table.DataTable(
                        id='us-basin-table',
                        style_data_conditional=[
                            {
                                'if': {'row_index': 'even'},
                                'textAlign': 'left',
                                'backgroundColor': '#686B6D',
                                'color': 'white'
                            },
                            {
                                'if': {'row_index': 'odd'},
                                'textAlign': 'left',
                                'backgroundColor': '#2C2D2E',
                                'color': 'white'
                            },
                            {
                                'if': {
                                    'filter_query': '{+/-} > 0',
                                    'column_id': '+/-'
                                },
                                'backgroundColor': 'green',
                                'color': 'white'
                            },
                            {
                                'if': {
                                    'filter_query': '{+/-} < 0',
                                    'column_id': '+/-'
                                },
                                'backgroundColor': 'red',
                                'color': 'white'
                            }
                        ],
                        style_header={
                            'backgroundColor': 'black',
                            'color': 'white',
                            'textAlign': 'left'
                        }
                        # fixed_rows={
                        #     'headers': True,
                        #     'data': 0
                        # }
                    )
                ], className='graph_container four columns',
                    style={'maxHeight': '300px', 'overflow': 'scroll'}
                ),
                html.Div([
                    dash_table.DataTable(
                        id='us-county-table',
                        style_data_conditional=[
                            {
                                'if': {'row_index': 'even'},
                                'textAlign': 'left',
                                'backgroundColor': '#686B6D',
                                'color': 'white'
                            },
                            {
                                'if': {'row_index': 'odd'},
                                'textAlign': 'left',
                                'backgroundColor': '#2C2D2E',
                                'color': 'white'
                            },
                            {
                                'if': {
                                    'filter_query': '{+/-} > 0',
                                    'column_id': '+/-'
                                },
                                'backgroundColor': 'green',
                                'color': 'white'
                            },
                            {
                                'if': {
                                    'filter_query': '{+/-} < 0',
                                    'column_id': '+/-'
                                },
                                'backgroundColor': 'red',
                                'color': 'white'
                            }
                        ],
                        style_header={
                            'backgroundColor': 'black',
                            'color': 'white',
                            'textAlign': 'left'
                        },
                        style_cell={
                            'whiteSpace': 'normal',
                            'height': 'auto'
                        }
                    )
                ], className='graph_container four columns',
                    style={'maxHeight': '300px', 'overflow': 'scroll'}
                )
            ], className='twelve columns'
            ),
        ], className='ten columns'
        )
    ], className='twelve columns'
    )
]
)

    # convert_dict = {'date': str}
    # master_df = functions.get_overall_master_df().astype(convert_dict)

# layout = serve_layout

# convert_dict = {'date': str}
# master_df = functions.get_overall_master_df().astype(convert_dict)


@app.callback(
    Output(
        'us-state-checklist',
        'value'
    ),
    [
        Input(
            'us-state-select-all',
            'n_clicks'
        ),
        Input(
            'us-state-clear-all',
            'n_clicks'
        )
    ],
)
def return_states_checklist(select_all, clear_all):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'state-select-all' in changed_id:
        return functions.get_state_list()
    elif 'state-clear-all' in changed_id:
        return []
    else:
        return functions.get_state_list()

@app.callback(
    Output(
        'us-basin-checklist',
        'value'
    ),
    [
        Input(
            'us-basin-select-all',
            'n_clicks'
        ),
        Input(
            'us-basin-clear-all',
            'n_clicks'
        )
    ],
)
def return_basins_checklist(select_all, clear_all):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'basin-select-all' in changed_id:
        return functions.get_basin_list()
    elif 'basin-clear-all' in changed_id:
        return []
    else:
        return functions.get_basin_list()

@app.callback(
    Output(
        'us-drill-for-checklist',
        'value'
    ),
    [
        Input(
            'us-drill-for-select-all',
            'n_clicks'
        ),
        Input(
            'us-drill-for-clear-all',
            'n_clicks'
        )
    ],
)
def return_drill_for_checklist(select_all, clear_all):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'drill-for-select-all' in changed_id:
        return functions.get_drill_for_list()
    elif 'drill-for-clear-all' in changed_id:
        return []
    else:
        return functions.get_drill_for_list()

@app.callback(
    Output(
        'us-location-checklist',
        'value'
    ),
    [
        Input(
            'us-location-select-all',
            'n_clicks'
        ),
        Input(
            'us-location-clear-all',
            'n_clicks'
        )
    ],
)
def return_locations_checklist(select_all, clear_all):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'location-select-all' in changed_id:
        return functions.get_location_list()
    elif 'location-clear-all' in changed_id:
        return []
    else:
        return functions.get_location_list()

@app.callback(
    Output(
        'us-trajectory-checklist',
        'value'
    ),
    [
        Input(
            'us-trajectory-select-all',
            'n_clicks'
        ),
        Input(
            'us-trajectory-clear-all',
            'n_clicks'
        )
    ],
)
def return_trajectory_checklist(select_all, clear_all):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'trajectory-select-all' in changed_id:
        return functions.get_trajectory_list()
    elif 'trajectory-clear-all' in changed_id:
        return []
    else:
        return functions.get_trajectory_list()

@app.callback(
    Output(
        'us-well-depth-checklist',
        'value'
    ),
    [
        Input(
            'us-well-depth-select-all',
            'n_clicks'
        ),
        Input(
            'us-well-depth-clear-all',
            'n_clicks'
        )
    ],
)
def return_well_depth_checklist(select_all, clear_all):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'well-depth-select-all' in changed_id:
        return functions.get_well_depth_list()
    elif 'well-depth-clear-all' in changed_id:
        return []
    else:
        return functions.get_well_depth_list()


@app.callback(
    [
        Output(
            'us-indicator',
            'figure'
        ),
        Output(
            'us-county-indicator',
            'figure'
        ),
        Output(
            'us-rig-map',
            'figure'
        ),
        Output(
            'us-drill-for',
            'figure'
        ),
        Output(
            'us-depth',
            'figure'
        ),
        Output(
            'us-trajectory',
            'figure'
        ),
        Output(
            'us-state-table',
            'columns'
        ),
        Output(
            'us-state-table',
            'data'
        ),
        Output(
            'us-basin-table',
            'columns'
        ),
        Output(
            'us-basin-table',
            'data'
        ),
        Output(
            'us-county-table',
            'columns'
        ),
        Output(
            'us-county-table',
            'data'
        )
    ],
    [
        Input(
            'us-submit-button',
            'n_clicks'
        )
    ],
    [
        State(
            'us-date-dropdown',
            'value'
        ),
        State(
            'us-reference-dropdown',
            'value'
        ),
        State(
            'us-state-checklist',
            'value'
        ),
        State(
            'us-basin-checklist',
            'value'
        ),
        State(
            'us-drill-for-checklist',
            'value'
        ),
        State(
            'us-location-checklist',
            'value'
        ),
        State(
            'us-trajectory-checklist',
            'value'
        ),
        State(
            'us-well-depth-checklist',
            'value'
        )
    ]
)
def return_references(click, date, dropdown_value, states, basins, drill_for, locations, trajectories, well_depths):
    # current_df = master_df[master_df['date'] == date]  # unfiltered df for current week

    date_list = functions.get_date_list_asc()  # list of all unique dates

    one_week_date = date_list[date_list.index(date) - 1]  # date 1 week before selected date
    one_month_date = date_list[date_list.index(date) - 4]
    three_month_date = date_list[date_list.index(date) - 13]
    six_month_date = date_list[date_list.index(date) - 26]
    one_year_date = date_list[date_list.index(date) - 52]
    three_year_date = date_list[date_list.index(date) - 156]
    five_year_date = date_list[date_list.index(date) - 260]

    # filtered_df = current_df[
    #     current_df['state'].isin(states) &
    #     current_df['basin'].isin(basins) &
    #     current_df['drill_for'].isin(drill_for) &
    #     current_df['location'].isin(locations) &
    #     current_df['trajectory'].isin(trajectories) &
    #     current_df['well_depth'].isin(well_depths)
    #     ]  # filtered df for current week

    # filtered_overall_master_df = master_df[
    #     master_df['state'].isin(states) &
    #     master_df['basin'].isin(basins) &
    #     master_df['drill_for'].isin(drill_for) &
    #     master_df['location'].isin(locations) &
    #     master_df['trajectory'].isin(trajectories) &
    #     master_df['well_depth'].isin(well_depths)
    #     ]  # filtered master df

    plus_minus_colorscale = [
        '#660000', '#800000', '#990000', '#b30000', '#cc0000', '#e60000',
        '#ff0000', '#ff1a1a', '#ff3333', '#ff4d4d', '#ff6666', '#ff8080',
        '#ff9999', '#ffffff', '#99ffbb', '#80ffaa', '#66ff99', '#4dff88',
        '#33ff77', '#1aff66', '#00ff55', '#00e64d', '#00cc44', '#00b33c',
        '#009933', '#00802b', '#006622']

    if dropdown_value == 'rig_count_view':
        reference_date = one_week_date
        scatter_reference_date = one_year_date

        df = functions.get_df(scatter_reference_date, date)


        filtered_df = df[
            df['state'].isin(states) &
            df['basin'].isin(basins) &
            df['drill_for'].isin(drill_for) &
            df['location'].isin(locations) &
            df['trajectory'].isin(trajectories) &
            df['well_depth'].isin(well_depths)
        ]

        current_df = filtered_df[filtered_df['date'] == date]
        reference_df = filtered_df[filtered_df['date'] == reference_date]

        scatter_df = filtered_df[['date', 'rig_count']].groupby('date').sum().reset_index()

        county_scatter_df = filtered_df[['date', 'county']].groupby(['date'])['county'].nunique().reset_index()


        indicator_data = [
            go.Indicator(
                mode='number+delta',
                value=current_df['rig_count'].sum(),
                delta={'reference': reference_df['rig_count'].sum()},
            ),
            go.Scatter(
                name='1-YEAR TREND',
                x=scatter_df['date'].tolist(),
                y=scatter_df['rig_count'].tolist()
            )
        ]

        indicator_layout = go.Layout(
            # title='COGS',
            # height=100,
            title_text='RIG COUNT AND TRENDS FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': False
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            height=177
        )

        indicator_fig = go.Figure(data=indicator_data, layout=indicator_layout)

        county_indicator_data = [
            go.Indicator(
                mode='number+delta',
                value=current_df['county'].nunique(),
                delta={'reference': reference_df['county'].nunique()},
            ),
            go.Scatter(
                name='1-YEAR TREND',
                x=county_scatter_df['date'].tolist(),
                y=county_scatter_df['county'].tolist()
            )
        ]

        county_indicator_layout = go.Layout(
                # title='COGS',
                # height=100,
                title_text='COUNTY COUNT AND TRENDS FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
                titlefont={
                    'size': 8
                },
                template="plotly_dark",
                xaxis={
                    'showgrid': False,
                    'showticklabels': False
                },
                yaxis={
                    'showgrid': False,
                    'showticklabels': False
                },
                margin={
                    't': 20,
                    'r': 0,
                    'b': 0,
                    'l': 0
                },
                height=177
            )

        county_indicator_fig = go.Figure(data=county_indicator_data, layout=county_indicator_layout)

        with urlopen(
                'https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json'
        ) as response:
            counties = json.load(response)

        map_df = current_df[[
            'fips', 'county', 'rig_count'
        ]].groupby(['fips', 'county']).sum().reset_index()

        map_data = go.Choropleth(
            name='Counties',
            geojson=counties,
            locations=map_df['fips'],
            z=map_df['rig_count'],
            colorscale='Oranges',
            hovertemplate=map_df['county'] + '<br>Rigs: %{z}'
        )

        map_layout = go.Layout(
            geo={
                'scope': 'usa',
                'showlakes': True
            },
            title_text='COUNTY-LEVEL HEAT MAP FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            titlefont={
                'size': 8
            },
            margin={
                'r': 0,
                't': 20,
                'l': 0,
                'b': 0
            },
            template="plotly_dark",
            height=354
        )

        map_fig = go.Figure(data=map_data, layout=map_layout)

        drill_for_df = current_df[[
            'drill_for',
            'rig_count'
        ]].groupby('drill_for').sum().reset_index()

        drill_for_pie_data = [
            go.Pie(
                labels=drill_for_df['drill_for'].tolist(),
                values=drill_for_df['rig_count'].tolist(),
                textposition='inside',
                textinfo='label+percent',
                textfont={
                    'size': 8
                }
            )
        ]

        drill_for_pie_layout = go.Layout(
                title_text='DRILL-FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
                titlefont={
                    'size': 8
                },
                template="plotly_dark",
                showlegend=False,
                height=118,
                margin={
                    'r': 0,
                    't': 20,
                    'l': 0,
                    'b': 0
                },
            )

        drill_for_fig = go.Figure(data=drill_for_pie_data, layout = drill_for_pie_layout)

        well_depth_df = current_df[[
            'well_depth', 'rig_count'
        ]].groupby('well_depth').sum().reset_index()

        well_depth_data = [
            go.Pie(
                labels=well_depth_df['well_depth'].tolist(),
                values=well_depth_df['rig_count'].tolist(),
                textposition='inside',
                textinfo='label+percent',
                textfont={
                    'size': 8
                }
            )
        ]

        well_depth_layout = go.Layout(
            title_text='WELL-DEPTH ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            showlegend=False,
            height=118,
            margin={
                'r': 0,
                't': 20,
                'l': 0,
                'b': 0
            },
        )

        well_depth_fig = go.Figure(data=well_depth_data, layout=well_depth_layout)

        trajectory_df = current_df[[
            'trajectory', 'rig_count'
        ]].groupby('trajectory').sum().reset_index()

        trajectory_data = [
            go.Pie(
                labels=trajectory_df['trajectory'].tolist(),
                values=trajectory_df['rig_count'].tolist(),
                textposition='inside',
                textinfo='label+percent',
                textfont={
                    'size': 8
                }
            )
        ]

        trajectory_layout = go.Layout(
            title_text='TRAJECTORY ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            showlegend=False,
            height=118,
            margin={
                'r': 0,
                't': 20,
                'l': 0,
                'b': 0
            },
        )

        trajectory_fig = go.Figure(data=trajectory_data, layout=trajectory_layout)

        state_table_df_raw = current_df[[
            'state', 'rig_count'
        ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})

        state_table_df_ref_raw = reference_df[[
            'state', 'rig_count'
        ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})

        state_table_df = state_table_df_raw.merge(
            state_table_df_ref_raw,
            'outer',
            ['state']
        )

        state_table_df['rig_count_after'] = state_table_df['rig_count_after'].fillna(0)
        state_table_df['rig_count_before'] = state_table_df['rig_count_before'].fillna(0)

        state_table_df['rig_count_after'] = state_table_df['rig_count_after'].astype(int)
        state_table_df['rig_count_before'] = state_table_df['rig_count_before'].astype(int)

        state_table_df['difference'] = state_table_df['rig_count_after'] - state_table_df['rig_count_before']

        state_table_df['rank'] = state_table_df['rig_count_after'].rank(method='min', ascending=False)

        state_table_df_sort = state_table_df.sort_values(
            by=['rig_count_after', 'difference'],
            ascending=[False, False]
        )

        state_final_table_df = pd.DataFrame({
            'RANK': [int(x) for x in state_table_df_sort['rank'].tolist()],
            'STATE': state_table_df_sort['state'].tolist(),
            'RIGS': state_table_df_sort['rig_count_after'].tolist(),
            '+/-': state_table_df_sort['difference'].tolist()
        })

        state_table_columns = [{
            'name': i, 'id': i
        } for i in state_final_table_df.columns]

        state_table_data = state_final_table_df.to_dict('records')

        basin_table_df_raw = current_df[[
            'basin', 'rig_count'
        ]].groupby(['basin']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})

        basin_table_df_ref_raw = reference_df[[
            'basin', 'rig_count'
        ]].groupby(['basin']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})

        basin_table_df = basin_table_df_raw.merge(
            basin_table_df_ref_raw,
            'outer',
            ['basin']
        )

        basin_table_df['rig_count_after'] = basin_table_df['rig_count_after'].fillna(0)
        basin_table_df['rig_count_before'] = basin_table_df['rig_count_before'].fillna(0)

        basin_table_df['rig_count_after'] = basin_table_df['rig_count_after'].astype(int)
        basin_table_df['rig_count_before'] = basin_table_df['rig_count_before'].astype(int)

        basin_table_df['difference'] = basin_table_df['rig_count_after'] - basin_table_df['rig_count_before']

        basin_table_df['rank'] = basin_table_df['rig_count_after'].rank(method='min', ascending=False)

        basin_table_df_sort = basin_table_df.sort_values(
            by=['rig_count_after', 'difference'],
            ascending=[False, False]
        )

        basin_final_table_df = pd.DataFrame({
            'RANK': [int(x) for x in basin_table_df_sort['rank'].tolist()],
            'BASIN': basin_table_df_sort['basin'].tolist(),
            'RIGS': basin_table_df_sort['rig_count_after'].tolist(),
            '+/-': basin_table_df_sort['difference'].tolist()
        })

        basin_table_columns = [{
            'name': i, 'id': i
        } for i in basin_final_table_df.columns]

        basin_table_data = basin_final_table_df.to_dict('records')

        county_table_df_raw = current_df[[
            'county', 'rig_count'
        ]].groupby(['county']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})

        county_table_df_ref_raw = reference_df[[
            'county', 'rig_count'
        ]].groupby(['county']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})

        county_table_df = county_table_df_raw.merge(
            county_table_df_ref_raw,
            'outer',
            ['county']
        )

        county_table_df['rig_count_after'] = county_table_df['rig_count_after'].fillna(0)
        county_table_df['rig_count_before'] = county_table_df['rig_count_before'].fillna(0)

        county_table_df['rig_count_after'] = county_table_df['rig_count_after'].astype(int)
        county_table_df['rig_count_before'] = county_table_df['rig_count_before'].astype(int)

        county_table_df['difference'] = county_table_df['rig_count_after'] - county_table_df['rig_count_before']

        county_table_df['rank'] = county_table_df['rig_count_after'].rank(method='min', ascending=False)

        county_table_df_sort = county_table_df.sort_values(
            by=['rig_count_after', 'difference'],
            ascending=[False, False]
        )

        county_final_table_df = pd.DataFrame({
            'RANK': [int(x) for x in county_table_df_sort['rank'].tolist()],
            'COUNTY': county_table_df_sort['county'].tolist(),
            'RIGS': county_table_df_sort['rig_count_after'].tolist(),
            '+/-': county_table_df_sort['difference'].tolist()
        })

        county_table_columns = [{
            'name': i, 'id': i
        } for i in county_final_table_df.columns]

        county_table_data = county_final_table_df.to_dict('records')

        return indicator_fig, county_indicator_fig, map_fig, drill_for_fig, well_depth_fig, trajectory_fig, \
            state_table_columns, state_table_data, basin_table_columns, basin_table_data, \
            county_table_columns, county_table_data


    elif dropdown_value == '1w':
        reference_date = one_week_date
        scatter_reference_date = one_year_date

        df = functions.get_df(scatter_reference_date, date)

        share_df = functions.get_df(reference_date, date)

        filtered_df = df[
            df['state'].isin(states) &
            df['basin'].isin(basins) &
            df['drill_for'].isin(drill_for) &
            df['location'].isin(locations) &
            df['trajectory'].isin(trajectories) &
            df['well_depth'].isin(well_depths)
        ]

        filtered_share_df = share_df[
            share_df['state'].isin(states) &
            share_df['basin'].isin(basins) &
            share_df['drill_for'].isin(drill_for) &
            share_df['location'].isin(locations) &
            share_df['trajectory'].isin(trajectories) &
            share_df['well_depth'].isin(well_depths)
        ]

        current_df = filtered_df[filtered_df['date'] == date]
        reference_df = filtered_df[filtered_df['date'] == reference_date]

        scatter_df = filtered_df[['date', 'rig_count']].groupby('date').sum().reset_index()

        county_scatter_df = filtered_df[['date', 'county']].groupby(['date'])['county'].nunique().reset_index()


        indicator_data = [
            go.Indicator(
                mode='number+delta',
                value=current_df['rig_count'].sum(),
                delta={'reference': reference_df['rig_count'].sum()},
            ),
            go.Scatter(
                name='1-YEAR TREND',
                x=scatter_df['date'].tolist(),
                y=scatter_df['rig_count'].tolist()
            )
        ]

        indicator_layout = go.Layout(
            title_text='RIG COUNT AND TRENDS FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': False
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            height=177
        )

        indicator_fig = go.Figure(data=indicator_data, layout=indicator_layout)

        county_indicator_data = [
            go.Indicator(
                mode='number+delta',
                value=current_df['county'].nunique(),
                delta={'reference': reference_df['county'].nunique()},
            ),
            go.Scatter(
                name='1-YEAR TREND',
                x=county_scatter_df['date'].tolist(),
                y=county_scatter_df['county'].tolist()
            )
        ]

        county_indicator_layout = go.Layout(
            # title='COGS',
            # height=100,
            title_text='COUNTY COUNT AND TRENDS FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': False
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            height=177
        )

        county_indicator_fig = go.Figure(data=county_indicator_data, layout=county_indicator_layout)

        with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
            counties = json.load(response)

        selected_week_df_raw = current_df[[
            'fips', 'county', 'rig_count'
        ]].groupby(['fips', 'county']).sum().reset_index()

        selected_week_df = selected_week_df_raw.rename(columns={'rig_count': 'rig_count_select'})

        ref_week_df_raw = reference_df[[
            'fips', 'county', 'rig_count'
        ]].groupby(['fips', 'county']).sum().reset_index()

        ref_week_df = ref_week_df_raw.rename(columns={'rig_count': 'rig_count_ref'})

        map_df = selected_week_df.merge(ref_week_df, 'outer', ['fips', 'county'])

        map_df['rig_count_ref'] = map_df['rig_count_ref'].fillna(0)
        map_df['rig_count_select'] = map_df['rig_count_select'].fillna(0)

        map_df['rig_count_ref'] = map_df['rig_count_ref'].astype(int)
        map_df['rig_count_select'] = map_df['rig_count_select'].astype(int)

        map_df['difference'] = map_df['rig_count_select'] - map_df['rig_count_ref']


        map_data = go.Choropleth(
            name='Counties',
            geojson=counties,
            locations=map_df['fips'],
            z=map_df['difference'],
            zmid=0,
            colorscale=plus_minus_colorscale,
            hovertemplate=map_df['county'] + '<br>Rig +/-: %{z}<br>Rig Count: ' + map_df['rig_count_select'].astype(str)
        )

        map_layout = go.Layout(
            geo={
                'scope': 'usa',
                'showlakes': True
            },
            title_text='COUNTY-LEVEL 1-WEEK +/- HEAT MAP FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            titlefont={
                'size': 8
            },
            margin={
                'r': 0,
                't': 20,
                'l': 0,
                'b': 0
            },
            template="plotly_dark",
            height=354
        )

        map_fig = go.Figure(data=map_data, layout=map_layout)

        totals_df_raw = filtered_share_df[['date', 'rig_count']].groupby('date').sum().reset_index()
        totals_df = totals_df_raw.rename(columns={'rig_count': 'overall_weekly_total'})


        drill_for_df = filtered_share_df[[
            'date',
            'drill_for',
            'rig_count'
        ]].groupby([
            'date',
            'drill_for'
        ]).sum().reset_index()

        drill_for_totals_df = drill_for_df.merge(totals_df, how='left', on='date')

        drill_for_totals_df['share'] = ((drill_for_totals_df['rig_count']) / (drill_for_totals_df['overall_weekly_total']))

        drill_for_data = [
            go.Scatter(
                name=i[:4],
                x=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['date'],
                y=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['share'],
                hovertemplate='%{x}<br>' + i + '<br>%{y}'
            ) for i in drill_for_totals_df['drill_for'].unique()
        ]

        drill_for_layout = go.Layout(
            title_text='1W DRILL-FOR HISTORY',
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': True,
                'tickformat': ',.0%',
                'tickfont': {
                    'size': 8
                }
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            showlegend=False,
        )

        drill_for_fig = go.Figure(data=drill_for_data, layout=drill_for_layout)


        well_depth_df = filtered_share_df[[
            'date',
            'well_depth',
            'rig_count'
        ]].groupby([
            'date',
            'well_depth'
        ]).sum().reset_index()

        well_depth_totals_df = well_depth_df.merge(totals_df, how='left', on='date')

        well_depth_totals_df['share'] = (
            (well_depth_totals_df['rig_count']) / (well_depth_totals_df['overall_weekly_total'])
        )

        well_depth_data = [
            go.Scatter(
                name=i[:4],
                x=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['date'],
                y=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['share'],
                hovertemplate='%{x}<br>' + i + '<br>%{y}'
            ) for i in well_depth_totals_df['well_depth'].unique()
        ]

        well_depth_layout = go.Layout(
            title_text='1W WELL-DEPTH HISTORY',
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': True,
                'tickformat': ',.0%',
                'tickfont': {
                    'size': 8
                }
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            showlegend=False,
        )

        well_depth_fig = go.Figure(data=well_depth_data, layout=well_depth_layout)

        trajectory_df = filtered_share_df[[
            'date',
            'trajectory',
            'rig_count'
        ]].groupby([
            'date',
            'trajectory'
        ]).sum().reset_index()

        trajectory_totals_df = trajectory_df.merge(totals_df, how='left', on='date')

        trajectory_totals_df['share'] = (
                    (trajectory_totals_df['rig_count']) / (trajectory_totals_df['overall_weekly_total']))

        trajectory_data = [
            go.Scatter(
                name=i[:4],
                x=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['date'],
                y=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['share'],
                hovertemplate='%{x}<br>' + i + '<br>%{y}'
            ) for i in trajectory_totals_df['trajectory'].unique()
        ]

        trajectory_layout = go.Layout(
            title_text='1W TRAJECTORY HISTORY',
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': True,
                'tickformat': ',.0%',
                'tickfont': {
                    'size': 8
                }
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            showlegend=False,
        )

        trajectory_fig = go.Figure(data=trajectory_data, layout=trajectory_layout)


        #### rankings by state section ######

        state_table_df_raw = current_df[[
            'state', 'rig_count'
        ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})

        state_table_df_ref_raw = reference_df[[
            'state', 'rig_count'
        ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})

        state_table_df = state_table_df_raw.merge(
            state_table_df_ref_raw,
            'outer',
            ['state']
        )

        state_table_df['rig_count_after'] = state_table_df['rig_count_after'].fillna(0)
        state_table_df['rig_count_before'] = state_table_df['rig_count_before'].fillna(0)

        state_table_df['rig_count_after'] = state_table_df['rig_count_after'].astype(int)
        state_table_df['rig_count_before'] = state_table_df['rig_count_before'].astype(int)

        state_table_df['difference'] = state_table_df['rig_count_after'] - state_table_df['rig_count_before']

        state_table_df['rank'] = state_table_df['difference'].rank(method='min', ascending=False)

        state_table_df_sort = state_table_df.sort_values(
            by=['difference', 'rig_count_after'],
            ascending=[False, False]
        )

        state_final_table_df = pd.DataFrame({
            'RANK': [int(x) for x in state_table_df_sort['rank'].tolist()],
            'STATE': state_table_df_sort['state'].tolist(),
            'RIGS': state_table_df_sort['rig_count_after'].tolist(),
            '+/-': state_table_df_sort['difference'].tolist()
        })

        state_table_columns = [{
            'name': i, 'id': i
        } for i in state_final_table_df.columns]

        state_table_data = state_final_table_df.to_dict('records')


        #### rankings by basin section ######

        basin_table_df_raw = current_df[[
            'basin', 'rig_count'
        ]].groupby(['basin']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})

        basin_table_df_ref_raw = reference_df[[
            'basin', 'rig_count'
        ]].groupby(['basin']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})

        basin_table_df = basin_table_df_raw.merge(
            basin_table_df_ref_raw,
            'outer',
            ['basin']
        )

        basin_table_df['rig_count_after'] = basin_table_df['rig_count_after'].fillna(0)
        basin_table_df['rig_count_before'] = basin_table_df['rig_count_before'].fillna(0)

        basin_table_df['rig_count_after'] = basin_table_df['rig_count_after'].astype(int)
        basin_table_df['rig_count_before'] = basin_table_df['rig_count_before'].astype(int)

        basin_table_df['difference'] = basin_table_df['rig_count_after'] - basin_table_df['rig_count_before']

        basin_table_df['rank'] = basin_table_df['difference'].rank(method='min', ascending=False)

        basin_table_df_sort = basin_table_df.sort_values(
            by=['difference', 'rig_count_after'],
            ascending=[False, False]
        )

        basin_final_table_df = pd.DataFrame({
            'RANK': [int(x) for x in basin_table_df_sort['rank'].tolist()],
            'BASIN': basin_table_df_sort['basin'].tolist(),
            'RIGS': basin_table_df_sort['rig_count_after'].tolist(),
            '+/-': basin_table_df_sort['difference'].tolist()
        })

        basin_table_columns = [{
            'name': i, 'id': i
        } for i in basin_final_table_df.columns]

        basin_table_data = basin_final_table_df.to_dict('records')


        #### rankings by county section ######

        county_table_df_raw = current_df[[
            'county', 'rig_count'
        ]].groupby(['county']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})

        county_table_df_ref_raw = reference_df[[
            'county', 'rig_count'
        ]].groupby(['county']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})

        county_table_df = county_table_df_raw.merge(
            county_table_df_ref_raw,
            'outer',
            ['county']
        )

        county_table_df['rig_count_after'] = county_table_df['rig_count_after'].fillna(0)
        county_table_df['rig_count_before'] = county_table_df['rig_count_before'].fillna(0)

        county_table_df['rig_count_after'] = county_table_df['rig_count_after'].astype(int)
        county_table_df['rig_count_before'] = county_table_df['rig_count_before'].astype(int)

        county_table_df['difference'] = county_table_df['rig_count_after'] - county_table_df['rig_count_before']

        county_table_df['rank'] = county_table_df['difference'].rank(method='min', ascending=False)

        county_table_df_sort = county_table_df.sort_values(
            by=['difference', 'rig_count_after'],
            ascending=[False, False]
        )

        county_final_table_df = pd.DataFrame({
            'RANK': [int(x) for x in county_table_df_sort['rank'].tolist()],
            'COUNTY': county_table_df_sort['county'].tolist(),
            'RIGS': county_table_df_sort['rig_count_after'].tolist(),
            '+/-': county_table_df_sort['difference'].tolist()
        })

        county_table_columns = [{
            'name': i, 'id': i
        } for i in county_final_table_df.columns]

        county_table_data = county_final_table_df.to_dict('records')


        return indicator_fig, county_indicator_fig, map_fig, \
            drill_for_fig, well_depth_fig, trajectory_fig, \
            state_table_columns, state_table_data, basin_table_columns, basin_table_data, \
            county_table_columns, county_table_data

    elif dropdown_value == '1m':
        reference_date = one_month_date
        scatter_reference_date = one_year_date

        df = functions.get_df(scatter_reference_date, date)

        share_df = functions.get_df(reference_date, date)

        filtered_df = df[
            df['state'].isin(states) &
            df['basin'].isin(basins) &
            df['drill_for'].isin(drill_for) &
            df['location'].isin(locations) &
            df['trajectory'].isin(trajectories) &
            df['well_depth'].isin(well_depths)
        ]

        filtered_share_df = share_df[
            share_df['state'].isin(states) &
            share_df['basin'].isin(basins) &
            share_df['drill_for'].isin(drill_for) &
            share_df['location'].isin(locations) &
            share_df['trajectory'].isin(trajectories) &
            share_df['well_depth'].isin(well_depths)
        ]


        current_df = filtered_df[filtered_df['date'] == date]
        reference_df = filtered_df[filtered_df['date'] == reference_date]

        scatter_df = filtered_df[['date', 'rig_count']].groupby('date').sum().reset_index()

        county_scatter_df = filtered_df[['date', 'county']].groupby(['date'])['county'].nunique().reset_index()

        indicator_data = [
            go.Indicator(
                mode='number+delta',
                value=current_df['rig_count'].sum(),
                delta={'reference': reference_df['rig_count'].sum()},
            ),
            go.Scatter(
                name='1-YEAR TREND',
                x=scatter_df['date'].tolist(),
                y=scatter_df['rig_count'].tolist()
            )
        ]

        indicator_layout = go.Layout(
            title_text='RIG COUNT AND TRENDS FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': False
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            height=177
        )

        indicator_fig = go.Figure(data=indicator_data, layout=indicator_layout)

        county_indicator_data = [
            go.Indicator(
                mode='number+delta',
                value=current_df['county'].nunique(),
                delta={'reference': reference_df['county'].nunique()},
            ),
            go.Scatter(
                name='1-YEAR TREND',
                x=county_scatter_df['date'].tolist(),
                y=county_scatter_df['county'].tolist()
            )
        ]

        county_indicator_layout = go.Layout(
            # title='COGS',
            # height=100,
            title_text='COUNTY COUNT AND TRENDS FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': False
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            height=177
        )

        county_indicator_fig = go.Figure(data=county_indicator_data, layout=county_indicator_layout)

        with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
            counties = json.load(response)

        selected_week_df_raw = current_df[[
            'fips', 'county', 'rig_count'
        ]].groupby(['fips', 'county']).sum().reset_index()

        selected_week_df = selected_week_df_raw.rename(columns={'rig_count': 'rig_count_select'})

        ref_week_df_raw = reference_df[[
            'fips', 'county', 'rig_count'
        ]].groupby(['fips', 'county']).sum().reset_index()

        ref_week_df = ref_week_df_raw.rename(columns={'rig_count': 'rig_count_ref'})

        map_df = selected_week_df.merge(ref_week_df, 'outer', ['fips', 'county'])

        map_df['rig_count_ref'] = map_df['rig_count_ref'].fillna(0)
        map_df['rig_count_select'] = map_df['rig_count_select'].fillna(0)

        map_df['rig_count_ref'] = map_df['rig_count_ref'].astype(int)
        map_df['rig_count_select'] = map_df['rig_count_select'].astype(int)

        map_df['difference'] = map_df['rig_count_select'] - map_df['rig_count_ref']

        map_data = go.Choropleth(
            name='Counties',
            geojson=counties,
            locations=map_df['fips'],
            z=map_df['difference'],
            zmid=0,
            colorscale=plus_minus_colorscale,
            hovertemplate=map_df['county'] + '<br>Rig +/-: %{z}<br>Rig Count: ' + map_df['rig_count_select'].astype(str)
        )

        map_layout = go.Layout(
            geo={
                'scope': 'usa',
                'showlakes': True
            },
            title_text='COUNTY-LEVEL 1-MONTH +/- HEAT MAP FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            titlefont={
                'size': 8
            },
            margin={
                'r': 0,
                't': 20,
                'l': 0,
                'b': 0
            },
            template="plotly_dark",
            height=354
        )

        map_fig = go.Figure(data=map_data, layout=map_layout)

        totals_df_raw = filtered_share_df[['date', 'rig_count']].groupby('date').sum().reset_index()
        totals_df = totals_df_raw.rename(columns={'rig_count': 'overall_weekly_total'})

        drill_for_df = filtered_share_df[[
            'date',
            'drill_for',
            'rig_count'
        ]].groupby([
            'date',
            'drill_for'
        ]).sum().reset_index()

        drill_for_totals_df = drill_for_df.merge(totals_df, how='left', on='date')

        drill_for_totals_df['share'] = (
                    (drill_for_totals_df['rig_count']) / (drill_for_totals_df['overall_weekly_total']))

        drill_for_data = [
            go.Scatter(
                name=i[:4],
                x=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['date'],
                y=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['share'],
                hovertemplate='%{x}<br>' + i + '<br>%{y}'
            ) for i in drill_for_totals_df['drill_for'].unique()
        ]

        drill_for_layout = go.Layout(
            title_text='1M DRILL-FOR HISTORY',
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': True,
                'tickformat': ',.0%',
                'tickfont': {
                    'size': 8
                }
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            showlegend=False,
        )

        drill_for_fig = go.Figure(data=drill_for_data, layout=drill_for_layout)

        well_depth_df = filtered_share_df[[
            'date',
            'well_depth',
            'rig_count'
        ]].groupby([
            'date',
            'well_depth'
        ]).sum().reset_index()

        well_depth_totals_df = well_depth_df.merge(totals_df, how='left', on='date')

        well_depth_totals_df['share'] = (
                (well_depth_totals_df['rig_count']) / (well_depth_totals_df['overall_weekly_total'])
        )

        well_depth_data = [
            go.Scatter(
                name=i[:4],
                x=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['date'],
                y=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['share'],
                hovertemplate='%{x}<br>' + i + '<br>%{y}'
            ) for i in well_depth_totals_df['well_depth'].unique()
        ]

        well_depth_layout = go.Layout(
            title_text='1M WELL-DEPTH HISTORY',
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': True,
                'tickformat': ',.0%',
                'tickfont': {
                    'size': 8
                }
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            showlegend=False,
        )

        well_depth_fig = go.Figure(data=well_depth_data, layout=well_depth_layout)

        trajectory_df = filtered_share_df[[
            'date',
            'trajectory',
            'rig_count'
        ]].groupby([
            'date',
            'trajectory'
        ]).sum().reset_index()

        trajectory_totals_df = trajectory_df.merge(totals_df, how='left', on='date')

        trajectory_totals_df['share'] = (
                (trajectory_totals_df['rig_count']) / (trajectory_totals_df['overall_weekly_total']))

        trajectory_data = [
            go.Scatter(
                name=i[:4],
                x=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['date'],
                y=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['share'],
                hovertemplate='%{x}<br>' + i + '<br>%{y}'
            ) for i in trajectory_totals_df['trajectory'].unique()
        ]

        trajectory_layout = go.Layout(
            title_text='1M TRAJECTORY HISTORY',
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': True,
                'tickformat': ',.0%',
                'tickfont': {
                    'size': 8
                }
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            showlegend=False,
        )

        trajectory_fig = go.Figure(data=trajectory_data, layout=trajectory_layout)

        #### rankings by state section ######

        state_table_df_raw = current_df[[
            'state', 'rig_count'
        ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})

        state_table_df_ref_raw = reference_df[[
            'state', 'rig_count'
        ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})

        state_table_df = state_table_df_raw.merge(
            state_table_df_ref_raw,
            'outer',
            ['state']
        )

        state_table_df['rig_count_after'] = state_table_df['rig_count_after'].fillna(0)
        state_table_df['rig_count_before'] = state_table_df['rig_count_before'].fillna(0)

        state_table_df['rig_count_after'] = state_table_df['rig_count_after'].astype(int)
        state_table_df['rig_count_before'] = state_table_df['rig_count_before'].astype(int)

        state_table_df['difference'] = state_table_df['rig_count_after'] - state_table_df['rig_count_before']

        state_table_df['rank'] = state_table_df['difference'].rank(method='min', ascending=False)

        state_table_df_sort = state_table_df.sort_values(
            by=['difference', 'rig_count_after'],
            ascending=[False, False]
        )

        state_final_table_df = pd.DataFrame({
            'RANK': [int(x) for x in state_table_df_sort['rank'].tolist()],
            'STATE': state_table_df_sort['state'].tolist(),
            'RIGS': state_table_df_sort['rig_count_after'].tolist(),
            '+/-': state_table_df_sort['difference'].tolist()
        })

        state_table_columns = [{
            'name': i, 'id': i
        } for i in state_final_table_df.columns]

        state_table_data = state_final_table_df.to_dict('records')

        #### rankings by basin section ######

        basin_table_df_raw = current_df[[
            'basin', 'rig_count'
        ]].groupby(['basin']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})

        basin_table_df_ref_raw = reference_df[[
            'basin', 'rig_count'
        ]].groupby(['basin']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})

        basin_table_df = basin_table_df_raw.merge(
            basin_table_df_ref_raw,
            'outer',
            ['basin']
        )

        basin_table_df['rig_count_after'] = basin_table_df['rig_count_after'].fillna(0)
        basin_table_df['rig_count_before'] = basin_table_df['rig_count_before'].fillna(0)

        basin_table_df['rig_count_after'] = basin_table_df['rig_count_after'].astype(int)
        basin_table_df['rig_count_before'] = basin_table_df['rig_count_before'].astype(int)

        basin_table_df['difference'] = basin_table_df['rig_count_after'] - basin_table_df['rig_count_before']

        basin_table_df['rank'] = basin_table_df['difference'].rank(method='min', ascending=False)

        basin_table_df_sort = basin_table_df.sort_values(
            by=['difference', 'rig_count_after'],
            ascending=[False, False]
        )

        basin_final_table_df = pd.DataFrame({
            'RANK': [int(x) for x in basin_table_df_sort['rank'].tolist()],
            'BASIN': basin_table_df_sort['basin'].tolist(),
            'RIGS': basin_table_df_sort['rig_count_after'].tolist(),
            '+/-': basin_table_df_sort['difference'].tolist()
        })

        basin_table_columns = [{
            'name': i, 'id': i
        } for i in basin_final_table_df.columns]

        basin_table_data = basin_final_table_df.to_dict('records')

        #### rankings by county section ######

        county_table_df_raw = current_df[[
            'county', 'rig_count'
        ]].groupby(['county']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})

        county_table_df_ref_raw = reference_df[[
            'county', 'rig_count'
        ]].groupby(['county']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})

        county_table_df = county_table_df_raw.merge(
            county_table_df_ref_raw,
            'outer',
            ['county']
        )

        county_table_df['rig_count_after'] = county_table_df['rig_count_after'].fillna(0)
        county_table_df['rig_count_before'] = county_table_df['rig_count_before'].fillna(0)

        county_table_df['rig_count_after'] = county_table_df['rig_count_after'].astype(int)
        county_table_df['rig_count_before'] = county_table_df['rig_count_before'].astype(int)

        county_table_df['difference'] = county_table_df['rig_count_after'] - county_table_df['rig_count_before']

        county_table_df['rank'] = county_table_df['difference'].rank(method='min', ascending=False)

        county_table_df_sort = county_table_df.sort_values(
            by=['difference', 'rig_count_after'],
            ascending=[False, False]
        )

        county_final_table_df = pd.DataFrame({
            'RANK': [int(x) for x in county_table_df_sort['rank'].tolist()],
            'COUNTY': county_table_df_sort['county'].tolist(),
            'RIGS': county_table_df_sort['rig_count_after'].tolist(),
            '+/-': county_table_df_sort['difference'].tolist()
        })

        county_table_columns = [{
            'name': i, 'id': i
        } for i in county_final_table_df.columns]

        county_table_data = county_final_table_df.to_dict('records')

        return indicator_fig, county_indicator_fig, map_fig, \
               drill_for_fig, well_depth_fig, trajectory_fig, \
               state_table_columns, state_table_data, basin_table_columns, basin_table_data, \
               county_table_columns, county_table_data


    elif dropdown_value == '3m':
        reference_date = three_month_date
        scatter_reference_date = one_year_date

        df = functions.get_df(scatter_reference_date, date)

        share_df = functions.get_df(reference_date, date)

        filtered_df = df[
            df['state'].isin(states) &
            df['basin'].isin(basins) &
            df['drill_for'].isin(drill_for) &
            df['location'].isin(locations) &
            df['trajectory'].isin(trajectories) &
            df['well_depth'].isin(well_depths)
        ]

        filtered_share_df = share_df[
            share_df['state'].isin(states) &
            share_df['basin'].isin(basins) &
            share_df['drill_for'].isin(drill_for) &
            share_df['location'].isin(locations) &
            share_df['trajectory'].isin(trajectories) &
            share_df['well_depth'].isin(well_depths)
        ]


        current_df = filtered_df[filtered_df['date'] == date]
        reference_df = filtered_df[filtered_df['date'] == reference_date]

        scatter_df = filtered_df[['date', 'rig_count']].groupby('date').sum().reset_index()

        county_scatter_df = filtered_df[['date', 'county']].groupby(['date'])['county'].nunique().reset_index()

        indicator_data = [
            go.Indicator(
                mode='number+delta',
                value=current_df['rig_count'].sum(),
                delta={'reference': reference_df['rig_count'].sum()},
            ),
            go.Scatter(
                name='1-YEAR TREND',
                x=scatter_df['date'].tolist(),
                y=scatter_df['rig_count'].tolist()
            )
        ]

        indicator_layout = go.Layout(
            title_text='RIG COUNT AND TRENDS FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': False
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            height=177
        )

        indicator_fig = go.Figure(data=indicator_data, layout=indicator_layout)

        county_indicator_data = [
            go.Indicator(
                mode='number+delta',
                value=current_df['county'].nunique(),
                delta={'reference': reference_df['county'].nunique()},
            ),
            go.Scatter(
                name='1-YEAR TREND',
                x=county_scatter_df['date'].tolist(),
                y=county_scatter_df['county'].tolist()
            )
        ]

        county_indicator_layout = go.Layout(
            # title='COGS',
            # height=100,
            title_text='COUNTY COUNT AND TRENDS FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': False
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            height=177
        )

        county_indicator_fig = go.Figure(data=county_indicator_data, layout=county_indicator_layout)

        with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
            counties = json.load(response)

        selected_week_df_raw = current_df[[
            'fips', 'county', 'rig_count'
        ]].groupby(['fips', 'county']).sum().reset_index()

        selected_week_df = selected_week_df_raw.rename(columns={'rig_count': 'rig_count_select'})

        ref_week_df_raw = reference_df[[
            'fips', 'county', 'rig_count'
        ]].groupby(['fips', 'county']).sum().reset_index()

        ref_week_df = ref_week_df_raw.rename(columns={'rig_count': 'rig_count_ref'})

        map_df = selected_week_df.merge(ref_week_df, 'outer', ['fips', 'county'])

        map_df['rig_count_ref'] = map_df['rig_count_ref'].fillna(0)
        map_df['rig_count_select'] = map_df['rig_count_select'].fillna(0)

        map_df['rig_count_ref'] = map_df['rig_count_ref'].astype(int)
        map_df['rig_count_select'] = map_df['rig_count_select'].astype(int)

        map_df['difference'] = map_df['rig_count_select'] - map_df['rig_count_ref']

        map_data = go.Choropleth(
            name='Counties',
            geojson=counties,
            locations=map_df['fips'],
            z=map_df['difference'],
            zmid=0,
            colorscale=plus_minus_colorscale,
            hovertemplate=map_df['county'] + '<br>Rig +/-: %{z}<br>Rig Count: ' + map_df['rig_count_select'].astype(str)
        )

        map_layout = go.Layout(
            geo={
                'scope': 'usa',
                'showlakes': True
            },
            title_text='COUNTY-LEVEL 3-MONTH +/- HEAT MAP FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            titlefont={
                'size': 8
            },
            margin={
                'r': 0,
                't': 20,
                'l': 0,
                'b': 0
            },
            template="plotly_dark",
            height=354
        )

        map_fig = go.Figure(data=map_data, layout=map_layout)

        totals_df_raw = filtered_share_df[['date', 'rig_count']].groupby('date').sum().reset_index()
        totals_df = totals_df_raw.rename(columns={'rig_count': 'overall_weekly_total'})

        drill_for_df = filtered_share_df[[
            'date',
            'drill_for',
            'rig_count'
        ]].groupby([
            'date',
            'drill_for'
        ]).sum().reset_index()

        drill_for_totals_df = drill_for_df.merge(totals_df, how='left', on='date')

        drill_for_totals_df['share'] = (
                    (drill_for_totals_df['rig_count']) / (drill_for_totals_df['overall_weekly_total']))

        drill_for_data = [
            go.Scatter(
                name=i[:4],
                x=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['date'],
                y=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['share'],
                hovertemplate='%{x}<br>' + i + '<br>%{y}'
            ) for i in drill_for_totals_df['drill_for'].unique()
        ]

        drill_for_layout = go.Layout(
            title_text='3M DRILL-FOR HISTORY',
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': True,
                'tickformat': ',.0%',
                'tickfont': {
                    'size': 8
                }
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            showlegend=False,
        )

        drill_for_fig = go.Figure(data=drill_for_data, layout=drill_for_layout)

        well_depth_df = filtered_share_df[[
            'date',
            'well_depth',
            'rig_count'
        ]].groupby([
            'date',
            'well_depth'
        ]).sum().reset_index()

        well_depth_totals_df = well_depth_df.merge(totals_df, how='left', on='date')

        well_depth_totals_df['share'] = (
                (well_depth_totals_df['rig_count']) / (well_depth_totals_df['overall_weekly_total'])
        )

        well_depth_data = [
            go.Scatter(
                name=i[:4],
                x=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['date'],
                y=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['share'],
                hovertemplate='%{x}<br>' + i + '<br>%{y}'
            ) for i in well_depth_totals_df['well_depth'].unique()
        ]

        well_depth_layout = go.Layout(
            title_text='3M WELL-DEPTH HISTORY',
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': True,
                'tickformat': ',.0%',
                'tickfont': {
                    'size': 8
                }
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            showlegend=False,
        )

        well_depth_fig = go.Figure(data=well_depth_data, layout=well_depth_layout)

        trajectory_df = filtered_share_df[[
            'date',
            'trajectory',
            'rig_count'
        ]].groupby([
            'date',
            'trajectory'
        ]).sum().reset_index()

        trajectory_totals_df = trajectory_df.merge(totals_df, how='left', on='date')

        trajectory_totals_df['share'] = (
                (trajectory_totals_df['rig_count']) / (trajectory_totals_df['overall_weekly_total']))

        trajectory_data = [
            go.Scatter(
                name=i[:4],
                x=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['date'],
                y=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['share'],
                hovertemplate='%{x}<br>' + i + '<br>%{y}'
            ) for i in trajectory_totals_df['trajectory'].unique()
        ]

        trajectory_layout = go.Layout(
            title_text='3M TRAJECTORY HISTORY',
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': True,
                'tickformat': ',.0%',
                'tickfont': {
                    'size': 8
                }
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            showlegend=False,
        )

        trajectory_fig = go.Figure(data=trajectory_data, layout=trajectory_layout)

        #### rankings by state section ######

        state_table_df_raw = current_df[[
            'state', 'rig_count'
        ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})

        state_table_df_ref_raw = reference_df[[
            'state', 'rig_count'
        ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})

        state_table_df = state_table_df_raw.merge(
            state_table_df_ref_raw,
            'outer',
            ['state']
        )

        state_table_df['rig_count_after'] = state_table_df['rig_count_after'].fillna(0)
        state_table_df['rig_count_before'] = state_table_df['rig_count_before'].fillna(0)

        state_table_df['rig_count_after'] = state_table_df['rig_count_after'].astype(int)
        state_table_df['rig_count_before'] = state_table_df['rig_count_before'].astype(int)

        state_table_df['difference'] = state_table_df['rig_count_after'] - state_table_df['rig_count_before']

        state_table_df['rank'] = state_table_df['difference'].rank(method='min', ascending=False)

        state_table_df_sort = state_table_df.sort_values(
            by=['difference', 'rig_count_after'],
            ascending=[False, False]
        )

        state_final_table_df = pd.DataFrame({
            'RANK': [int(x) for x in state_table_df_sort['rank'].tolist()],
            'STATE': state_table_df_sort['state'].tolist(),
            'RIGS': state_table_df_sort['rig_count_after'].tolist(),
            '+/-': state_table_df_sort['difference'].tolist()
        })

        state_table_columns = [{
            'name': i, 'id': i
        } for i in state_final_table_df.columns]

        state_table_data = state_final_table_df.to_dict('records')

        #### rankings by basin section ######

        basin_table_df_raw = current_df[[
            'basin', 'rig_count'
        ]].groupby(['basin']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})

        basin_table_df_ref_raw = reference_df[[
            'basin', 'rig_count'
        ]].groupby(['basin']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})

        basin_table_df = basin_table_df_raw.merge(
            basin_table_df_ref_raw,
            'outer',
            ['basin']
        )

        basin_table_df['rig_count_after'] = basin_table_df['rig_count_after'].fillna(0)
        basin_table_df['rig_count_before'] = basin_table_df['rig_count_before'].fillna(0)

        basin_table_df['rig_count_after'] = basin_table_df['rig_count_after'].astype(int)
        basin_table_df['rig_count_before'] = basin_table_df['rig_count_before'].astype(int)

        basin_table_df['difference'] = basin_table_df['rig_count_after'] - basin_table_df['rig_count_before']

        basin_table_df['rank'] = basin_table_df['difference'].rank(method='min', ascending=False)

        basin_table_df_sort = basin_table_df.sort_values(
            by=['difference', 'rig_count_after'],
            ascending=[False, False]
        )

        basin_final_table_df = pd.DataFrame({
            'RANK': [int(x) for x in basin_table_df_sort['rank'].tolist()],
            'BASIN': basin_table_df_sort['basin'].tolist(),
            'RIGS': basin_table_df_sort['rig_count_after'].tolist(),
            '+/-': basin_table_df_sort['difference'].tolist()
        })

        basin_table_columns = [{
            'name': i, 'id': i
        } for i in basin_final_table_df.columns]

        basin_table_data = basin_final_table_df.to_dict('records')

        #### rankings by county section ######

        county_table_df_raw = current_df[[
            'county', 'rig_count'
        ]].groupby(['county']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})

        county_table_df_ref_raw = reference_df[[
            'county', 'rig_count'
        ]].groupby(['county']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})

        county_table_df = county_table_df_raw.merge(
            county_table_df_ref_raw,
            'outer',
            ['county']
        )

        county_table_df['rig_count_after'] = county_table_df['rig_count_after'].fillna(0)
        county_table_df['rig_count_before'] = county_table_df['rig_count_before'].fillna(0)

        county_table_df['rig_count_after'] = county_table_df['rig_count_after'].astype(int)
        county_table_df['rig_count_before'] = county_table_df['rig_count_before'].astype(int)

        county_table_df['difference'] = county_table_df['rig_count_after'] - county_table_df['rig_count_before']

        county_table_df['rank'] = county_table_df['difference'].rank(method='min', ascending=False)

        county_table_df_sort = county_table_df.sort_values(
            by=['difference', 'rig_count_after'],
            ascending=[False, False]
        )

        county_final_table_df = pd.DataFrame({
            'RANK': [int(x) for x in county_table_df_sort['rank'].tolist()],
            'COUNTY': county_table_df_sort['county'].tolist(),
            'RIGS': county_table_df_sort['rig_count_after'].tolist(),
            '+/-': county_table_df_sort['difference'].tolist()
        })

        county_table_columns = [{
            'name': i, 'id': i
        } for i in county_final_table_df.columns]

        county_table_data = county_final_table_df.to_dict('records')

        return indicator_fig, county_indicator_fig, map_fig, \
               drill_for_fig, well_depth_fig, trajectory_fig, \
               state_table_columns, state_table_data, basin_table_columns, basin_table_data, \
               county_table_columns, county_table_data


    elif dropdown_value == '6m':
        reference_date = six_month_date
        scatter_reference_date = one_year_date

        df = functions.get_df(scatter_reference_date, date)

        share_df = functions.get_df(reference_date, date)

        filtered_df = df[
            df['state'].isin(states) &
            df['basin'].isin(basins) &
            df['drill_for'].isin(drill_for) &
            df['location'].isin(locations) &
            df['trajectory'].isin(trajectories) &
            df['well_depth'].isin(well_depths)
        ]

        filtered_share_df = share_df[
            share_df['state'].isin(states) &
            share_df['basin'].isin(basins) &
            share_df['drill_for'].isin(drill_for) &
            share_df['location'].isin(locations) &
            share_df['trajectory'].isin(trajectories) &
            share_df['well_depth'].isin(well_depths)
        ]


        current_df = filtered_df[filtered_df['date'] == date]
        reference_df = filtered_df[filtered_df['date'] == reference_date]

        scatter_df = filtered_df[['date', 'rig_count']].groupby('date').sum().reset_index()

        county_scatter_df = filtered_df[['date', 'county']].groupby(['date'])['county'].nunique().reset_index()

        indicator_data = [
            go.Indicator(
                mode='number+delta',
                value=current_df['rig_count'].sum(),
                delta={'reference': reference_df['rig_count'].sum()},
            ),
            go.Scatter(
                name='1-YEAR TREND',
                x=scatter_df['date'].tolist(),
                y=scatter_df['rig_count'].tolist()
            )
        ]

        indicator_layout = go.Layout(
            title_text='RIG COUNT AND TRENDS FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': False
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            height=177
        )

        indicator_fig = go.Figure(data=indicator_data, layout=indicator_layout)

        county_indicator_data = [
            go.Indicator(
                mode='number+delta',
                value=current_df['county'].nunique(),
                delta={'reference': reference_df['county'].nunique()},
            ),
            go.Scatter(
                name='1-YEAR TREND',
                x=county_scatter_df['date'].tolist(),
                y=county_scatter_df['county'].tolist()
            )
        ]

        county_indicator_layout = go.Layout(
            # title='COGS',
            # height=100,
            title_text='COUNTY COUNT AND TRENDS FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': False
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            height=177
        )

        county_indicator_fig = go.Figure(data=county_indicator_data, layout=county_indicator_layout)

        with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
            counties = json.load(response)

        selected_week_df_raw = current_df[[
            'fips', 'county', 'rig_count'
        ]].groupby(['fips', 'county']).sum().reset_index()

        selected_week_df = selected_week_df_raw.rename(columns={'rig_count': 'rig_count_select'})

        ref_week_df_raw = reference_df[[
            'fips', 'county', 'rig_count'
        ]].groupby(['fips', 'county']).sum().reset_index()

        ref_week_df = ref_week_df_raw.rename(columns={'rig_count': 'rig_count_ref'})

        map_df = selected_week_df.merge(ref_week_df, 'outer', ['fips', 'county'])

        map_df['rig_count_ref'] = map_df['rig_count_ref'].fillna(0)
        map_df['rig_count_select'] = map_df['rig_count_select'].fillna(0)

        map_df['rig_count_ref'] = map_df['rig_count_ref'].astype(int)
        map_df['rig_count_select'] = map_df['rig_count_select'].astype(int)

        map_df['difference'] = map_df['rig_count_select'] - map_df['rig_count_ref']

        map_data = go.Choropleth(
            name='Counties',
            geojson=counties,
            locations=map_df['fips'],
            z=map_df['difference'],
            zmid=0,
            colorscale=plus_minus_colorscale,
            hovertemplate=map_df['county'] + '<br>Rig +/-: %{z}<br>Rig Count: ' + map_df['rig_count_select'].astype(str)
        )

        map_layout = go.Layout(
            geo={
                'scope': 'usa',
                'showlakes': True
            },
            title_text='COUNTY-LEVEL 6-MONTH +/- HEAT MAP FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            titlefont={
                'size': 8
            },
            margin={
                'r': 0,
                't': 20,
                'l': 0,
                'b': 0
            },
            template="plotly_dark",
            height=354
        )

        map_fig = go.Figure(data=map_data, layout=map_layout)

        totals_df_raw = filtered_share_df[['date', 'rig_count']].groupby('date').sum().reset_index()
        totals_df = totals_df_raw.rename(columns={'rig_count': 'overall_weekly_total'})

        drill_for_df = filtered_share_df[[
            'date',
            'drill_for',
            'rig_count'
        ]].groupby([
            'date',
            'drill_for'
        ]).sum().reset_index()

        drill_for_totals_df = drill_for_df.merge(totals_df, how='left', on='date')

        drill_for_totals_df['share'] = (
                    (drill_for_totals_df['rig_count']) / (drill_for_totals_df['overall_weekly_total']))

        drill_for_data = [
            go.Scatter(
                name=i[:4],
                x=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['date'],
                y=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['share'],
                hovertemplate='%{x}<br>' + i + '<br>%{y}'
            ) for i in drill_for_totals_df['drill_for'].unique()
        ]

        drill_for_layout = go.Layout(
            title_text='6M DRILL-FOR HISTORY',
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': True,
                'tickformat': ',.0%',
                'tickfont': {
                    'size': 8
                }
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            showlegend=False,
        )

        drill_for_fig = go.Figure(data=drill_for_data, layout=drill_for_layout)

        well_depth_df = filtered_share_df[[
            'date',
            'well_depth',
            'rig_count'
        ]].groupby([
            'date',
            'well_depth'
        ]).sum().reset_index()

        well_depth_totals_df = well_depth_df.merge(totals_df, how='left', on='date')

        well_depth_totals_df['share'] = (
                (well_depth_totals_df['rig_count']) / (well_depth_totals_df['overall_weekly_total'])
        )

        well_depth_data = [
            go.Scatter(
                name=i[:4],
                x=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['date'],
                y=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['share'],
                hovertemplate='%{x}<br>' + i + '<br>%{y}'
            ) for i in well_depth_totals_df['well_depth'].unique()
        ]

        well_depth_layout = go.Layout(
            title_text='6M WELL-DEPTH HISTORY',
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': True,
                'tickformat': ',.0%',
                'tickfont': {
                    'size': 8
                }
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            showlegend=False,
        )

        well_depth_fig = go.Figure(data=well_depth_data, layout=well_depth_layout)

        trajectory_df = filtered_share_df[[
            'date',
            'trajectory',
            'rig_count'
        ]].groupby([
            'date',
            'trajectory'
        ]).sum().reset_index()

        trajectory_totals_df = trajectory_df.merge(totals_df, how='left', on='date')

        trajectory_totals_df['share'] = (
                (trajectory_totals_df['rig_count']) / (trajectory_totals_df['overall_weekly_total']))

        trajectory_data = [
            go.Scatter(
                name=i[:4],
                x=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['date'],
                y=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['share'],
                hovertemplate='%{x}<br>' + i + '<br>%{y}'
            ) for i in trajectory_totals_df['trajectory'].unique()
        ]

        trajectory_layout = go.Layout(
            title_text='6M TRAJECTORY HISTORY',
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': True,
                'tickformat': ',.0%',
                'tickfont': {
                    'size': 8
                }
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            showlegend=False,
        )

        trajectory_fig = go.Figure(data=trajectory_data, layout=trajectory_layout)

        #### rankings by state section ######

        state_table_df_raw = current_df[[
            'state', 'rig_count'
        ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})

        state_table_df_ref_raw = reference_df[[
            'state', 'rig_count'
        ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})

        state_table_df = state_table_df_raw.merge(
            state_table_df_ref_raw,
            'outer',
            ['state']
        )

        state_table_df['rig_count_after'] = state_table_df['rig_count_after'].fillna(0)
        state_table_df['rig_count_before'] = state_table_df['rig_count_before'].fillna(0)

        state_table_df['rig_count_after'] = state_table_df['rig_count_after'].astype(int)
        state_table_df['rig_count_before'] = state_table_df['rig_count_before'].astype(int)

        state_table_df['difference'] = state_table_df['rig_count_after'] - state_table_df['rig_count_before']

        state_table_df['rank'] = state_table_df['difference'].rank(method='min', ascending=False)

        state_table_df_sort = state_table_df.sort_values(
            by=['difference', 'rig_count_after'],
            ascending=[False, False]
        )

        state_final_table_df = pd.DataFrame({
            'RANK': [int(x) for x in state_table_df_sort['rank'].tolist()],
            'STATE': state_table_df_sort['state'].tolist(),
            'RIGS': state_table_df_sort['rig_count_after'].tolist(),
            '+/-': state_table_df_sort['difference'].tolist()
        })

        state_table_columns = [{
            'name': i, 'id': i
        } for i in state_final_table_df.columns]

        state_table_data = state_final_table_df.to_dict('records')

        #### rankings by basin section ######

        basin_table_df_raw = current_df[[
            'basin', 'rig_count'
        ]].groupby(['basin']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})

        basin_table_df_ref_raw = reference_df[[
            'basin', 'rig_count'
        ]].groupby(['basin']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})

        basin_table_df = basin_table_df_raw.merge(
            basin_table_df_ref_raw,
            'outer',
            ['basin']
        )

        basin_table_df['rig_count_after'] = basin_table_df['rig_count_after'].fillna(0)
        basin_table_df['rig_count_before'] = basin_table_df['rig_count_before'].fillna(0)

        basin_table_df['rig_count_after'] = basin_table_df['rig_count_after'].astype(int)
        basin_table_df['rig_count_before'] = basin_table_df['rig_count_before'].astype(int)

        basin_table_df['difference'] = basin_table_df['rig_count_after'] - basin_table_df['rig_count_before']

        basin_table_df['rank'] = basin_table_df['difference'].rank(method='min', ascending=False)

        basin_table_df_sort = basin_table_df.sort_values(
            by=['difference', 'rig_count_after'],
            ascending=[False, False]
        )

        basin_final_table_df = pd.DataFrame({
            'RANK': [int(x) for x in basin_table_df_sort['rank'].tolist()],
            'BASIN': basin_table_df_sort['basin'].tolist(),
            'RIGS': basin_table_df_sort['rig_count_after'].tolist(),
            '+/-': basin_table_df_sort['difference'].tolist()
        })

        basin_table_columns = [{
            'name': i, 'id': i
        } for i in basin_final_table_df.columns]

        basin_table_data = basin_final_table_df.to_dict('records')

        #### rankings by county section ######

        county_table_df_raw = current_df[[
            'county', 'rig_count'
        ]].groupby(['county']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})

        county_table_df_ref_raw = reference_df[[
            'county', 'rig_count'
        ]].groupby(['county']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})

        county_table_df = county_table_df_raw.merge(
            county_table_df_ref_raw,
            'outer',
            ['county']
        )

        county_table_df['rig_count_after'] = county_table_df['rig_count_after'].fillna(0)
        county_table_df['rig_count_before'] = county_table_df['rig_count_before'].fillna(0)

        county_table_df['rig_count_after'] = county_table_df['rig_count_after'].astype(int)
        county_table_df['rig_count_before'] = county_table_df['rig_count_before'].astype(int)

        county_table_df['difference'] = county_table_df['rig_count_after'] - county_table_df['rig_count_before']

        county_table_df['rank'] = county_table_df['difference'].rank(method='min', ascending=False)

        county_table_df_sort = county_table_df.sort_values(
            by=['difference', 'rig_count_after'],
            ascending=[False, False]
        )

        county_final_table_df = pd.DataFrame({
            'RANK': [int(x) for x in county_table_df_sort['rank'].tolist()],
            'COUNTY': county_table_df_sort['county'].tolist(),
            'RIGS': county_table_df_sort['rig_count_after'].tolist(),
            '+/-': county_table_df_sort['difference'].tolist()
        })

        county_table_columns = [{
            'name': i, 'id': i
        } for i in county_final_table_df.columns]

        county_table_data = county_final_table_df.to_dict('records')

        return indicator_fig, county_indicator_fig, map_fig, \
               drill_for_fig, well_depth_fig, trajectory_fig, \
               state_table_columns, state_table_data, basin_table_columns, basin_table_data, \
               county_table_columns, county_table_data


    elif dropdown_value == '1y':
        reference_date = one_year_date
        scatter_reference_date = reference_date

        df = functions.get_df(scatter_reference_date, date)

        share_df = functions.get_df(reference_date, date)

        filtered_df = df[
            df['state'].isin(states) &
            df['basin'].isin(basins) &
            df['drill_for'].isin(drill_for) &
            df['location'].isin(locations) &
            df['trajectory'].isin(trajectories) &
            df['well_depth'].isin(well_depths)
        ]

        filtered_share_df = share_df[
            share_df['state'].isin(states) &
            share_df['basin'].isin(basins) &
            share_df['drill_for'].isin(drill_for) &
            share_df['location'].isin(locations) &
            share_df['trajectory'].isin(trajectories) &
            share_df['well_depth'].isin(well_depths)
        ]


        current_df = filtered_df[filtered_df['date'] == date]
        reference_df = filtered_df[filtered_df['date'] == reference_date]

        scatter_df = filtered_df[['date', 'rig_count']].groupby('date').sum().reset_index()

        county_scatter_df = filtered_df[['date', 'county']].groupby(['date'])['county'].nunique().reset_index()

        indicator_data = [
            go.Indicator(
                mode='number+delta',
                value=current_df['rig_count'].sum(),
                delta={'reference': reference_df['rig_count'].sum()},
            ),
            go.Scatter(
                name='1-YEAR TREND',
                x=scatter_df['date'].tolist(),
                y=scatter_df['rig_count'].tolist()
            )
        ]

        indicator_layout = go.Layout(
            title_text='RIG COUNT AND TRENDS FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': False
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            height=177
        )

        indicator_fig = go.Figure(data=indicator_data, layout=indicator_layout)

        county_indicator_data = [
            go.Indicator(
                mode='number+delta',
                value=current_df['county'].nunique(),
                delta={'reference': reference_df['county'].nunique()},
            ),
            go.Scatter(
                name='1-YEAR TREND',
                x=county_scatter_df['date'].tolist(),
                y=county_scatter_df['county'].tolist()
            )
        ]

        county_indicator_layout = go.Layout(
            # title='COGS',
            # height=100,
            title_text='COUNTY COUNT AND TRENDS FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': False
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            height=177
        )

        county_indicator_fig = go.Figure(data=county_indicator_data, layout=county_indicator_layout)

        with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
            counties = json.load(response)

        selected_week_df_raw = current_df[[
            'fips', 'county', 'rig_count'
        ]].groupby(['fips', 'county']).sum().reset_index()

        selected_week_df = selected_week_df_raw.rename(columns={'rig_count': 'rig_count_select'})

        ref_week_df_raw = reference_df[[
            'fips', 'county', 'rig_count'
        ]].groupby(['fips', 'county']).sum().reset_index()

        ref_week_df = ref_week_df_raw.rename(columns={'rig_count': 'rig_count_ref'})

        map_df = selected_week_df.merge(ref_week_df, 'outer', ['fips', 'county'])

        map_df['rig_count_ref'] = map_df['rig_count_ref'].fillna(0)
        map_df['rig_count_select'] = map_df['rig_count_select'].fillna(0)

        map_df['rig_count_ref'] = map_df['rig_count_ref'].astype(int)
        map_df['rig_count_select'] = map_df['rig_count_select'].astype(int)

        map_df['difference'] = map_df['rig_count_select'] - map_df['rig_count_ref']

        map_data = go.Choropleth(
            name='Counties',
            geojson=counties,
            locations=map_df['fips'],
            z=map_df['difference'],
            zmid=0,
            colorscale=plus_minus_colorscale,
            hovertemplate=map_df['county'] + '<br>Rig +/-: %{z}<br>Rig Count: ' + map_df['rig_count_select'].astype(str)
        )

        map_layout = go.Layout(
            geo={
                'scope': 'usa',
                'showlakes': True
            },
            title_text='COUNTY-LEVEL 1-YEAR +/- HEAT MAP FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            titlefont={
                'size': 8
            },
            margin={
                'r': 0,
                't': 20,
                'l': 0,
                'b': 0
            },
            template="plotly_dark",
            height=354
        )

        map_fig = go.Figure(data=map_data, layout=map_layout)

        totals_df_raw = filtered_share_df[['date', 'rig_count']].groupby('date').sum().reset_index()
        totals_df = totals_df_raw.rename(columns={'rig_count': 'overall_weekly_total'})

        drill_for_df = filtered_share_df[[
            'date',
            'drill_for',
            'rig_count'
        ]].groupby([
            'date',
            'drill_for'
        ]).sum().reset_index()

        drill_for_totals_df = drill_for_df.merge(totals_df, how='left', on='date')

        drill_for_totals_df['share'] = (
                    (drill_for_totals_df['rig_count']) / (drill_for_totals_df['overall_weekly_total']))

        drill_for_data = [
            go.Scatter(
                name=i[:4],
                x=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['date'],
                y=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['share'],
                hovertemplate='%{x}<br>' + i + '<br>%{y}'
            ) for i in drill_for_totals_df['drill_for'].unique()
        ]

        drill_for_layout = go.Layout(
            title_text='1Y DRILL-FOR HISTORY',
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': True,
                'tickformat': ',.0%',
                'tickfont': {
                    'size': 8
                }
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            showlegend=False,
        )

        drill_for_fig = go.Figure(data=drill_for_data, layout=drill_for_layout)

        well_depth_df = filtered_share_df[[
            'date',
            'well_depth',
            'rig_count'
        ]].groupby([
            'date',
            'well_depth'
        ]).sum().reset_index()

        well_depth_totals_df = well_depth_df.merge(totals_df, how='left', on='date')

        well_depth_totals_df['share'] = (
                (well_depth_totals_df['rig_count']) / (well_depth_totals_df['overall_weekly_total'])
        )

        well_depth_data = [
            go.Scatter(
                name=i[:4],
                x=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['date'],
                y=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['share'],
                hovertemplate='%{x}<br>' + i + '<br>%{y}'
            ) for i in well_depth_totals_df['well_depth'].unique()
        ]

        well_depth_layout = go.Layout(
            title_text='1Y WELL-DEPTH HISTORY',
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': True,
                'tickformat': ',.0%',
                'tickfont': {
                    'size': 8
                }
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            showlegend=False,
        )

        well_depth_fig = go.Figure(data=well_depth_data, layout=well_depth_layout)

        trajectory_df = filtered_share_df[[
            'date',
            'trajectory',
            'rig_count'
        ]].groupby([
            'date',
            'trajectory'
        ]).sum().reset_index()

        trajectory_totals_df = trajectory_df.merge(totals_df, how='left', on='date')

        trajectory_totals_df['share'] = (
                (trajectory_totals_df['rig_count']) / (trajectory_totals_df['overall_weekly_total']))

        trajectory_data = [
            go.Scatter(
                name=i[:4],
                x=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['date'],
                y=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['share'],
                hovertemplate='%{x}<br>' + i + '<br>%{y}'
            ) for i in trajectory_totals_df['trajectory'].unique()
        ]

        trajectory_layout = go.Layout(
            title_text='1Y TRAJECTORY HISTORY',
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': True,
                'tickformat': ',.0%',
                'tickfont': {
                    'size': 8
                }
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            showlegend=False,
        )

        trajectory_fig = go.Figure(data=trajectory_data, layout=trajectory_layout)

        #### rankings by state section ######

        state_table_df_raw = current_df[[
            'state', 'rig_count'
        ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})

        state_table_df_ref_raw = reference_df[[
            'state', 'rig_count'
        ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})

        state_table_df = state_table_df_raw.merge(
            state_table_df_ref_raw,
            'outer',
            ['state']
        )

        state_table_df['rig_count_after'] = state_table_df['rig_count_after'].fillna(0)
        state_table_df['rig_count_before'] = state_table_df['rig_count_before'].fillna(0)

        state_table_df['rig_count_after'] = state_table_df['rig_count_after'].astype(int)
        state_table_df['rig_count_before'] = state_table_df['rig_count_before'].astype(int)

        state_table_df['difference'] = state_table_df['rig_count_after'] - state_table_df['rig_count_before']

        state_table_df['rank'] = state_table_df['difference'].rank(method='min', ascending=False)

        state_table_df_sort = state_table_df.sort_values(
            by=['difference', 'rig_count_after'],
            ascending=[False, False]
        )

        state_final_table_df = pd.DataFrame({
            'RANK': [int(x) for x in state_table_df_sort['rank'].tolist()],
            'STATE': state_table_df_sort['state'].tolist(),
            'RIGS': state_table_df_sort['rig_count_after'].tolist(),
            '+/-': state_table_df_sort['difference'].tolist()
        })

        state_table_columns = [{
            'name': i, 'id': i
        } for i in state_final_table_df.columns]

        state_table_data = state_final_table_df.to_dict('records')

        #### rankings by basin section ######

        basin_table_df_raw = current_df[[
            'basin', 'rig_count'
        ]].groupby(['basin']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})

        basin_table_df_ref_raw = reference_df[[
            'basin', 'rig_count'
        ]].groupby(['basin']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})

        basin_table_df = basin_table_df_raw.merge(
            basin_table_df_ref_raw,
            'outer',
            ['basin']
        )

        basin_table_df['rig_count_after'] = basin_table_df['rig_count_after'].fillna(0)
        basin_table_df['rig_count_before'] = basin_table_df['rig_count_before'].fillna(0)

        basin_table_df['rig_count_after'] = basin_table_df['rig_count_after'].astype(int)
        basin_table_df['rig_count_before'] = basin_table_df['rig_count_before'].astype(int)

        basin_table_df['difference'] = basin_table_df['rig_count_after'] - basin_table_df['rig_count_before']

        basin_table_df['rank'] = basin_table_df['difference'].rank(method='min', ascending=False)

        basin_table_df_sort = basin_table_df.sort_values(
            by=['difference', 'rig_count_after'],
            ascending=[False, False]
        )

        basin_final_table_df = pd.DataFrame({
            'RANK': [int(x) for x in basin_table_df_sort['rank'].tolist()],
            'BASIN': basin_table_df_sort['basin'].tolist(),
            'RIGS': basin_table_df_sort['rig_count_after'].tolist(),
            '+/-': basin_table_df_sort['difference'].tolist()
        })

        basin_table_columns = [{
            'name': i, 'id': i
        } for i in basin_final_table_df.columns]

        basin_table_data = basin_final_table_df.to_dict('records')

        #### rankings by county section ######

        county_table_df_raw = current_df[[
            'county', 'rig_count'
        ]].groupby(['county']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})

        county_table_df_ref_raw = reference_df[[
            'county', 'rig_count'
        ]].groupby(['county']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})

        county_table_df = county_table_df_raw.merge(
            county_table_df_ref_raw,
            'outer',
            ['county']
        )

        county_table_df['rig_count_after'] = county_table_df['rig_count_after'].fillna(0)
        county_table_df['rig_count_before'] = county_table_df['rig_count_before'].fillna(0)

        county_table_df['rig_count_after'] = county_table_df['rig_count_after'].astype(int)
        county_table_df['rig_count_before'] = county_table_df['rig_count_before'].astype(int)

        county_table_df['difference'] = county_table_df['rig_count_after'] - county_table_df['rig_count_before']

        county_table_df['rank'] = county_table_df['difference'].rank(method='min', ascending=False)

        county_table_df_sort = county_table_df.sort_values(
            by=['difference', 'rig_count_after'],
            ascending=[False, False]
        )

        county_final_table_df = pd.DataFrame({
            'RANK': [int(x) for x in county_table_df_sort['rank'].tolist()],
            'COUNTY': county_table_df_sort['county'].tolist(),
            'RIGS': county_table_df_sort['rig_count_after'].tolist(),
            '+/-': county_table_df_sort['difference'].tolist()
        })

        county_table_columns = [{
            'name': i, 'id': i
        } for i in county_final_table_df.columns]

        county_table_data = county_final_table_df.to_dict('records')

        return indicator_fig, county_indicator_fig, map_fig, \
               drill_for_fig, well_depth_fig, trajectory_fig, \
               state_table_columns, state_table_data, basin_table_columns, basin_table_data, \
               county_table_columns, county_table_data



    elif dropdown_value == '3y':
        reference_date = three_year_date
        scatter_reference_date = reference_date

        df = functions.get_df(scatter_reference_date, date)

        share_df = functions.get_df(reference_date, date)

        filtered_df = df[
            df['state'].isin(states) &
            df['basin'].isin(basins) &
            df['drill_for'].isin(drill_for) &
            df['location'].isin(locations) &
            df['trajectory'].isin(trajectories) &
            df['well_depth'].isin(well_depths)
        ]

        filtered_share_df = share_df[
            share_df['state'].isin(states) &
            share_df['basin'].isin(basins) &
            share_df['drill_for'].isin(drill_for) &
            share_df['location'].isin(locations) &
            share_df['trajectory'].isin(trajectories) &
            share_df['well_depth'].isin(well_depths)
        ]


        current_df = filtered_df[filtered_df['date'] == date]
        reference_df = filtered_df[filtered_df['date'] == reference_date]

        scatter_df = filtered_df[['date', 'rig_count']].groupby('date').sum().reset_index()

        county_scatter_df = filtered_df[['date', 'county']].groupby(['date'])['county'].nunique().reset_index()

        indicator_data = [
            go.Indicator(
                mode='number+delta',
                value=current_df['rig_count'].sum(),
                delta={'reference': reference_df['rig_count'].sum()},
            ),
            go.Scatter(
                name='1-YEAR TREND',
                x=scatter_df['date'].tolist(),
                y=scatter_df['rig_count'].tolist()
            )
        ]

        indicator_layout = go.Layout(
            title_text='RIG COUNT AND TRENDS FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': False
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            height=177
        )

        indicator_fig = go.Figure(data=indicator_data, layout=indicator_layout)

        county_indicator_data = [
            go.Indicator(
                mode='number+delta',
                value=current_df['county'].nunique(),
                delta={'reference': reference_df['county'].nunique()},
            ),
            go.Scatter(
                name='1-YEAR TREND',
                x=county_scatter_df['date'].tolist(),
                y=county_scatter_df['county'].tolist()
            )
        ]

        county_indicator_layout = go.Layout(
            # title='COGS',
            # height=100,
            title_text='COUNTY COUNT AND TRENDS FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': False
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            height=177
        )

        county_indicator_fig = go.Figure(data=county_indicator_data, layout=county_indicator_layout)

        with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
            counties = json.load(response)

        selected_week_df_raw = current_df[[
            'fips', 'county', 'rig_count'
        ]].groupby(['fips', 'county']).sum().reset_index()

        selected_week_df = selected_week_df_raw.rename(columns={'rig_count': 'rig_count_select'})

        ref_week_df_raw = reference_df[[
            'fips', 'county', 'rig_count'
        ]].groupby(['fips', 'county']).sum().reset_index()

        ref_week_df = ref_week_df_raw.rename(columns={'rig_count': 'rig_count_ref'})

        map_df = selected_week_df.merge(ref_week_df, 'outer', ['fips', 'county'])

        map_df['rig_count_ref'] = map_df['rig_count_ref'].fillna(0)
        map_df['rig_count_select'] = map_df['rig_count_select'].fillna(0)

        map_df['rig_count_ref'] = map_df['rig_count_ref'].astype(int)
        map_df['rig_count_select'] = map_df['rig_count_select'].astype(int)

        map_df['difference'] = map_df['rig_count_select'] - map_df['rig_count_ref']

        map_data = go.Choropleth(
            name='Counties',
            geojson=counties,
            locations=map_df['fips'],
            z=map_df['difference'],
            zmid=0,
            colorscale=plus_minus_colorscale,
            hovertemplate=map_df['county'] + '<br>Rig +/-: %{z}<br>Rig Count: ' + map_df['rig_count_select'].astype(str)
        )

        map_layout = go.Layout(
            geo={
                'scope': 'usa',
                'showlakes': True
            },
            title_text='COUNTY-LEVEL 3-YEAR +/- HEAT MAP FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            titlefont={
                'size': 8
            },
            margin={
                'r': 0,
                't': 20,
                'l': 0,
                'b': 0
            },
            template="plotly_dark",
            height=354
        )

        map_fig = go.Figure(data=map_data, layout=map_layout)

        totals_df_raw = filtered_share_df[['date', 'rig_count']].groupby('date').sum().reset_index()
        totals_df = totals_df_raw.rename(columns={'rig_count': 'overall_weekly_total'})

        drill_for_df = filtered_share_df[[
            'date',
            'drill_for',
            'rig_count'
        ]].groupby([
            'date',
            'drill_for'
        ]).sum().reset_index()

        drill_for_totals_df = drill_for_df.merge(totals_df, how='left', on='date')

        drill_for_totals_df['share'] = (
                    (drill_for_totals_df['rig_count']) / (drill_for_totals_df['overall_weekly_total']))

        drill_for_data = [
            go.Scatter(
                name=i[:4],
                x=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['date'],
                y=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['share'],
                hovertemplate='%{x}<br>' + i + '<br>%{y}'
            ) for i in drill_for_totals_df['drill_for'].unique()
        ]

        drill_for_layout = go.Layout(
            title_text='3Y DRILL-FOR HISTORY',
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': True,
                'tickformat': ',.0%',
                'tickfont': {
                    'size': 8
                }
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            showlegend=False,
        )

        drill_for_fig = go.Figure(data=drill_for_data, layout=drill_for_layout)

        well_depth_df = filtered_share_df[[
            'date',
            'well_depth',
            'rig_count'
        ]].groupby([
            'date',
            'well_depth'
        ]).sum().reset_index()

        well_depth_totals_df = well_depth_df.merge(totals_df, how='left', on='date')

        well_depth_totals_df['share'] = (
                (well_depth_totals_df['rig_count']) / (well_depth_totals_df['overall_weekly_total'])
        )

        well_depth_data = [
            go.Scatter(
                name=i[:4],
                x=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['date'],
                y=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['share'],
                hovertemplate='%{x}<br>' + i + '<br>%{y}'
            ) for i in well_depth_totals_df['well_depth'].unique()
        ]

        well_depth_layout = go.Layout(
            title_text='3Y WELL-DEPTH HISTORY',
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': True,
                'tickformat': ',.0%',
                'tickfont': {
                    'size': 8
                }
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            showlegend=False,
        )

        well_depth_fig = go.Figure(data=well_depth_data, layout=well_depth_layout)

        trajectory_df = filtered_share_df[[
            'date',
            'trajectory',
            'rig_count'
        ]].groupby([
            'date',
            'trajectory'
        ]).sum().reset_index()

        trajectory_totals_df = trajectory_df.merge(totals_df, how='left', on='date')

        trajectory_totals_df['share'] = (
                (trajectory_totals_df['rig_count']) / (trajectory_totals_df['overall_weekly_total']))

        trajectory_data = [
            go.Scatter(
                name=i[:4],
                x=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['date'],
                y=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['share'],
                hovertemplate='%{x}<br>' + i + '<br>%{y}'
            ) for i in trajectory_totals_df['trajectory'].unique()
        ]

        trajectory_layout = go.Layout(
            title_text='3Y TRAJECTORY HISTORY',
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': True,
                'tickformat': ',.0%',
                'tickfont': {
                    'size': 8
                }
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            showlegend=False,
        )

        trajectory_fig = go.Figure(data=trajectory_data, layout=trajectory_layout)

        #### rankings by state section ######

        state_table_df_raw = current_df[[
            'state', 'rig_count'
        ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})

        state_table_df_ref_raw = reference_df[[
            'state', 'rig_count'
        ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})

        state_table_df = state_table_df_raw.merge(
            state_table_df_ref_raw,
            'outer',
            ['state']
        )

        state_table_df['rig_count_after'] = state_table_df['rig_count_after'].fillna(0)
        state_table_df['rig_count_before'] = state_table_df['rig_count_before'].fillna(0)

        state_table_df['rig_count_after'] = state_table_df['rig_count_after'].astype(int)
        state_table_df['rig_count_before'] = state_table_df['rig_count_before'].astype(int)

        state_table_df['difference'] = state_table_df['rig_count_after'] - state_table_df['rig_count_before']

        state_table_df['rank'] = state_table_df['difference'].rank(method='min', ascending=False)

        state_table_df_sort = state_table_df.sort_values(
            by=['difference', 'rig_count_after'],
            ascending=[False, False]
        )

        state_final_table_df = pd.DataFrame({
            'RANK': [int(x) for x in state_table_df_sort['rank'].tolist()],
            'STATE': state_table_df_sort['state'].tolist(),
            'RIGS': state_table_df_sort['rig_count_after'].tolist(),
            '+/-': state_table_df_sort['difference'].tolist()
        })

        state_table_columns = [{
            'name': i, 'id': i
        } for i in state_final_table_df.columns]

        state_table_data = state_final_table_df.to_dict('records')

        #### rankings by basin section ######

        basin_table_df_raw = current_df[[
            'basin', 'rig_count'
        ]].groupby(['basin']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})

        basin_table_df_ref_raw = reference_df[[
            'basin', 'rig_count'
        ]].groupby(['basin']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})

        basin_table_df = basin_table_df_raw.merge(
            basin_table_df_ref_raw,
            'outer',
            ['basin']
        )

        basin_table_df['rig_count_after'] = basin_table_df['rig_count_after'].fillna(0)
        basin_table_df['rig_count_before'] = basin_table_df['rig_count_before'].fillna(0)

        basin_table_df['rig_count_after'] = basin_table_df['rig_count_after'].astype(int)
        basin_table_df['rig_count_before'] = basin_table_df['rig_count_before'].astype(int)

        basin_table_df['difference'] = basin_table_df['rig_count_after'] - basin_table_df['rig_count_before']

        basin_table_df['rank'] = basin_table_df['difference'].rank(method='min', ascending=False)

        basin_table_df_sort = basin_table_df.sort_values(
            by=['difference', 'rig_count_after'],
            ascending=[False, False]
        )

        basin_final_table_df = pd.DataFrame({
            'RANK': [int(x) for x in basin_table_df_sort['rank'].tolist()],
            'BASIN': basin_table_df_sort['basin'].tolist(),
            'RIGS': basin_table_df_sort['rig_count_after'].tolist(),
            '+/-': basin_table_df_sort['difference'].tolist()
        })

        basin_table_columns = [{
            'name': i, 'id': i
        } for i in basin_final_table_df.columns]

        basin_table_data = basin_final_table_df.to_dict('records')

        #### rankings by county section ######

        county_table_df_raw = current_df[[
            'county', 'rig_count'
        ]].groupby(['county']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})

        county_table_df_ref_raw = reference_df[[
            'county', 'rig_count'
        ]].groupby(['county']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})

        county_table_df = county_table_df_raw.merge(
            county_table_df_ref_raw,
            'outer',
            ['county']
        )

        county_table_df['rig_count_after'] = county_table_df['rig_count_after'].fillna(0)
        county_table_df['rig_count_before'] = county_table_df['rig_count_before'].fillna(0)

        county_table_df['rig_count_after'] = county_table_df['rig_count_after'].astype(int)
        county_table_df['rig_count_before'] = county_table_df['rig_count_before'].astype(int)

        county_table_df['difference'] = county_table_df['rig_count_after'] - county_table_df['rig_count_before']

        county_table_df['rank'] = county_table_df['difference'].rank(method='min', ascending=False)

        county_table_df_sort = county_table_df.sort_values(
            by=['difference', 'rig_count_after'],
            ascending=[False, False]
        )

        county_final_table_df = pd.DataFrame({
            'RANK': [int(x) for x in county_table_df_sort['rank'].tolist()],
            'COUNTY': county_table_df_sort['county'].tolist(),
            'RIGS': county_table_df_sort['rig_count_after'].tolist(),
            '+/-': county_table_df_sort['difference'].tolist()
        })

        county_table_columns = [{
            'name': i, 'id': i
        } for i in county_final_table_df.columns]

        county_table_data = county_final_table_df.to_dict('records')

        return indicator_fig, county_indicator_fig, map_fig, \
               drill_for_fig, well_depth_fig, trajectory_fig, \
               state_table_columns, state_table_data, basin_table_columns, basin_table_data, \
               county_table_columns, county_table_data


    else:
        reference_date = five_year_date
        scatter_reference_date = reference_date

        df = functions.get_df(scatter_reference_date, date)

        share_df = functions.get_df(reference_date, date)

        filtered_df = df[
            df['state'].isin(states) &
            df['basin'].isin(basins) &
            df['drill_for'].isin(drill_for) &
            df['location'].isin(locations) &
            df['trajectory'].isin(trajectories) &
            df['well_depth'].isin(well_depths)
        ]

        filtered_share_df = share_df[
            share_df['state'].isin(states) &
            share_df['basin'].isin(basins) &
            share_df['drill_for'].isin(drill_for) &
            share_df['location'].isin(locations) &
            share_df['trajectory'].isin(trajectories) &
            share_df['well_depth'].isin(well_depths)
        ]


        current_df = filtered_df[filtered_df['date'] == date]
        reference_df = filtered_df[filtered_df['date'] == reference_date]

        scatter_df = filtered_df[['date', 'rig_count']].groupby('date').sum().reset_index()

        county_scatter_df = filtered_df[['date', 'county']].groupby(['date'])['county'].nunique().reset_index()

        indicator_data = [
            go.Indicator(
                mode='number+delta',
                value=current_df['rig_count'].sum(),
                delta={'reference': reference_df['rig_count'].sum()},
            ),
            go.Scatter(
                name='1-YEAR TREND',
                x=scatter_df['date'].tolist(),
                y=scatter_df['rig_count'].tolist()
            )
        ]

        indicator_layout = go.Layout(
            title_text='RIG COUNT AND TRENDS FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': False
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            height=177
        )

        indicator_fig = go.Figure(data=indicator_data, layout=indicator_layout)

        county_indicator_data = [
            go.Indicator(
                mode='number+delta',
                value=current_df['county'].nunique(),
                delta={'reference': reference_df['county'].nunique()},
            ),
            go.Scatter(
                name='1-YEAR TREND',
                x=county_scatter_df['date'].tolist(),
                y=county_scatter_df['county'].tolist()
            )
        ]

        county_indicator_layout = go.Layout(
            # title='COGS',
            # height=100,
            title_text='COUNTY COUNT AND TRENDS FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': False
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            height=177
        )

        county_indicator_fig = go.Figure(data=county_indicator_data, layout=county_indicator_layout)

        with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
            counties = json.load(response)

        selected_week_df_raw = current_df[[
            'fips', 'county', 'rig_count'
        ]].groupby(['fips', 'county']).sum().reset_index()

        selected_week_df = selected_week_df_raw.rename(columns={'rig_count': 'rig_count_select'})

        ref_week_df_raw = reference_df[[
            'fips', 'county', 'rig_count'
        ]].groupby(['fips', 'county']).sum().reset_index()

        ref_week_df = ref_week_df_raw.rename(columns={'rig_count': 'rig_count_ref'})

        map_df = selected_week_df.merge(ref_week_df, 'outer', ['fips', 'county'])

        map_df['rig_count_ref'] = map_df['rig_count_ref'].fillna(0)
        map_df['rig_count_select'] = map_df['rig_count_select'].fillna(0)

        map_df['rig_count_ref'] = map_df['rig_count_ref'].astype(int)
        map_df['rig_count_select'] = map_df['rig_count_select'].astype(int)

        map_df['difference'] = map_df['rig_count_select'] - map_df['rig_count_ref']

        map_data = go.Choropleth(
            name='Counties',
            geojson=counties,
            locations=map_df['fips'],
            z=map_df['difference'],
            zmid=0,
            colorscale=plus_minus_colorscale,
            hovertemplate=map_df['county'] + '<br>Rig +/-: %{z}<br>Rig Count: ' + map_df['rig_count_select'].astype(str)
        )

        map_layout = go.Layout(
            geo={
                'scope': 'usa',
                'showlakes': True
            },
            title_text='COUNTY-LEVEL 5-YEAR +/- HEAT MAP FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            titlefont={
                'size': 8
            },
            margin={
                'r': 0,
                't': 20,
                'l': 0,
                'b': 0
            },
            template="plotly_dark",
            height=354
        )

        map_fig = go.Figure(data=map_data, layout=map_layout)

        totals_df_raw = filtered_share_df[['date', 'rig_count']].groupby('date').sum().reset_index()
        totals_df = totals_df_raw.rename(columns={'rig_count': 'overall_weekly_total'})

        drill_for_df = filtered_share_df[[
            'date',
            'drill_for',
            'rig_count'
        ]].groupby([
            'date',
            'drill_for'
        ]).sum().reset_index()

        drill_for_totals_df = drill_for_df.merge(totals_df, how='left', on='date')

        drill_for_totals_df['share'] = (
                    (drill_for_totals_df['rig_count']) / (drill_for_totals_df['overall_weekly_total']))

        drill_for_data = [
            go.Scatter(
                name=i[:4],
                x=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['date'],
                y=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['share'],
                hovertemplate='%{x}<br>' + i + '<br>%{y}'
            ) for i in drill_for_totals_df['drill_for'].unique()
        ]

        drill_for_layout = go.Layout(
            title_text='5Y DRILL-FOR HISTORY',
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': True,
                'tickformat': ',.0%',
                'tickfont': {
                    'size': 8
                }
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            showlegend=False,
        )

        drill_for_fig = go.Figure(data=drill_for_data, layout=drill_for_layout)

        well_depth_df = filtered_share_df[[
            'date',
            'well_depth',
            'rig_count'
        ]].groupby([
            'date',
            'well_depth'
        ]).sum().reset_index()

        well_depth_totals_df = well_depth_df.merge(totals_df, how='left', on='date')

        well_depth_totals_df['share'] = (
                (well_depth_totals_df['rig_count']) / (well_depth_totals_df['overall_weekly_total'])
        )

        well_depth_data = [
            go.Scatter(
                name=i[:4],
                x=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['date'],
                y=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['share'],
                hovertemplate='%{x}<br>' + i + '<br>%{y}'
            ) for i in well_depth_totals_df['well_depth'].unique()
        ]

        well_depth_layout = go.Layout(
            title_text='5Y WELL-DEPTH HISTORY',
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': True,
                'tickformat': ',.0%',
                'tickfont': {
                    'size': 8
                }
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            showlegend=False,
        )

        well_depth_fig = go.Figure(data=well_depth_data, layout=well_depth_layout)

        trajectory_df = filtered_share_df[[
            'date',
            'trajectory',
            'rig_count'
        ]].groupby([
            'date',
            'trajectory'
        ]).sum().reset_index()

        trajectory_totals_df = trajectory_df.merge(totals_df, how='left', on='date')

        trajectory_totals_df['share'] = (
                (trajectory_totals_df['rig_count']) / (trajectory_totals_df['overall_weekly_total']))

        trajectory_data = [
            go.Scatter(
                name=i[:4],
                x=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['date'],
                y=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['share'],
                hovertemplate='%{x}<br>' + i + '<br>%{y}'
            ) for i in trajectory_totals_df['trajectory'].unique()
        ]

        trajectory_layout = go.Layout(
            title_text='5Y TRAJECTORY HISTORY',
            titlefont={
                'size': 8
            },
            template="plotly_dark",
            xaxis={
                'showgrid': False,
                'showticklabels': False
            },
            yaxis={
                'showgrid': False,
                'showticklabels': True,
                'tickformat': ',.0%',
                'tickfont': {
                    'size': 8
                }
            },
            margin={
                't': 20,
                'r': 0,
                'b': 0,
                'l': 0
            },
            showlegend=False,
        )

        trajectory_fig = go.Figure(data=trajectory_data, layout=trajectory_layout)

        #### rankings by state section ######

        state_table_df_raw = current_df[[
            'state', 'rig_count'
        ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})

        state_table_df_ref_raw = reference_df[[
            'state', 'rig_count'
        ]].groupby(['state']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})

        state_table_df = state_table_df_raw.merge(
            state_table_df_ref_raw,
            'outer',
            ['state']
        )

        state_table_df['rig_count_after'] = state_table_df['rig_count_after'].fillna(0)
        state_table_df['rig_count_before'] = state_table_df['rig_count_before'].fillna(0)

        state_table_df['rig_count_after'] = state_table_df['rig_count_after'].astype(int)
        state_table_df['rig_count_before'] = state_table_df['rig_count_before'].astype(int)

        state_table_df['difference'] = state_table_df['rig_count_after'] - state_table_df['rig_count_before']

        state_table_df['rank'] = state_table_df['difference'].rank(method='min', ascending=False)

        state_table_df_sort = state_table_df.sort_values(
            by=['difference', 'rig_count_after'],
            ascending=[False, False]
        )

        state_final_table_df = pd.DataFrame({
            'RANK': [int(x) for x in state_table_df_sort['rank'].tolist()],
            'STATE': state_table_df_sort['state'].tolist(),
            'RIGS': state_table_df_sort['rig_count_after'].tolist(),
            '+/-': state_table_df_sort['difference'].tolist()
        })

        state_table_columns = [{
            'name': i, 'id': i
        } for i in state_final_table_df.columns]

        state_table_data = state_final_table_df.to_dict('records')

        #### rankings by basin section ######

        basin_table_df_raw = current_df[[
            'basin', 'rig_count'
        ]].groupby(['basin']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})

        basin_table_df_ref_raw = reference_df[[
            'basin', 'rig_count'
        ]].groupby(['basin']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})

        basin_table_df = basin_table_df_raw.merge(
            basin_table_df_ref_raw,
            'outer',
            ['basin']
        )

        basin_table_df['rig_count_after'] = basin_table_df['rig_count_after'].fillna(0)
        basin_table_df['rig_count_before'] = basin_table_df['rig_count_before'].fillna(0)

        basin_table_df['rig_count_after'] = basin_table_df['rig_count_after'].astype(int)
        basin_table_df['rig_count_before'] = basin_table_df['rig_count_before'].astype(int)

        basin_table_df['difference'] = basin_table_df['rig_count_after'] - basin_table_df['rig_count_before']

        basin_table_df['rank'] = basin_table_df['difference'].rank(method='min', ascending=False)

        basin_table_df_sort = basin_table_df.sort_values(
            by=['difference', 'rig_count_after'],
            ascending=[False, False]
        )

        basin_final_table_df = pd.DataFrame({
            'RANK': [int(x) for x in basin_table_df_sort['rank'].tolist()],
            'BASIN': basin_table_df_sort['basin'].tolist(),
            'RIGS': basin_table_df_sort['rig_count_after'].tolist(),
            '+/-': basin_table_df_sort['difference'].tolist()
        })

        basin_table_columns = [{
            'name': i, 'id': i
        } for i in basin_final_table_df.columns]

        basin_table_data = basin_final_table_df.to_dict('records')

        #### rankings by county section ######

        county_table_df_raw = current_df[[
            'county', 'rig_count'
        ]].groupby(['county']).sum().reset_index().rename(columns={'rig_count': 'rig_count_after'})

        county_table_df_ref_raw = reference_df[[
            'county', 'rig_count'
        ]].groupby(['county']).sum().reset_index().rename(columns={'rig_count': 'rig_count_before'})

        county_table_df = county_table_df_raw.merge(
            county_table_df_ref_raw,
            'outer',
            ['county']
        )

        county_table_df['rig_count_after'] = county_table_df['rig_count_after'].fillna(0)
        county_table_df['rig_count_before'] = county_table_df['rig_count_before'].fillna(0)

        county_table_df['rig_count_after'] = county_table_df['rig_count_after'].astype(int)
        county_table_df['rig_count_before'] = county_table_df['rig_count_before'].astype(int)

        county_table_df['difference'] = county_table_df['rig_count_after'] - county_table_df['rig_count_before']

        county_table_df['rank'] = county_table_df['difference'].rank(method='min', ascending=False)

        county_table_df_sort = county_table_df.sort_values(
            by=['difference', 'rig_count_after'],
            ascending=[False, False]
        )

        county_final_table_df = pd.DataFrame({
            'RANK': [int(x) for x in county_table_df_sort['rank'].tolist()],
            'COUNTY': county_table_df_sort['county'].tolist(),
            'RIGS': county_table_df_sort['rig_count_after'].tolist(),
            '+/-': county_table_df_sort['difference'].tolist()
        })

        county_table_columns = [{
            'name': i, 'id': i
        } for i in county_final_table_df.columns]

        county_table_data = county_final_table_df.to_dict('records')

        return indicator_fig, county_indicator_fig, map_fig, \
               drill_for_fig, well_depth_fig, trajectory_fig, \
               state_table_columns, state_table_data, basin_table_columns, basin_table_data, \
               county_table_columns, county_table_data


# if __name__ == '__main__':
#     app.run_server(host='0.0.0.0', port=8050, debug=True)