__author__ = 'alienchang'
from flask import Flask

app = Flask(__name__)
from app import test
from app.models import album