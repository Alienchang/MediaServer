#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from app.models import fileManager
from flask import Response, request
from flask_restful.representations import json

__author__ = 'alienchang'
from app import app

from models import album
@app.route('/test')
def test():
    return 'hello world'

@app.route('/photos')
def photos():
    return album.allPhotos()
    # return '333'

@app.route('/first_contact')
def firstContact():
    return album.firstContact()

@app.route('/print_files')
def printFiles():
    page = request.args.get('page')

    list = fileManager.GetFileList('/Users/alienchang/Pictures/照片图库.photoslibrary/Masters/', [])

    endItem = 10 * int(page) + 10;
    if list.count < 10 * int(page) + 10:
        endItem = list.count


    return Response(json.dumps(list[10 * int(page) : endItem]) ,mimetype='text/json')
#     list = GetFileList()
# for e in list:
#     print e
#     return fileManager.eachFile()
#     # fileManager.eachFile('/Users/alienchang/Pictures/照片图库.photoslibrary/Masters/')
