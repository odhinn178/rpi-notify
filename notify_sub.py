#!/usr/bin/python3

import logging
import os
import ssl
import paho.mqtt.client as mqtt

current_path = os.path.dirname(__file__)
log_dir = '/var/log'
log_path = os.path.normpath(os.path.abspath(log_dir))

LOG = logging.getLogger(__name__)
timestamp_format_string = "_%m%d%y_%H%M%S"


def on_connect(mqttc, obj, flags, rc):
    if rc == 0:
        LOG.info('Subscriber Connection status code: {} | Connection status: successful'.format(rc))
    elif rc == 1:
        LOG.info('Subscriber Connection status code: {} | Connection status: connection refused'.format(rc))


def on_subscribe(mqttc, obj, mid, granted_qos):
    LOG.info('Subscribed: {} {} data {}'.format(mid, granted_qos, obj))


def on_message(mqttc, obj, msg):
    LOG.info('Received message from topic: {} | QoS: {} | Data Received: {}'.format(msg.topic, msg.qos, msg.payload))


def main():
    # Set up logging
    log_file = os.path.normpath(log_path + '/' + 'rpi_notify.log')
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s : %(name)s : %(lineno)s : %(levelname)s : %(message)s',
                        filename=log_file,
                        filemode='w')
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    LOG.setLevel(logging.DEBUG)
    LOG.addHandler(console_handler)

    # Create a client with client-id = RPiNotify
    mqttc = mqtt.Client(client_id="RPiNotify")

    mqttc.on_connect = on_connect
    mqttc.on_subscribe = on_subscribe
    mqttc.on_message = on_message

    # Configure network encryption and authentication options. Enables SSL/TLS support.
    mqttc.tls_set("/home/pi/root-CA.crt",
            certfile="/home/pi/d026af591f-certificate.pem.crt",
            keyfile="/home/pi/d026af591f-private.pem.key",
            tls_version=ssl.PROTOCOL_TLSv1_2,
            ciphers=None)

    # Connect to aws-iot endpoint
    mqttc.connect("AXBVRTRIAWLF1.iot.us-west-2.amazonaws.com", port=8883)

    # Subscribe to the notifiation topic
    mqttc.subscribe("update/", qos=1)

    # Automatically handles reconnecting
    mqttc.loop_forever()


if __name__ == '__main__':
    main()