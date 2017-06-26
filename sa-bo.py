#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIN = 18
GPIO.setup(PIN, GPIO.OUT)
servo = GPIO.PWM(PIN, 50) 

def reset():
  GPIO.output(PIN, GPIO.LOW)

print "start!!!"

servo.start(0.0)
servo.ChangeDutyCycle(2.4)
time.sleep(1)
servo.ChangeDutyCycle(10.5)
time.sleep(1)
servo.ChangeDutyCycle(2.4)
time.sleep(1)

print "finish!!!"

servo.stop()
reset()
GPIO.cleanup()


