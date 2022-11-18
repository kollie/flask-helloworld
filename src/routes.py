import os
import flask

app = flask.Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
  storage = Storage()
  storage.populate()
  score = storage.score()
  return "Hello world, %d!" % score

class Storage():
  def __init__(self):
    self.db = dict()

  def populate(self):
    self.db['score'] = 1234

  def score(self):
    return self.db['score']

if __name__ == "__main__":
  app.run(host='0.0.0.0')