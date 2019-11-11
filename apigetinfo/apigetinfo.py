import re
import argparse
import socket
import hashlib
import json
import netifaces as ni
from flask import Flask, jsonify

from datetime import datetime

now = datetime.now()
current_day = now.strftime("%d-%m-%Y" )
current_time = now.strftime("%H:%M:%S")
#ip_address = socket.gethostbyname(socket.gethostname())
#ip_address = socket.getfqdn(socket.gethostname())

ni.ifaddresses('eth0')
ip_address = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

# MD5  Assumes the default UTF-8
hash_object = hashlib.md5(current_day.encode())
hex_dig = hash_object.hexdigest()

info = ["Date : " + current_day, "Time : " + current_time , "IP Address : " + ip_address , "Hash : " + hex_dig ]

infojsonrdy=json.dumps(info, sort_keys=True, indent=4)

app = Flask(__name__)

@app.route("/info", methods=["GET"])
def getinfo():
    return infojsonrdy
#     return jsonify(info)

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=5000)

