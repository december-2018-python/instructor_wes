from .mysqlconnection import connectToMySQL
import random
SCHEMA = 'ninja_gold_december'

def get_all():
  db = connectToMySQL(SCHEMA)
  query = "SELECT * FROM locations;"
  return db.query_db(query)

def calculate_gold_with_id(location_id):
  db = connectToMySQL(SCHEMA)
  query = 'SELECT min_gold, max_gold FROM locations WHERE id=%(location_id)s;'
  data = {
    'location_id': location_id
  }
  location = db.query_db(query, data)[0]
  return random.randint(location['min_gold'], location['max_gold'])