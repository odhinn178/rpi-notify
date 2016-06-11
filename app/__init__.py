from flask import Flask
from app import config
from app import notify

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY

rpi_notify = notify.RPiNotify(config.app_cfg, config.cert_path)

from app import views