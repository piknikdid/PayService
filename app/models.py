import hashlib
import json
import urllib2
from . import app
from datetime import datetime
from app import db
from sqlalchemy.dialects.postgresql import JSON


class InvoiceData(db.Model):
    __tablename__ = 'invoice_data'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(20))
    amount = db.Column(db.String(20))
    currency = db.Column(db.String(20))
    payment_method = db.Column(db.String(20))
    payway = db.Column(db.String(20))
    date = db.Column(db.DateTime,
        default=datetime.utcnow)

    def __init__(self, description, amount, currency, payway, payment_method):
        self.description = description
        self.amount = amount
        self.currency = currency
        self.payment_method = payment_method
        self.payway = payway


    def __repr__(self):
        return '<id {}>'.format(self.id)


class Invoice:
    tip_params = ('amount', 'currency', 'shop_id', 'shop_invoice_id')
    invoice_params = ('amount', 'currency', 'payway', 'shop_id', 'shop_invoice_id')


    def __init__(self, description, amount, currency, payway, payment_method):
        self.description = description
        self.amount = amount
        self.currency = currency
        self.payment_method = payment_method
        self.payway = payway

        self._ps_shop_id = app.config['PS_SHOP_ID']
        self._ps_secret_key = app.config['PS_SECRET_KEY']
        self._ps_api_url = app.config['PS_INVOICE_URL']
        
        self._param_mapping = {
            'amount': self.amount,
            'currency': self.currency,
            'payway': self.payway,
            'shop_id': self._ps_shop_id,
            'shop_invoice_id':""
            
        }

    def save (self):
        save =  InvoiceData(self.description, self.amount, self.currency, self.payment_method, self.payway)
        db.session.add(save)
        db.session.commit()
        self._param_mapping['shop_invoice_id'] = int(save.id)
        return "data saved"


    def signature(self):
        keys = ()
        if self.payment_method == 'tip':
            keys = self.tip_params
        if self.payment_method == 'invoice':
            keys = self.invoice_params
        keys_sorted = sorted(keys)
        string_to_sign = ':'.join(str(self._get_param_value(param)) for param in keys_sorted) + self._ps_secret_key
        signature = hashlib.md5(string_to_sign).hexdigest()
        return signature

    def get_invoice_form_params(self):
        params = {
            "description": self.description,
            "payway": self.payway,
            "shop_invoice_id": self._param_mapping['shop_invoice_id'],
            "sign": self.signature(),
            "currency": self.currency,
            "amount": self.amount,
            "shop_id": self._ps_shop_id
        }

        req = urllib2.Request(self._ps_api_url, json.dumps(params),
                              {'Content-Type': 'application/json'})
        f = urllib2.urlopen(req)
        response = f.read()
        f.close()

        result = json.loads(response)  

        if result['result'] != 'ok':
            raise Exception
        
        return result['data']

    def _get_param_value(self, param):
        return self._param_mapping[param]