#!/usr/bin/env python
# Storagenerd v0.1 29-May-2024
# Helper script to make single file scanning available through rest api.
# Test with curl http://localhost:8081/api/v0.1/test or
# curl -X POST -H "Content-Type: application/json" http://localhost:8081/api/v0.1/scan -d '{"file": "/home"}'

from flask import Flask, abort, jsonify, request
import subprocess

host = '0.0.0.0'
port = '8081'

'''Load Flask'''
app = Flask(__name__)

'''Define paths and responses'''
@app.route('/')
def index():
    return "This app is api driven only"

@app.route('/api/v0.1/test', methods=['GET'])
def runtest():
    file = '/home'
    cmd = "sudo /opt/ds_agent/dsa_scan --target %s --json" % file
    output = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
    return output

@app.route('/api/v0.1/scan', methods=['POST'])
def runcmd():
    file = request.json['file']
    print(file)
    cmd = "sudo /opt/ds_agent/dsa_scan --target %s --json" % file
    output = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
    return output

if __name__ == '__main__':
    app.run(host=host,port=port)
