#!/usr/local/bin/python
# -*- coding: utf-8 -*-
 
import RPi.GPIO as GPIO
import time
 
interval_time = 0.06
loop_num = 50
 
# 各GPIOの番号
SCK = 27   #次のbit
RCK = 22   #反映
SI = 17    #データ
dP = 18    #ピンデータ
cP = 23
bP = 24
aP = 25

#初期化
GPIO.setmode(GPIO.BCM)
GPIO.setup(SCK, GPIO.OUT)
GPIO.setup(RCK, GPIO.OUT)
GPIO.setup(SI, GPIO.OUT)
GPIO.setup(aP, GPIO.OUT)
GPIO.setup(bP, GPIO.OUT)
GPIO.setup(cP, GPIO.OUT)
GPIO.setup(dP, GPIO.OUT)
 
def reset():
  GPIO.output(SCK, GPIO.LOW)
  GPIO.output(RCK, GPIO.LOW)
  GPIO.output(SI, GPIO.LOW)
  GPIO.output(aP, GPIO.LOW)
  GPIO.output(bP, GPIO.LOW)
  GPIO.output(cP, GPIO.LOW)
  GPIO.output(dP, GPIO.LOW)
 
def shift(PIN_NUM):
  GPIO.output(PIN_NUM, GPIO.HIGH)
  GPIO.output(PIN_NUM, GPIO.LOW)

LED_0 = [1,1,1,1,1,1,0,0]
LED_1 = [0,1,1,0,0,0,0,1]
LED_2 = [1,1,0,1,1,0,1,0]
LED_3 = [1,1,1,1,0,0,1,1]
LED_4 = [0,1,1,0,0,1,1,0]
LED_5 = [1,0,1,1,0,1,1,1]
LED_6 = [1,0,1,1,1,1,1,0]
LED_7 = [1,1,1,0,0,0,0,1]
LED_8 = [1,1,1,1,1,1,1,0]
LED_9 = [1,1,1,1,0,1,1,1]

def send_data(data, pin):
  GPIO.output(RCK, GPIO.LOW)
  GPIO.output(SCK, GPIO.LOW)
  GPIO.output(pin, GPIO.HIGH)

  for i in range(8):
    n = 7 - i
    if data[n] == 1:
      GPIO.output(SI, GPIO.HIGH)
      GPIO.output(pin, GPIO.HIGH)
    else:
      GPIO.output(SI, GPIO.LOW)
      GPIO.output(pin, GPIO.LOW)

    shift(SCK)

  shift(RCK)
  GPIO.output(pin, GPIO.LOW)
 
try:
  print("start")
  for num in range(loop_num):
    send_data(LED_0,aP)
    send_data(LED_1,bP)
    send_data(LED_2,cP)
    send_data(LED_3,dP)
finally:
  print("finish")
  time.sleep(0.2)
  reset()
  GPIO.cleanup()
