from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(get_remote_address, app=app, default_limits=["200 per hour", "50 per minute"])

@app.route('/secure-api')
@limiter.limit("10 per second")
def secure_endpoint():
    return "This endpoint is rate-limited."
