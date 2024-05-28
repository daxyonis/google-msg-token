from flask import Flask, request
from auth import ServiceAccountAuth

app = Flask(__name__)

@app.route('/token')
def get_token():
    file = request.args.get('file')
    scope = request.args.get('scope')
    auth_instance = ServiceAccountAuth(file, scope)
    return auth_instance.token_data["token"]

if __name__ == '__main__':
    app.run()