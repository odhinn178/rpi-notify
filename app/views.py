from flask import render_template, redirect, url_for, flash

from app import app, socketio
from app import rpi_notify
from app.forms import NotifyForm
from app.model import Msg

def index():
    form = NotifyForm()
    if form.validate_on_submit():
        msg = form.message.data
        priority = form.priority.data
        rpi_notify.send_notification(msg, priority)
        flash('Message sent')
        socketio.emit('notify', {'message': msg,
                                 'priority': priority},
                      namespace='/notification')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

def notification():
    return render_template('notification.html')

app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
app.add_url_rule('/notification', 'notification', notification, methods=['GET', 'POST'])

@socketio.on('connect')
def socket_connect():
    print('Client connected!')

@socketio.on('disconnect')
def socket_disconnected():
    print('Client disconnected!')
