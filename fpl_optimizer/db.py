from os import environ
from flask import g
from flask.cli import with_appcontext
import sqlalchemy as sa
import click

def init_db(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(setup_db)

def get_db():
    conn_string = get_connection_string()
    engine = sa.create_engine(conn_string, connect_args={'sslmode':'require'})
    if 'db' not in g:
        g.db = engine.connect()
        if(not g.db.closed): 
            print('Connected to database')
    else:
        print('Database already initialized')
    return g.db

def get_connection_string():
    host = environ.get('DBHOST')
    user = environ.get('DBUSER')
    password = environ.get('DBPASS')
    name = environ.get('DBNAME')

    conn_string = 'postgresql+psycopg2://{0}:{1}@{2}/{3}'.format(user, password, host, name)
    return conn_string

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
        print("Closed database connection")

@click.command('setup_db')
@with_appcontext
def setup_db():
    print("No database setup implemented yet")