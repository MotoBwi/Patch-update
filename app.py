from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "Hello Bapan!"


if __name__ == '__main__':  # Corrected this line
  app.run(host='0.0.0.0', debug=True)
