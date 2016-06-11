from app import app
from app import rpi_notify


class Message(object):
    def __init__(self):
        self.message_pending = False
        self.message = None
        self.priority = False

    def callback(self, client, userdata, msg):
        self.message, self.priority = rpi_notify.get_message_from_payload(msg)
        print('Message received [pri: {}]: {}'.format(self.priority, self.message))
        self.message_pending = True

    def get_message(self):
        return self.message, self.priority

    def flush_message(self):
        self.message = None
        self.priority = False


Msg = Message()


@app.before_first_request
def connect_and_subscribe():
    rpi_notify.connect()
    rpi_notify.set_message_callback(Msg.callback)


@app.before_first_request
def run():
    rpi_notify.run()
    rpi_notify.subscribe_to_notify_topic()