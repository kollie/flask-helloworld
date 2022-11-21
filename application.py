import os
import flask

application = flask.Flask(__name__)

@application.route('/')
def hello_world():
  return "Testing app github pipeling.."

if __name__ == "__main__":
  application.run()