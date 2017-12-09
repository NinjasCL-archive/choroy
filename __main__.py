# -*- coding: utf-8 -*-
""" 
Choroy (https://www.avesdechile.cl/039.htm) 
is a simple shortener for chaucha addresses

Usage: 
Base Url: https://choroy.chaucha.cl

GET /{uid}

Returns an json containing the chaucha address for the given uid

Example Json Output:
  {
      "data": {
          "address": "chUZgQYe3fxNGEjyRbQyehQ3Q7mkJrTWdU",
          "created_at": 1512773521.5192478,
          "_links": {
              "uri": "/@clsource",
              "url": "http://localhost:8666/@clsource"
          },
          "uid": "@clsource"
      }
  }

POST /links

Create a new short url for a chaucha address

Params:
 - uid (string, optional) : Custom uid. If not given a random uid is created
 - address (string, required): Chaucha Address to shorten.

Headers:
  Content-Type: application/json

Example Json Input:
  {
    "uid" : "@clsource",
    "address" : "chUZgQYe3fxNGEjyRbQyehQ3Q7mkJrTWdU"
  }

Example Json Output:
  {
      "data": {
          "address": "chUZgQYe3fxNGEjyRbQyehQ3Q7mkJrTWdU",
          "created_at": 1512773521.5192478,
          "_links": {
              "uri": "/@clsource",
              "url": "http://localhost:8666/@clsource"
          },
          "uid": "@clsource"
      }
  }

------------

GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Copyright (c) 2017 Proyecto Chaucha <https://www.chaucha.cl>
Coded by: Camilo Castro <camilo@ninjas.cl>
Date: 8 December 2017
Url: https://github.com/proyecto-chaucha/choroy

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from choroy import app, host, port

if __name__ == '__main__':
  
  try:
    app.run(host, port, True)
  except PermissionError:
    app.run(host, 8666, True)
