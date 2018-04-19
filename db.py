import psycopg2, os, warnings, pdb
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

if find_dotenv() == '':
    warnings.warn('You should probably have a .env file with database config arguments')

aigh_db_args = {
    'dbname' : os.environ.get('AIGH_DATABASE', 'aigh'),
    'host' : os.environ.get('AIGH_HOST', 'localhost'),
    'user' : os.environ.get('AIGH_USER', ''),
    'password' : os.environ.get('AIGH_PASSWORD', '')
}
aigh_conn = psycopg2.connect(**aigh_db_args)

atlas_db_args = {
    'dbname' : os.environ.get('ATLAS_DATABASE', 'atlas'),
    'host' : os.environ.get('ATLAS_HOST', 'localhost'),
    'user' : os.environ.get('ATLAS_USER', ''),
    'password' : os.environ.get('ATLAS_PASSWORD', '')
}
atlas_conn = psycopg2.connect(**atlas_db_args)