import os
from flask import Flask

app = Flask(__name__)

VERSION = os.environ.get("APP_VERSION", "v1")
COLOR = os.environ.get("APP_COLOR", "#2c3e50")

PAGE = """
<html>
  <body style="background-color:{color}; color:white; font-family:sans-serif; text-align:center; padding-top:15%;">
    <h1>DevOps Journey App</h1>
    <h2>Version: {version}</h2>
    <p>Deployed via: {deployer}</p>
  </body>
</html>
"""


@app.route("/")
def home():
    deployer = os.environ.get("DEPLOYED_BY", "unknown")
    return PAGE.format(color=COLOR, version=VERSION, deployer=deployer)


@app.route("/healthz")
def health():
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
