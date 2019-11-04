import re
import argparse
import socket
import hashlib
from datetime import datetime

now = datetime.now()
current_day = now.strftime("%d-%m-%Y" )
current_time = now.strftime("%H:%M:%S")
ip_address =socket.gethostbyname(socket.gethostname())

# MD5  Assumes the default UTF-8
hash_object = hashlib.md5(current_day.encode())
hex_dig = hash_object.hexdigest()

content = ["Date : " + current_day +'\n', "Time : " + current_time + '\n', "IP Address : " + ip_address + '\n', "Hash : " + hex_dig]

parser = argparse.ArgumentParser()
parser.add_argument(
    '--filePath', type=str,
    default='/etc/motd',
    help='path to MOTD file (default: /etc/motd)')
args = parser.parse_args()

with open(args.filePath, 'w') as motdfile:
    motdfile.writelines(content)

