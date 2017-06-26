#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

#初期化、初期設定
GPIO.setmode(GPIO.BCM)

PIN = 24
GPIO.setup(PIN, GPIO.OUT)
servo = GPIO.PWM(PIN, 50) 

def reset():
  GPIO.output(PIN, GPIO.LOW)

def switch():
  servo.start(0.0)
  servo.ChangeDutyCycle(5.0)
  time.sleep(1.0)
  servo.ChangeDutyCycle(3.1)
  time.sleep(1.0)
  servo.ChangeDutyCycle(5.0)
  time.sleep(1.0)


try:
  print("オンにするよ!!!")
  switch()
finally:
  print("オンにしたよ!!!")
  servo.stop()
  reset()
  GPIO.cleanup()


