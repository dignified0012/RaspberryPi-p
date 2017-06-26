#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

interval_time = 0.05
loop_num = 2

# 各GPIOの番号
SCK = 27
RCK = 22
SI = 17

GPIO.setmode(GPIO.BCM)

# 初期化
GPIO.setup(SCK, GPIO.OUT)
GPIO.setup(RCK, GPIO.OUT)
GPIO.setup(SI, GPIO.OUT)

def reset():
  GPIO.output(SCK, GPIO.LOW)
  GPIO.output(RCK, GPIO.LOW)
  GPIO.output(SI, GPIO.LOW)

def shift(PIN_NUM):
  GPIO.output(PIN_NUM, GPIO.HIGH)
  GPIO.output(PIN_NUM, GPIO.LOW)

def send_bits(data):
  for i in range(8):
    if ((1 << i ) & data) == 0:
      GPIO.output(SI, GPIO.LOW)
    else:
      GPIO.output(SI, GPIO.LOW)

    shift(SCK)

  shift(RCK)

def lighting():
  reset()

  num = 1
  for i in range(9):
    send_bits(num)
    num = num << 1
    time.sleep(interval_time)

  send_bits(0)

try:
  print("start")
  for num in range(loop_num):
    lighting()
finally:
  print("finish")
  reset()
  GPIO.cleanup()
