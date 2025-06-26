import os

from peewee import SqliteDatabase

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

db_path = os.path.join(BASE_DIR, '..', 'config', 'data', 'playbase_db.sqlite')

db_path = os.path.normpath(db_path)

db = SqliteDatabase(db_path)
