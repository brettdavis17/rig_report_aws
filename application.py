import json
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import dash_table
import pandas as pd
from urllib.request import urlopen
from dateutil.relativedelta import relativedelta
import functions

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css'
]

app = dash.Dash(
    __name__
    # external_stylesheets=external_stylesheets
)
server = app.server

app.config['suppress_callback_exceptions'] = True

app.layout = html.Div([
    #header
    html.Div([
        html.H2('USA LAND RIG DASHBOARD')
    ], className='header'
    ),
    #dropdowns
    html.Div([
        html.Div([
            html.Button(
                'SUBMIT',
                id='submit-button'
            ),
            dcc.Dropdown(
                id='date-dropdown',
                options=[{'label': x, 'value': x} for x in functions.get_date_list()],
                multi=False,
                value=functions.get_date_list()[0],
                placeholder='Select a date',
                persistence=True
            ),
            html.Details([
                html.Summary('States'),
                html.Div([
                    dcc.Checklist(
                        id='state-checklist',
                        options=[{'label': x, 'value': x} for x in functions.get_state_list()],
                        value=functions.get_state_list(),
                        persistence=True
                    )
                ])
            ]),
            html.Details([
                html.Summary('Basins'),
                html.Div([
                    dcc.Checklist(
                        id='basin-checklist',
                        options=[{'label': x, 'value': x} for x in functions.get_basin_list()],
                        value=functions.get_basin_list(),
                        persistence=True
                    )
                ])
            ]),
            html.Details([
                html.Summary('Drill For'),
                html.Div([
                    dcc.Checklist(
                        id='drill-for-checklist',
                        options=[{'label': x, 'value': x} for x in functions.get_drill_for_list()],
                        value=functions.get_drill_for_list(),
                        persistence=True
                    )
                ])
            ]),
            html.Details([
                html.Summary('Location'),
                html.Div([
                    dcc.Checklist(
                        id='location-checklist',
                        options=[{'label': x, 'value': x} for x in functions.get_location_list()],
                        value=functions.get_location_list(),
                        persistence=True
                    )
                ])
            ]),
            html.Details([
                html.Summary('Trajectory'),
                html.Div([
                    dcc.Checklist(
                        id='trajectory-checklist',
                        options=[{'label': x, 'value': x} for x in functions.get_trajectory_list()],
                        value=functions.get_trajectory_list(),
                        persistence=True
                    )
                ])
            ]),
            html.Details([
                html.Summary('Well Depth'),
                html.Div([
                    dcc.Checklist(
                        id='well-depth-checklist',
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
                    dcc.Graph(
                        id='indicator'
                    )
                ], className='graph_container six columns'
                ),
                html.Div([
                    dcc.Graph(
                        id='county-indicator'
                    )
                ], className='graph_container six columns'
                )
            ], className='twelve columns'
            ),
            html.Div([
                html.Div([
                    dash_table.DataTable(
                        id='state-table',
                        style_cell={
                            'textAlign': 'left'
                        }
                        # fixed_rows={
                        #     'headers': True,
                        #     'data': 0
                        # }
                    )
                ], className='graph_container four columns', style={'maxHeight': '300px', 'overflow': 'scroll'}
                ),
                html.Div([
                    dash_table.DataTable(
                        id='basin-table',
                        style_cell={
                            'textAlign': 'left'
                        }
                        # fixed_rows={
                        #     'headers': True,
                        #     'data': 0
                        # }
                    )
                ], className='graph_container four columns', style={'maxHeight': '300px', 'overflow': 'scroll'}
                ),
                html.Div([
                    dash_table.DataTable(
                        id='county-table',
                        style_cell={
                            'textAlign': 'left'
                        }
                        # fixed_rows={
                        #     'headers': True,
                        #     'data': 0
                        # }
                    )
                ], className='graph_container four columns', style={'maxHeight': '300px', 'overflow': 'scroll'}
                )
                # html.Div([
                #     dcc.Graph(
                #         id='basin-table'
                #     )
                # ], className='graph_container four columns'
                # ),
                # html.Div([
                #     dcc.Graph(
                #         id='county-table'
                #     )
                # ], className='graph_container four columns'
                # )
            ], className='twelve columns'
            ),
            html.Div([
                html.Div([
                    dcc.Graph(
                        id='rig-map'
                    )
                ], className='graph_container twelve columns'
                ),
            ], className='twelve columns'
            ),
            html.Div([
                html.Div([
                    dcc.Graph(
                        id='drill-for-pie'
                    )
                ], className='graph_container five columns'
                ),
                html.Div([
                    dcc.Graph(
                        id='drill-for-scatter'
                    )
                ], className='graph_container seven columns'
                ),
            ], className='twelve columns'
            ),
            html.Div([
                html.Div([
                    dcc.Graph(
                        id='depth-pie'
                    )
                ], className='graph_container five columns'
                ),
                html.Div([
                    dcc.Graph(
                        id='depth-scatter'
                    )
                ], className='graph_container seven columns'
                )
            ], className='twelve columns'
            ),
            html.Div([
                html.Div([
                    dcc.Graph(
                        id='trajectory-pie'
                    )
                ], className='graph_container five columns'
                ),
                html.Div([
                    dcc.Graph(
                        id='trajectory-scatter'
                    )
                ], className='graph_container seven columns'
                )
            ], className='twelve columns'
            ),
            html.Div([
                html.Div([
                    html.Button(
                        'SUBMIT',
                        id='stack-graph-button'
                    )
                ], className='two columns'
                ),
                html.Div([
                    dcc.RadioItems(
                        id='stack-radio',
                        options=[
                            {'label': 'States', 'value': 'state'},
                            {'label': 'Basins', 'value': 'basin'},
                            {'label': 'Counties', 'value': 'county'},
                            {'label': 'Drill For', 'value': 'drill_for'},
                            {'label': 'Trajectory', 'value': 'trajectory'},
                            {'label': 'Well Depth', 'value': 'well_depth'}
                        ],
                        value='basin',
                        labelStyle={
                            'display': 'inline-block'
                        },
                        persistence=True
                    )
                ], className='ten columns'
                ),
            ], className='twelve columns'
            ),
            html.Div([
                html.Div([
                    dcc.Graph(
                        id='stack-graph'
                    )
                ], className='twelve columns graph_container'
                )
            ], className='twelve columns'
            )
        ], className='ten columns'
        )
    ], className='twelve columns'
    )
]
)

convert_dict = {'date': str}
master_df = functions.get_overall_master_df().astype(convert_dict)


@app.callback(
    [
        Output(
            'indicator',
            'figure'
        ),
        Output(
            'county-indicator',
            'figure'
        ),
        Output(
            'state-table',
            'columns'
        ),
        Output(
            'state-table',
            'data'
        ),
        Output(
            'basin-table',
            'columns'
        ),
        Output(
            'basin-table',
            'data'
        ),
        Output(
            'county-table',
            'columns'
        ),
        Output(
            'county-table',
            'data'
        ),
        Output(
            'rig-map',
            'figure'
        ),
        Output(
            'drill-for-pie',
            'figure'
        ),
        Output(
            'drill-for-scatter',
            'figure'
        ),
        Output(
            'depth-pie',
            'figure'
        ),
        Output(
            'depth-scatter',
            'figure'
        ),
        Output(
            'trajectory-pie',
            'figure'
        ),
        Output(
            'trajectory-scatter',
            'figure'
        )
    ],
    [
        Input(
            'submit-button',
            'n_clicks'
        )
    ],
    [
        State(
            'date-dropdown',
            'value'
        ),
        State(
            'state-checklist',
            'value'
        ),
        State(
            'basin-checklist',
            'value'
        ),
        State(
            'drill-for-checklist',
            'value'
        ),
        State(
            'location-checklist',
            'value'
        ),
        State(
            'trajectory-checklist',
            'value'
        ),
        State(
            'well-depth-checklist',
            'value'
        )
    ]
)
def return_outputs(click, date, states, basins, drill_for, locations, trajectories, well_depths):

    # one_year_df = functions.get_one_year_df(date)

    current_df = master_df[master_df['date'] == date]

    date_list = master_df['date'].unique().tolist()

    delta_date = date_list[date_list.index(date) - 1]

    indicator_df = current_df[
        current_df['state'].isin(states) &
        current_df['basin'].isin(basins) &
        current_df['drill_for'].isin(drill_for) &
        current_df['location'].isin(locations) &
        current_df['trajectory'].isin(trajectories) &
        current_df['well_depth'].isin(well_depths)
    ]

    current_minus_1_df = master_df[master_df['date'] == delta_date]

    delta_df = current_minus_1_df[
        current_minus_1_df['state'].isin(states) &
        current_minus_1_df['basin'].isin(basins) &
        current_minus_1_df['drill_for'].isin(drill_for) &
        current_minus_1_df['location'].isin(locations) &
        current_minus_1_df['trajectory'].isin(trajectories) &
        current_minus_1_df['well_depth'].isin(well_depths)
        ]

    one_year_df = master_df[(master_df['date'] >= str(int(date[:4]) -1 ) + date[4:]) & (master_df['date'] <= date)]

    scatter_df = one_year_df[
        one_year_df['state'].isin(states) &
        one_year_df['basin'].isin(basins) &
        one_year_df['drill_for'].isin(drill_for) &
        one_year_df['location'].isin(locations) &
        one_year_df['trajectory'].isin(trajectories) &
        one_year_df['well_depth'].isin(well_depths)
    ][[
        'date',
        'rig_count'
    ]].groupby('date').sum().reset_index()

    # scatter_df = one_year_df[['date', 'rig_count']].groupby('date').sum().reset_index()

    scatter_y_values = scatter_df['rig_count'].tolist()

    scatter_x_values = scatter_df['date'].tolist()

    indicator_fig = {
        'data': [
            go.Indicator(
                mode='number+delta',
                value=indicator_df['rig_count'].sum(),
                delta={'reference':delta_df['rig_count'].sum()},
                number={
                    'font': {
                        'size': 48
                    }
                }
            ),
            go.Scatter(
                name='1-YEAR TREND',
                x=scatter_x_values,
                y=scatter_y_values
            )
        ],
        'layout': go.Layout(
            # title='COGS',
            # height=100,
            paper_bgcolor='white',
            title_text='RIG COUNT AND TRENDS<br>FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4]
        )
    }

    # county_count_scatter = scatter_df.groupby(['date'])['county'].nunique().reset_index()

    county_count_scatter = one_year_df[
        one_year_df['state'].isin(states) &
        one_year_df['basin'].isin(basins) &
        one_year_df['drill_for'].isin(drill_for) &
        one_year_df['location'].isin(locations) &
        one_year_df['trajectory'].isin(trajectories) &
        one_year_df['well_depth'].isin(well_depths)
    ][[
        'date',
        'county'
    ]].groupby(['date'])['county'].nunique().reset_index()

    county_indicator_fig = {
        'data': [
            go.Indicator(
                mode='number+delta',
                value=indicator_df['county'].nunique(),
                delta={'reference': delta_df['county'].nunique()},
                number={
                    'font': {
                        'size': 48
                    }
                }
            ),
            go.Scatter(
                name='1-YEAR TREND',
                x=county_count_scatter['date'].tolist(),
                y=county_count_scatter['county'].tolist()
            )
        ],
        'layout': go.Layout(
            # title='COGS',
            # height=100,
            paper_bgcolor='white',
            title_text='COUNTY COUNT AND TRENDS<br>FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4]
        )
    }

    state_raw_table_df = indicator_df[['state', 'rig_count']].groupby(['state']).sum().reset_index()

    state_table_df = state_raw_table_df.sort_values(by=['rig_count'], ascending=False)

    state_table_df['rank'] = state_table_df['rig_count'].rank(method='min', ascending=False)

    state_final_table_df = pd.DataFrame({
        'RANK': [int(x) for x in state_table_df['rank'].tolist()],
        'STATE': state_table_df['state'].tolist(),
        'RIGS': state_table_df['rig_count'].tolist()
    })

    state_table_columns = [{
        'name': i, 'id': i
    } for i in state_final_table_df.columns]

    state_table_data = state_final_table_df.to_dict('records')

    state_table_fig = {
        'data': [
            go.Table(
                header={
                    'values': state_final_table_df.columns.tolist(),
                    'font': {
                        'size': 10
                    },
                    'align': 'left'
                },
                cells={
                    'values': [state_final_table_df[k].tolist() for k in state_final_table_df.columns],
                    'align': 'left',
                    'font': {
                        'size': 8
                    }
                }
            )
        ],
        'layout': go.Layout(
            title='RIG COUNT RANKING BY STATE<br>FOR ' + date
        )
    }

    basin_raw_table_df = indicator_df[['basin', 'rig_count']].groupby(['basin']).sum().reset_index()

    basin_table_df = basin_raw_table_df.sort_values(by=['rig_count'], ascending=False)

    basin_table_df['rank'] = basin_table_df['rig_count'].rank(method='min', ascending=False)

    basin_final_table_df = pd.DataFrame({
        'RANK': [int(x) for x in basin_table_df['rank'].tolist()],
        'BASIN': basin_table_df['basin'].tolist(),
        'RIGS': basin_table_df['rig_count'].tolist()
    })

    basin_table_columns = [{
        'name': i, 'id': i
    } for i in basin_final_table_df.columns]

    basin_table_data = basin_final_table_df.to_dict('records')

    # basin_table_fig = {
    #     'data': [
    #         go.Table(
    #             header={
    #                 'values': basin_final_table_df.columns.tolist(),
    #                 'font': {
    #                     'size': 10
    #                 },
    #                 'align': 'left'
    #             },
    #             cells={
    #                 'values': [basin_final_table_df[k].tolist() for k in basin_final_table_df.columns],
    #                 'align': 'left',
    #                 'font': {
    #                     'size': 8
    #                 }
    #             }
    #         )
    #     ],
    #     'layout': go.Layout(
    #         title='RIG COUNT RANKING BY BASIN<br>FOR ' + date
    #     )
    # }

    county_raw_table_df = indicator_df[['county', 'rig_count']].groupby(['county']).sum().reset_index()

    county_table_df = county_raw_table_df.sort_values(by=['rig_count'], ascending=False)

    county_table_df['rank'] = county_table_df['rig_count'].rank(method='min', ascending=False)

    county_final_table_df = pd.DataFrame({
        'RANK': [int(x) for x in county_table_df['rank'].tolist()],
        'COUNTY': county_table_df['county'].tolist(),
        'RIGS': county_table_df['rig_count'].tolist()
    })

    county_table_columns = [{
        'name': i, 'id': i
    } for i in county_final_table_df.columns]

    county_table_data = county_final_table_df.to_dict('records')

    # county_table_fig = {
    #     'data': [
    #         go.Table(
    #             header={
    #                 'values': county_final_table_df.columns.tolist(),
    #                 'font': {
    #                     'size': 10
    #                 },
    #                 'align': 'left'
    #             },
    #             cells={
    #                 'values': [county_final_table_df[k].tolist() for k in county_final_table_df.columns],
    #                 'align': 'left',
    #                 'font': {
    #                     'size': 8
    #                 }
    #             }
    #         )
    #     ],
    #     'layout': go.Layout(
    #         title='RIG COUNT RANKING BY COUNTY<br>FOR ' + date
    #     )
    # }

    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)

    map_df = indicator_df[['fips', 'county', 'rig_count']].groupby(['fips', 'county']).sum().reset_index()

    map_fig = {
        'data': [
            go.Choropleth(
                geojson=counties,
                locations=map_df['fips'],
                z=map_df['rig_count'],
                colorscale='Oranges',
                hovertemplate=map_df['county'] + '<br>Rigs: %{z}'
            )
        ],
        'layout': go.Layout(
            geo={
                'scope':'usa',
                'showlakes':True
            },
            title_text='COUNTY-LEVEL HEAT MAP FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4],
            margin={
                'r': 0,
                't': 0,
                'l': 0,
                'b': 0
            }
        )
    }

    drill_for_df = indicator_df[['drill_for', 'rig_count']].groupby('drill_for').sum().reset_index()

    drill_for_pie_fig = {
        'data': [
            go.Pie(
                labels=drill_for_df['drill_for'].tolist(),
                values=drill_for_df['rig_count'].tolist(),
            )
        ],
        'layout': go.Layout(
            title_text='SHARE OF DRILL-FOR<br>FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4]
        )
    }

    # df = functions.get_share_drill_for_df()
    # df['share'] = (df['rig_count'] / df['overall_weekly_rig_count'])

    filtered_overall_master_df = master_df[
        master_df['state'].isin(states) &
        master_df['basin'].isin(basins) &
        master_df['drill_for'].isin(drill_for) &
        master_df['location'].isin(locations) &
        master_df['trajectory'].isin(trajectories) &
        master_df['well_depth'].isin(well_depths)
        ]

    totals_df = filtered_overall_master_df[['date', 'rig_count']].groupby('date').sum().reset_index()
    totals_rename_df = totals_df.rename(columns={'rig_count': 'overall_weekly_total'})

    drill_for_df = filtered_overall_master_df[[
        'date',
        'drill_for',
        'rig_count'
    ]].groupby([
        'date',
        'drill_for'
    ]).sum().reset_index()

    drill_for_totals_df = drill_for_df.merge(totals_rename_df, how='left', on='date')

    drill_for_totals_df['share'] = ((drill_for_totals_df['rig_count']) / (drill_for_totals_df['overall_weekly_total']))
    max_share = drill_for_totals_df['share'].max()

    drill_for_scatter_fig = {
        'data': [
            go.Scatter(
                name=i,
                x=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['date'],
                y=drill_for_totals_df[drill_for_totals_df['drill_for'] == i]['share']
            ) for i in drill_for_totals_df['drill_for'].unique()
        ],
        'layout': go.Layout(
            title_text='SHARE OF DRILL-FOR HISTORY',
            shapes=[{
                'type': 'line',
                'xref': 'x',
                'yref': 'y',
                'x0': date,
                'y0': 0,
                'x1': date,
                'y1': max_share
            }]
        )
    }

    drill_for_df = indicator_df[['well_depth', 'rig_count']].groupby('well_depth').sum().reset_index()

    well_depth_pie_fig = {
        'data': [
            go.Pie(
                labels=drill_for_df['well_depth'].tolist(),
                values=drill_for_df['rig_count'].tolist(),
            )
        ],
        'layout': go.Layout(
            title_text='SHARE OF WELL-DEPTH<br>' + date[5:7] + '-' + date[8:] + '-' + date[:4]
        )
    }

    # df = functions.get_share_well_depth_df()
    # df['share'] = (df['rig_count'] / df['overall_weekly_rig_count'])
    # max_share = df['share'].max()

    totals_df = filtered_overall_master_df[['date', 'rig_count']].groupby('date').sum().reset_index()
    totals_rename_df = totals_df.rename(columns={'rig_count': 'overall_weekly_total'})

    well_depth_df = filtered_overall_master_df[[
        'date',
        'well_depth',
        'rig_count'
    ]].groupby([
        'date',
        'well_depth'
    ]).sum().reset_index()

    well_depth_totals_df = well_depth_df.merge(totals_rename_df, how='left', on='date')

    well_depth_totals_df['share'] = ((well_depth_totals_df['rig_count']) / (well_depth_totals_df['overall_weekly_total']))
    max_share = well_depth_totals_df['share'].max()

    well_depth_scatter_fig = {
        'data': [
            go.Scatter(
                name=i,
                x=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['date'],
                y=well_depth_totals_df[well_depth_totals_df['well_depth'] == i]['share']
            ) for i in well_depth_totals_df['well_depth'].unique()
        ],
        'layout': go.Layout(
            title_text='SHARE OF WELL-DEPTH HISTORY',
            shapes=[{
                'type': 'line',
                'xref': 'x',
                'yref': 'y',
                'x0': date,
                'y0': 0,
                'x1': date,
                'y1': max_share
            }]
        )
    }

    trajectory_df = indicator_df[['trajectory', 'rig_count']].groupby('trajectory').sum().reset_index()

    trajectory_pie_fig = {
        'data': [
            go.Pie(
                labels=trajectory_df['trajectory'].tolist(),
                values=trajectory_df['rig_count'].tolist(),
            )
        ],
        'layout': go.Layout(
            title_text='SHARE OF RIG TRAJECTORIES<br>FOR ' + date[5:7] + '-' + date[8:] + '-' + date[:4]
        )
    }

    # df = functions.get_share_trajectory_df()
    # df['share'] = (df['rig_count'] / df['overall_weekly_rig_count'])
    # max_share = df['share'].max()

    totals_df = filtered_overall_master_df[['date', 'rig_count']].groupby('date').sum().reset_index()
    totals_rename_df = totals_df.rename(columns={'rig_count': 'overall_weekly_total'})

    trajectory_df = filtered_overall_master_df[[
        'date',
        'trajectory',
        'rig_count'
    ]].groupby([
        'date',
        'trajectory'
    ]).sum().reset_index()

    trajectory_totals_df = trajectory_df.merge(totals_rename_df, how='left', on='date')

    trajectory_totals_df['share'] = (
                (trajectory_totals_df['rig_count']) / (trajectory_totals_df['overall_weekly_total']))
    max_share = trajectory_totals_df['share'].max()

    trajectory_scatter_fig = {
        'data': [
            go.Scatter(
                name=i,
                x=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['date'],
                y=trajectory_totals_df[trajectory_totals_df['trajectory'] == i]['share']
            ) for i in trajectory_totals_df['trajectory'].unique()
        ],
        'layout': go.Layout(
            title_text='SHARE OF TRAJECTORY HISTORY',
            shapes=[{
                'type': 'line',
                'xref': 'x',
                'yref': 'y',
                'x0': date,
                'y0': 0,
                'x1': date,
                'y1': max_share
            }]
        )
    }

    return indicator_fig, county_indicator_fig, state_table_columns, state_table_data, basin_table_columns, \
           basin_table_data, county_table_columns, county_table_data, map_fig, drill_for_pie_fig, \
           drill_for_scatter_fig, well_depth_pie_fig, well_depth_scatter_fig, trajectory_pie_fig, \
           trajectory_scatter_fig

@app.callback(
    Output(
        'stack-graph',
        'figure'
    ),
    [
        Input(
            'stack-graph-button',
            'n_clicks'
        )
    ],
    [
        State(
            'stack-radio',
            'value'
        )
    ]
)
def return_stack_graph_outputs(click, radio):

    df = master_df[['date', radio, 'rig_count']]

    dff = df.groupby(['date', radio]).sum().reset_index()

    data = [{
        'type': 'scatter',
        'name': i,
        'x': dff[dff[radio] == i]['date'].tolist(),
        'y': dff[dff[radio] == i]['rig_count'].tolist(),
        'stackgroup': 'one'
    } for i in dff[radio].unique()
    ]

    layout = {
        'title': 'RIG COUNT HISTORY STACKED BY ' + radio.upper()
    }

    stack_fig = go.Figure(data=data, layout=layout)

    return stack_fig

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)