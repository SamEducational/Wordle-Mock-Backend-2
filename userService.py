# userService:
import toml
import base64

from typing import Tuple
from quart import Quart, jsonify, g, request, abort
from quart_schema import QuartSchema, validate_request

app = Quart(__name__)
QuartSchema(app)

app.config.from_file(f"./config/app.toml", toml.load)

def jsonify_message(message):
    return {"message": message}

def get_username_password_from_header(req) -> Tuple[str, str]:
    if "Authorization" not in request.headers:
        return "",""
    hashBytes = req.headers["Authorization"].split()[1]
    username, passsword = base64.b64decode(hashBytes).decode("utf-8").split(":")
    return username, passsword

@app.route("/", methods=["GET"])
async def home():
    """
    Home
    
    This is just the welcome message.
    """
    
    return jsonify_message("Welcome to userService.")

@app.route("/login", methods=["GET", "POST"])
async def login():
    """"
    Login
    
    Authenticate user from username & password pass through the header.
    """

    if request.method == "GET":
        return jsonify_message("Send as POST with based64(username:password) in Authorization header.")
    else:
        return {"authenticated": True}, 200