from .mysqlconnection import connectToMySQL
SCHEMA = 'ninja_gold_december'

def get_all_for_current_user(user_id):
  db = connectToMySQL(SCHEMA)
  query = '''SELECT * FROM activities 
  JOIN locations ON activities.location_id = locations.id
  WHERE user_id=%(user_id)s
  ORDER BY activities.created_at DESC;'''
  data = {
    "user_id": user_id
  }
  return db.query_db(query, data)

def create_activity(gold, user_id, location_id):
  db = connectToMySQL(SCHEMA)
  query = 'INSERT INTO activities (gold_amount, user_id, location_id, created_at, updated_at) VALUES(%(gold)s, %(user_id)s, %(location_id)s, NOW(), NOW());'
  data = {
    'gold': gold,
    'user_id': user_id,
    'location_id': location_id
  }
  return db.query_db(query, data)