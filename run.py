#!/usr/bin/env python

from app import app
from app import rpi_notify

rpi_notify.connect()
rpi_notify.run()
app.run(debug=True)
