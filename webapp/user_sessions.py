import random

user_sessions = {}

def create_session(user):
  hash = str(random.random())[:50] 
  user_sessions[hash] = user
  
  return hash

def remove_session(hash):
  del user_sessions[hash]