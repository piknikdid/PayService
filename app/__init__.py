from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import logging
from logging import FileHandler


app = Flask(__name__)
app.config.from_object('config')


db = SQLAlchemy(app)


handler = FileHandler('app.log')
handler.setLevel(logging.DEBUG)

app.logger.addHandler(handler)

from app import views

