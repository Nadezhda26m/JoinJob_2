from os.path import dirname, exists
from os import makedirs

PATH_DB = f'{dirname(__file__)}\\database\\'

if not exists(PATH_DB):
    makedirs(PATH_DB)
