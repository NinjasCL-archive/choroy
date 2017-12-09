import os
from os import environ
from flask import Flask
from tinydb import TinyDB

app = Flask(__name__)

pwd = os.path.dirname(os.path.abspath(__file__))
db = TinyDB('%s/storage/db.json' % pwd)
sample_address = 'chUZgQYe3fxNGEjyRbQyehQ3Q7mkJrTWdU'

host = environ.get('CHOROY_SERVER_HOST', 'localhost')
  
if host == '':
  host = 'localhost'

port = 8666
try:
  port = int(environ.get('CHOROY_SERVER_PORT', port))
except ValueError:
  port = 8666

# Change to https if needed
protocol = environ.get('CHOROY_SERVER_PROTOCOL', 'http')
base_url = '%s://%s:%s' % (protocol, host, port)
if(port == 80):
  base_url = '%s://%s' % (protocol, host)


name = 'Choroy'
version = '1.0.0'

from choroy import views