from machine import Pin
import network
import random
import time
import urequests
import ujson as json

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
#add your SSID
ssid = "" 
# add your password
password = " " 
wlan.connect(ssid,password)

print('connecting...')
while not wlan.isconnected():
    pass 

print('Connected to Wi-Fi')
