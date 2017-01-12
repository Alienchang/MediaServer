from flask import Response
from app.database import db
from sqlalchemy.ext.declarative import declarative_base

__author__ = 'alienchang'
# from app.database import db
import json

class Album(db.Model):
    id   = db.Column(db.Integer ,primary_key = True)
    name = db.Column(db.String() ,nullable = True)
    url  = db.Column(db.String() ,nullable = True)
    @classmethod
    def allPhotos(cls):
        return '111'


class AddressBook(db.Model):
    __tablename__ = 'address_book'
    id    = db.Column(db.Integer ,primary_key = True)
    phone = db.Column(db.String() ,nullable = True)
    uid   = db.Column(db.Integer ,nullable = True)


def firstContact():
    addressBook = db.session.query(AddressBook).first()
    return str(addressBook.phone)


class FeedBack(db.Model):
    __tablename__ = 'feedback'
    id    = db.Column(db.Integer ,primary_key = True)
    phone = db.Column(db.String() ,nullable = True)
    uid   = db.Column(db.Integer ,nullable = True)


def allPhotos():
    dictionary = [
        {
        'url' : 'http://obvsohucu.bkt.clouddn.com/20131215144203_YUQ2F.thumb.600_0.jpeg',
        'name': '20131215144203_YUQ2F'
        },
        {
        'url' : 'http://obvsohucu.bkt.clouddn.com/20131215144203_YUQ2F.thumb.600_0.jpeg',
        'name': '20131215144203_YUQ2F'
        },
        {
        'url' : 'http://obvsohucu.bkt.clouddn.com/20131215144203_YUQ2F.thumb.600_0.jpeg',
        'name': '20131215144203_YUQ2F'
        }

    ]
    # return json.dumps(dictionary)
    return Response(json.dumps(dictionary) ,mimetype='text/json')

