#!/usr/bin/python

import paho.mqtt.client as paho
import os
import socket
import ssl
from time import sleep
from random import uniform

connflag = False

def on_connect(client, userdata, flags, rc):
    global connflag
    connflag = True
    print("Connection returned result: " + str(rc) )

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

awshost = "AXBVRTRIAWLF1.iot.us-west-2.amazonaws.com"
awsport = 8883
clientId = "RPiNotify"
thingName = "RPiNotify"
caPath = "cert/root-CA.crt"
certPath = "cert/d026af591f-certificate.pem.crt"
keyPath = "cert/d026af591f-private.pem.key"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

mqttc.connect(awshost, awsport, keepalive=60)

mqttc.loop_start()

while 1==1:
    sleep(2.0)
    if connflag == True:
        tempreading = uniform(20.0,25.0)
        mqttc.publish("notify/downstream", tempreading, qos=1)
        print("msg sent: temperature " + "%.2f" % tempreading )
    else:
        print("waiting for connection...")