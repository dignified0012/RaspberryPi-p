#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

# 各GPIOの番号
SDA = 28
SCL = 30

GPIO.setmode(GPIO.BCM)

# 初期化
GPIO.setup(SDA, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
GPIO.setup(SCL, GPIO.IN, pull_up_down=GPIO.PUD_OFF)

def reset():
  GPIO.output(SDA, GPIO.LOW)
  GPIO.output(SCL, GPIO.LOW)

try:
  print("start")
  for i in range(20):
    time.sleep(1)
    print(i)

   
finally:
  print("finish")
  GPIO.setup(SDA, GPIO.OUT)
  GPIO.setup(SCL, GPIO.OUT)
  reset()
  GPIO.cleanup()
