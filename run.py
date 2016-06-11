#!/usr/bin/env python

from app import app
from app import rpi_notify

app.run(debug=True)
rpi_notify.connect()