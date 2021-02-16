import psycopg2
import pandas as pd
from dateutil.relativedelta import relativedelta

DB_NAME = 'fpelltoe'
DB_USER = 'fpelltoe'
DB_PASS = 'MihevzwEYa3-L5FTM_IX7p51s2LXjdcv'
DB_HOST = 'lallah.db.elephantsql.com'
DB_PORT = '5432'

# conn = psycopg2.connect(
#     database=DB_NAME,
#     user=DB_USER,
#     password=DB_PASS,
#     host=DB_HOST,
#     port=DB_PORT
# )
#
# c = conn.cursor()

def get_date_list():

    conn = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )

    c = conn.cursor()

    sql = '''
        SELECT DISTINCT publish_date as date
        FROM new_main
        ORDER BY date DESC
    '''

    df = pd.read_sql(
        sql,
        conn
    )

    dates_list = df['date'].astype(str).to_list()

    # dates_list = df['date'].tolist()

    conn.close()

    return dates_list


def get_date_list_asc():

    conn = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )

    c = conn.cursor()

    sql = '''
        SELECT DISTINCT publish_date as date
        FROM new_main
        ORDER BY date ASC
    '''

    df = pd.read_sql(
        sql,
        conn
    )

    dates_list = df['date'].astype(str).to_list()

    # dates_list = df['date'].tolist()

    conn.close()

    return dates_list

date_list = get_date_list_asc()

def get_country_list():

    conn = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )

    c = conn.cursor()

    sql = '''
        SELECT DISTINCT country as country
        FROM new_main
        ORDER BY country
    '''

    df = pd.read_sql(
        sql,
        conn
    )

    country_list = df['country'].astype(str).to_list()

    conn.close()

    return country_list


def get_state_list():

    conn = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )

    c = conn.cursor()

    sql = '''
        SELECT DISTINCT state_or_province as state
        FROM new_main
        ORDER BY state
    '''

    df = pd.read_sql(
        sql,
        conn
    )

    states_list = df['state'].astype(str).to_list()

    conn.close()

    return states_list

def get_basin_list():

    conn = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )

    c = conn.cursor()

    sql = '''
            SELECT DISTINCT basin as basin
            FROM new_main
            ORDER BY basin
        '''

    df = pd.read_sql(
        sql,
        conn
    )

    basin_list = df['basin'].astype(str).to_list()

    conn.close()

    return basin_list

def get_drill_for_list():

    conn = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )

    c = conn.cursor()

    sql = '''
            SELECT DISTINCT drill_for as drill_for
            FROM new_main
            ORDER BY drill_for
        '''

    df = pd.read_sql(
        sql,
        conn
    )

    drill_for_list = df['drill_for'].astype(str).to_list()

    conn.close()

    return drill_for_list

def get_location_list():

    conn = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )

    c = conn.cursor()

    sql = '''
            SELECT DISTINCT location as location
            FROM new_main
            ORDER BY location
        '''

    df = pd.read_sql(
        sql,
        conn
    )

    location_list = df['location'].astype(str).to_list()

    conn.close()

    return location_list

def get_trajectory_list():

    conn = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )

    c = conn.cursor()

    sql = '''
            SELECT DISTINCT trajectory as trajectory
            FROM new_main
            ORDER BY trajectory
        '''

    df = pd.read_sql(
        sql,
        conn
    )

    trajectory_list = df['trajectory'].astype(str).to_list()

    conn.close()

    return trajectory_list

def get_well_depth_list():

    conn = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )

    c = conn.cursor()

    sql = '''
            SELECT DISTINCT well_depth as well_depth
            FROM new_main
            ORDER BY well_depth
        '''

    df = pd.read_sql(
        sql,
        conn
    )

    well_depth_list = df['well_depth'].astype(str).to_list()

    conn.close()

    return well_depth_list

def get_one_year_df(date):

    conn = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )

    sql = '''
        SELECT m.country as country, c.fips as fips, m.county_and_state as county, m.basin as basin,
            m.drill_for as drill_for, m.location as location, m.trajectory as trajectory, m.well_depth, 
            m.year as year, m.month as month, m.week as week, m.rig_count as rig_count, m.state_or_province as state,
            m.publish_date as date
        FROM new_main AS m
        LEFT JOIN counties_and_states_master AS c ON c.county_and_state = m.county_and_state
        WHERE publish_date >= '%s' AND publish_date <= '%s' AND location = 'Land' AND country = 'UNITED STATES'
        ORDER BY publish_date ASC
    '''

    sql_input = (str(int(date[:4]) - 1) + date[4:], date)

    final_sql = sql % sql_input

    df = pd.read_sql(
        final_sql,
        conn
    )

    conn.close()

    return df

