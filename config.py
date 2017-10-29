import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_DATABASE_URI= 'fill this field'
SQLALCHEMY_TRACK_MODIFICATIONS = False


CSRF_ENABLED = True
SECRET_KEY = 'asdf86tasdhfuisdfKHgdfasuasdyf7asdf9'

#PayService API params
PS_TIP_URL = 'https://tip.pay-trio.com/ru/'
PS_INVOICE_URL = 'https://central.pay-trio.com/invoice'
PS_SHOP_ID = 'fill this field'
PS_SECRET_KEY = 'fill this field'
