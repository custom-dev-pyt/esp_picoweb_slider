import usocket as socket
import select
import machine, onewire, ds18x20, time
from machine import Pin, I2C, PWM, ADC

from time import sleep
import time, math

import network

import esp
esp.osdebug(None)

import gc
gc.collect()

client_ssid = 'extend'
client_password = 'Q@wh4u2s7T&g5D'
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(client_ssid, client_password)
while station.isconnected() == False:
    
    pass
print('Connection successful')
esp_addr = station.ifconfig()
print("IP ESP: {} ".format(esp_addr[0]))

