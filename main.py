from flask import Flask, request
from auth import ServiceAccountAuth
import os

app = Flask(__name__)

@app.route('/token')
def get_token():
    # current working directory
    cwd = os.getcwd()
    file = cwd + os.path.sep + request.args.get('file')
    scope = request.args.get('scope')
    auth_instance = ServiceAccountAuth(file, scope)
    return auth_instance.token_data["token"]

if __name__ == '__main__':
    app.run()