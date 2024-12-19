from flask import render_template, Flask, send_from_directory, jsonify, request
from flask_cors import CORS
import os
import config as cf


current_dir = os.getcwd()  # Get the current directory
parent_dir = os.path.dirname(__file__)


app = Flask(__name__,template_folder=parent_dir)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/restart', methods=['POST'])
def restart():
    data = {'message':'restarting'}
    return jsonify(data)


@app.route('/config', methods=['GET','POST'])
def config():
    if request.method == 'GET':
        data = cf.get_config_json()
        response = jsonify(data)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    elif request.method == 'POST':
        if request.json["ANNOUNCEMENTS_ENABLED"] == True:
            request.json["ANNOUNCEMENTS_ENABLED"] = "ENABLED"
        elif request.json["ANNOUNCEMENTS_ENABLED"] == False:
            request.json["ANNOUNCEMENTS_ENABLED"] = "DISABLED"
        cf.update_config(request.json)
        print(request.json)
        data = {'message':'Changes saved. Changes will take effect when the bot is restarted.'}
        response = jsonify(data)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

app.run(debug=True, host='0.0.0.0')