# 
# Felipe Ryan Jan 2016
#
import os
from flask import Flask, render_template, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy
import json


app = Flask(__name__)

if 'DATABASE_URL' in os.environ:
    app.config.from_object('config.Production')
else:
    app.config.from_object('config.Development')

db = SQLAlchemy(app)

@app.route('/')
def hello():
    #return render_template('index.html')
    return "Hello World!"


@app.route('/api/v1.0/scans', methods=['POST'])
def receive_scan_from_api():
    if not request.json:
        abort(400)

    msg = json.dumps(request.json)

    print '\nJson Received from External Source:'
    print msg
    print '\n'
    
    return jsonify({'Response':'All ok'}), 201


if __name__ == '__main__':
    app.run()
