"""
Entrypoint to the app
"""

from flask import Flask

app = Flask(__name__)


@app.route("/index")
def index():
    return "Hello Anmol"


if __name__ == '__main__':
    app.run()

