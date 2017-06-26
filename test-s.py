from RPIO import PWM
servo = PWM.Servo()
servo.set_servo(7,1000)
servo.stop_servo(7)
