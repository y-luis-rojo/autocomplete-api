import os

from flask import Flask, jsonify, request

from autocomplete.repository import AppsRepository

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('application.cfg', silent=True)

if app.config['APPS_FILE'].startswith('/'):
    # Absolute path
    repository = AppsRepository(app.config['APPS_FILE'])
else:
    # Relative path
    repository = AppsRepository(os.path.dirname(os.path.realpath(__file__)) + '/' + app.config['APPS_FILE'])


@app.route('/', methods=['GET'])
def hello_world():
    prefix = request.args.get('prefix')
    return jsonify(repository.get(prefix))


if __name__ == '__main__':
    app.run()
