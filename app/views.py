from flask import render_template, redirect, url_for, flash

from app import app
from app import rpi_notify
from app.forms import NotifyForm

def index():
    form = NotifyForm()
    if form.validate_on_submit():
        rpi_notify.send_notification(form.message, form.priority)
        flash('Message sent')
        return redirect(url_for('index'))
    return render_template('index,html', form=form)


app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])