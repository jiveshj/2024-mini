from machine import Pin
import network
import random
import time
import urequests
import ujson as json

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
ssid = "" #add your SSID
password = " " # add your password
wlan.connect(ssid,password)

print('connecting...')
while not wlan.isconnected():
    pass 

print('Connected to Wi-Fi')