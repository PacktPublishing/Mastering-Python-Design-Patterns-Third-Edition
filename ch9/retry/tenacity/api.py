from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from flask import Flask

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["100 per day", "10 per hour"],
    storage_uri="memory://",
    strategy="fixed-window",
)


@app.route("/api")
@limiter.limit("2/minute")
def api():
    return {"msg": "Welcome to our API!"}


if __name__ == "__main__":
    app.run(debug=True)
