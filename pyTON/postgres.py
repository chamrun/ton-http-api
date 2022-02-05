import psycopg2


def postgres_insert_record(rec, table, postgres_settings):
    with psycopg2.connect(**postgres_settings) as conn:
        with conn.cursor() as cur:
            keys = list(rec.keys())
            keys_format = ', '.join(keys)
            values_format = ', '.join(['%s'] * len(keys))
            sql = f"insert into {table}({keys_format}) values ({values_format})"
            values = list(rec.values())
            cur.execute(sql, values)
    return


def postgres_execute_sql(sql, postgres_settings):
    with psycopg2.connect(**postgres_settings) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
    return


liteserver_tasks_table_create_query = '''create table if not exists liteserver_tasks(
    id serial,
    timestamp integer NOT NULL,
    liteserver varchar NOT NULL,
    method varchar NOT NULL,
    elapsed float NOT NULL,
    result_type varchar NOT NULL,
    details json
);
create index if not exists liteserver_tasks_timestamp_idx on liteserver_tasks(timestamp);'''


requests_table_create_query = '''create table if not exists requests(
    id serial,
    timestamp float NOT NULL,
    from_ip varchar NOT NULL,
    url varchar NOT NULL,
    status_code integer NOT NULL,
    elapsed float NOT NULL,
    referer varchar,
    origin varchar,
    api_key varchar
);
create index if not exists requests_timestamp_idx on requests(timestamp);'''
