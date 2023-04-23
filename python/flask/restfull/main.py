from flask import Flask, url_for, request, Response
from flask import json, jsonify
from functools import wraps


app = Flask(__name__)


@app.route('/')
def api_root():
    return 'Welcome'


@app.route('/articles')
def api_articles():
    return f"List of {url_for('api_articles')}"

# Routes can use differnt converters in their definition
# e.g.: @app.route('/articles/<articleid>')
# can be replaced by:
# @app.route('/articles/<articleid>')       -> accepts any text without a slash (the default)
# @app.route('/articles/<int:articleid>')   -> accepts integers
# @app.route('/articles/<float:articleid>') -> like int but for floating point values
# @app.route('/articles/<path:articleid>')  -> like the default but also accepts slashes
# @app.route('/articles/<any:articleid>')   -> matches one of the items provided
# @app.route('/articles/<uuid:articleid>')  -> accepts UUID strings
# default is `string` which accepts any text without slashes.


@app.route('/articles/<articleid>')
def api_article(articleid):
    return f"You are reading {articleid}"


@app.route('/hello')
def api_hello():
    if 'name' in request.args:
        return f"Hello {request.args['name']}\n"
    return 'Hello John'


# REQUEST METHODS (HTTP VERBS)

@app.route('/echo', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    match request.method:
        case 'GET':
            return 'ECHO: GET\n'
        case 'POST':
            return 'ECHO: POST\n'
        case 'PATCH':
            return 'ECHO: PATCH\n'
        case 'PUT':
            return 'ECHO: PUT\n'
        case 'DELETE':
            return 'ECHO: DELETE\n'



# REQUEST DATA & HEADERS

@app.route('/messages', methods=['POST'])
def api_message():
    match request.headers['Content-Type']:
        case 'text/plain':
            return f"Text Message: {request.data}"
        case 'application/json':
            return f"JSON Message: {json.dumps(request.json)}"
        case 'application/octet-stream':
            with open('./binary.bin', 'wb') as f:
                f.write(request.data)
            return 'Binary message written!'
        case _:
            return "415 Unsupported Media Type!"


# RESPONSES
# Responses are handled by Flask's Response class


@app.route('/hi', methods=['GET'])
def api_hi():
    data = {
        'hello': 'world',
        'number': 3
    }
    js = json.dumps(data)

    # We can replace this line with Flask's jsonify
    # resp = Response(js, status=200, mimetype='application/json')
    resp = jsonify(data)
    resp.status_code = 200
    resp.headers['Link'] = 'http://localhost'

    return resp


# Default Flask error messages can be overwritten using
# either the @errorhandler or app.error_handler_spec[None][404] = not_found
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': f"Not Found: {request.url}"
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


@app.route('/users/<userid>', methods=['GET'])
def api_users(userid):
    users = {
        '1': 'Alice',
        '2': 'Bob',
        '3': 'Abe'
    }

    return jsonify({userid:users[userid]}) if userid in users else not_found()


# AUTHORIZATION

def check_auth(username, password):
    return username == 'admin' and password == 'secret'


def authenticate():
    message = {'message': 'Authenticate.'}
    resp = jsonify(message)

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Localhost"'

    return resp


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth:
            return authenticate()
        elif not check_auth(auth.username, auth.password):
            return authenticate()

        return f(*args, **kwargs)
    return decorated


@app.route('/secrets')
@requires_auth
def api_secret():
    return 'secret text'


# DEBUG & LOGGING
# app.run(debug=True)
# Flask uses python logging off the box
import logging
file_handler = logging.FileHandler('app.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)


@app.route('/logging', methods=['GET'])
def api_logging():
    app.logger.info('informing')
    app.logger.warning('warning')
    app.logger.error('something bad happened')

    return 'check your logs\n'


if __name__ == '__main__':
    app.run(debug=True)
