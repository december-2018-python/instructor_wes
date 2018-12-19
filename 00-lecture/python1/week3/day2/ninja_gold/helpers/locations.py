from .mysqlconnection import connectToMySQL
SCHEMA = 'ninja_gold_december'

def get_all():
  db = connectToMySQL(SCHEMA)
  query = "SELECT * FROM locations;"
  return db.query_db(query)