def get_overall_master_df():

    conn = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )

    sql = '''
        SELECT c.fips as fips, m.county_and_state as county, m.basin as basin,
            m.drill_for as drill_for, m.location as location, m.trajectory as trajectory, m.well_depth, 
            m.rig_count as rig_count, m.state_or_province as state, m.publish_date as date
        FROM main AS m
        LEFT JOIN counties_and_states_master AS c ON c.county_and_state = m.county_and_state
        ORDER BY publish_date ASC
    '''

    df = pd.read_sql(
        sql,
        conn
    )

    conn.close()

    return df

def get_df(first_date, second_date):
    conn = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )

    sql = '''
        SELECT c.fips as fips, m.county_and_state as county, m.basin as basin,
            m.drill_for as drill_for, m.location as location, m.trajectory as trajectory, m.well_depth, 
            m.rig_count as rig_count, m.state_or_province as state, m.publish_date as date
        FROM new_main AS m
        LEFT JOIN counties_and_states_master AS c ON c.county_and_state = m.county_and_state
        WHERE publish_date >= ('%s') AND publish_date <= ('%s') and m.country = 'UNITED STATES'
        ORDER BY publish_date ASC
    '''

    sql_input = (first_date, second_date)

    final_sql = sql % sql_input

    df = pd.read_sql(final_sql, conn)

    conn.close()

    convert_dict = {'date': str}
    dff = df.astype(convert_dict)

    return dff


def get_north_america_df(first_date, second_date):
    conn = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )

    sql = '''
        SELECT country, state_or_province as state, basin, drill_for, location, trajectory, well_depth,
	        rig_count, publish_date as date
        FROM new_main
        WHERE publish_date >= ('%s') AND publish_date <= ('%s') AND 
            country IN ('UNITED STATES', 'CANADA')
        ORDER BY date ASC
    '''

    sql_input = (first_date, second_date)

    final_sql = sql % sql_input

    df = pd.read_sql(final_sql, conn)

    conn.close()

    convert_dict = {'date': str}
    dff = df.astype(convert_dict)

    return dff


def get_max_date():

    conn = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )

    sql = '''
        SELECT MAX(publish_date) as max
        FROM new_main
    '''

    df = pd.read_sql(sql, conn)

    conn.close()

    return df['max'][0]



def get_share_drill_for_df():

    conn = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )

    sql = '''
        SELECT m.publish_date, m.drill_for, m.rig_count, s.overall_weekly_rig_count
        FROM (
            SELECT publish_date, drill_for, SUM(rig_count) as rig_count
            FROM main
            GROUP BY publish_date, drill_for
        ) as m
        LEFT JOIN (
            SELECT publish_date, SUM(rig_count) as overall_weekly_rig_count
            FROM main
            GROUP BY publish_date
        ) as s
        ON s.publish_date = m.publish_date
        ORDER BY m.publish_date
    '''

    df = pd.read_sql(sql, conn)

    conn.close()

    return df

def get_share_well_depth_df():

    conn = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )

    sql = '''
        SELECT m.publish_date, m.well_depth, m.rig_count, s.overall_weekly_rig_count
        FROM (
            SELECT publish_date, well_depth, SUM(rig_count) as rig_count
            FROM main
            GROUP BY publish_date, well_depth
        ) as m
        LEFT JOIN (
            SELECT publish_date, SUM(rig_count) as overall_weekly_rig_count
            FROM main
            GROUP BY publish_date
        ) as s
        ON s.publish_date = m.publish_date
        ORDER BY m.publish_date
    '''

    df = pd.read_sql(sql, conn)

    conn.close()

    return df

def get_share_trajectory_df():
    sql = '''
        SELECT m.publish_date, m.trajectory, m.rig_count, s.overall_weekly_rig_count
        FROM (
            SELECT publish_date, trajectory, SUM(rig_count) as rig_count
            FROM main
            GROUP BY publish_date, trajectory
        ) as m
        LEFT JOIN (
            SELECT publish_date, SUM(rig_count) as overall_weekly_rig_count
            FROM main
            GROUP BY publish_date
        ) as s
        ON s.publish_date = m.publish_date
        ORDER BY m.publish_date
    '''

    df = pd.read_sql(sql, conn)

    conn.close()

    return df

def get_weekly_total_df():

    sql = '''
        SELECT publish_date as date, SUM(rig_count) as overall_weekly_total
        FROM main
        GROUP BY publish_date
    '''

    df = pd.read_sql(sql, conn)

    conn.close()

    return df



# def get_rig_indicator_fig(date):
#
#     df = get_weekly_total_df().astype({'date': str})
#
#     current_df = df[df['date'] == date]
#
#     date_list = df['date'].unique().tolist()
#
#     one_week_ago_df = df[df['date'] = date_list[date_list.index(date) - 1]]
#
#     one_year_df = df[(df['date'] >= str(int(date[:4]) - 1) + date[4:]) & (df['date'] <= date)]

