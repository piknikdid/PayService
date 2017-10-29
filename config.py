import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_DATABASE_URI= 'mysql://root:admin123@localhost/invoice_data'
SQLALCHEMY_TRACK_MODIFICATIONS = False


CSRF_ENABLED = True
SECRET_KEY = 'asdf86tasdhfuisdfKHgdfasuasdyf7asdf9'

#PayService API params
PS_TIP_URL = 'https://tip.pay-trio.com/ru/'
PS_INVOICE_URL = 'https://central.pay-trio.com/invoice'
PS_SHOP_ID = 305220
PS_SECRET_KEY = 'jwyKXMJIAK9Z6aPmLHkouUbLE7cDWxZNh'
