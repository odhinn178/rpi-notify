from flask import Flask
from flask_bootstrap import Bootstrap
from flask_socketio import SocketIO
from app import config
from app import notify

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['DEBUG'] = True
Bootstrap(app)
socketio = SocketIO(app)

rpi_notify = notify.RPiNotify(config.app_cfg, config.cert_path)

from app import views