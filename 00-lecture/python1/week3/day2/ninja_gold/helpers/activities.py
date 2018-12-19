from .mysqlconnection import connectToMySQL
SCHEMA = 'ninja_gold_december'

def get_all_for_current_user(user_id):
  db = connectToMySQL(SCHEMA)
  query = 'SELECT * FROM activities WHERE user_id=%(user_id)s;'
  data = {
    "user_id": user_id
  }
  return db.query_db(query, data)