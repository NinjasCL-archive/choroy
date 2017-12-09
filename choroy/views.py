import json
import urllib

from uuid import uuid4
from time import time

from tinydb import Query

from flask import jsonify, url_for, request
from choroy import app, db, base_url, sample_address, name, version

def links_for_uid(uid = ''):
  uri = url_for('read', uid=uid)
  url = '%s%s' % (base_url, uri)
  return {
    'uri' : urllib.parse.unquote(uri),
    'url' : urllib.parse.unquote(url),
    'encoded_uri' : uri,
    'encoded_url' : url
  }

@app.errorhandler(Exception)
def handle_exception(raw):
  print('Error: %s' % raw)
  error = {
    'error' : 'Error al procesar request'
  }
  response = jsonify(error)
  response.status_code = 400
  return response

@app.route('/', methods = ['GET'])
def index():
  payload = {
    'data' : {
      'name' : name,
      'version' : version,
      '_links' : {
        'new' : '/links',
        'docs' : 'https://github.com/proyecto-chaucha/choroy'
      }
    }
  }
  response = jsonify(payload)
  return response


@app.route('/<string:uid>', methods = ['GET'])
def read(uid):

  File = Query()
  results = db.search(File.data.uid == uid)

  if len(results) < 0:
    raise ValueError('%s Not Found' % uid)

  output = results[0]
  output['data']['_links'] = links_for_uid(uid)
  return jsonify(output)

@app.route('/links', methods = ['POST'])
def create():
  data = request.get_json(force=True)

  uid = ''
  address = ''

  try:
    uid = data['uid'] or ''
    print('Using %s Uid' % uid)
  except Exception:
    pass

  try:
    address = data['address'] or ''
    print('Using %s Address' % address)
  except Exception:
    pass

  if not uid or uid == '':
    print('UID Not Valid %s' % uid)
    uid = uuid4().hex[0:5]
    print('New UID %s' % uid)


  if not address or address == '':
    print('Address not Found')
    raise ValueError('Address not Found')

  sample = sample_address
  if not address[0] == sample[0] or len(address) < len(sample):
    print('Not a Public Chaucha Address')
    raise ValueError('Not a Public Chaucha Address')

  File = Query()
  results = db.search(File.data.uid == uid)

  if len(results) > 0:
    raise ValueError('%s Found' % uid)

  payload = {
    'data' : {
      'uid' : uid,
      'address' : address,
      'created_at' : time()
    }
  }

  db.insert(payload)

  payload['data']['_links'] = links_for_uid(uid)

  response = jsonify(payload)
  response.status_code = 201

  return response
