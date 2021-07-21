#this code is to be run on raspberry pi
import serial
import os, time
import RPi.GPIO as GPIO
import json
import urllib3
import certifi

GPIO.setmode(GPIO.BOARD)
port = serial.Serial('/dev/serial0', baudrate=9600, timeout=1)

while True:
    port.write(b'AT\r')
    time.sleep(1)
    port.write(b'AT+CGATT=1\r')
    time.sleep(1)
    
    time.sleep(1)
    port.write(b'AT+SAPBR=3,1,"CONTYPE","GPRS"\r')
    
    time.sleep(1)
    port.write(b'AT+SAPBR=3,1,"APN","airtelgprs.com"\r')
    
    time.sleep(1)
    port.write(b'AT+SAPBR=1,1\r')
    
    time.sleep(1)
    port.write(b'AT+SAPBR=2,1\r')
    rcv = port.read(300 )
    time.sleep(1)
    port.write(b'AT+CLBS=1,1\r')#location output
    time.sleep(4)
    rcv = port.read(200)
    #print(rcv.decode())
    print("............restart")
    print(rcv)
    #b = rcv.decode()
    x=rcv.find(b"0")
    print(x)
    if x !=-1 and len(rcv)>42:
        
        a=rcv[x+2:x+21]
        a=a.decode()
        print(a)
        lat,long=a.split(",")
        print('latitude '+lat)
        print('longitude '+long)
        http = urllib3.PoolManager(ca_certs=certifi.where())
        host = "https://gsmdata.herokuapp.com/api"
        req = http.request('POST',host, fields={'d1':lat,'d2':long})
