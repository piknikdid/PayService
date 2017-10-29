from flask import render_template, redirect, url_for
from . import app, db
from forms import ServiceForm
from models import Invoice


@app.route('/', methods=['GET'])
def index():
    form = ServiceForm()
    return render_template("index.html", title='Main', form=form)


@app.route('/process', methods=['POST'])
def process():
    form = ServiceForm()
    if form.validate_on_submit():
        currency = int(form.currency.data)
        if currency == 978:
            invoice = Invoice(form.description.data, form.amount.data, currency, 'payeer_usd', 'invoice')
            invoice.save()
            data = invoice.get_invoice_form_params()
            return render_template('invoice.html', data=data, title='Invoice')

        if currency == 840:
            invoice = Invoice(form.description.data, form.amount.data, currency, 'payeer_usd', 'tip')
            invoice.save()
            return render_template('tip.html', invoice=invoice, form_url=app.config['PS_TIP_URL'],
                                   shop_id=app.config['PS_SHOP_ID'], title='TIP')
    
    return redirect(url_for('index'))