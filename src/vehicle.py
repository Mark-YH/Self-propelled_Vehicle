'''
Created on 2017/2/2

@author: Mark Hsu
'''

import time
import RPi.GPIO as GPIO

# Physical numbering
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Define GPIO
ultrasound_Forward_TRIG = 11
ultrasound_Forward_ECHO = 12
ultrasound_Left_TRIG = 13
ultrasound_Left_ECHO = 15
ultrasound_Right_TRIG = 16
ultrasound_Right_ECHO = 18
motor_RightFront_in1 = 31
motor_RightFront_in2 = 33
motor_RightRear_in3 = 35
motor_RightRear_in4 = 37
motor_LeftFront_in1 = 32
motor_LeftFront_in2 = 36
motor_LeftRear_in3 = 38
motor_LeftRear_in4 = 40

GPIO.setup(ultrasound_Forward_TRIG, GPIO.OUT)
GPIO.setup(ultrasound_Forward_ECHO, GPIO.IN)
GPIO.setup(ultrasound_Left_TRIG, GPIO.OUT)
GPIO.setup(ultrasound_Left_ECHO, GPIO.IN)
GPIO.setup(ultrasound_Right_TRIG, GPIO.OUT)
GPIO.setup(ultrasound_Right_ECHO, GPIO.IN)
GPIO.setup(motor_RightFront_in1, GPIO.OUT)
GPIO.setup(motor_RightFront_in2, GPIO.OUT)
GPIO.setup(motor_RightRear_in3, GPIO.OUT)
GPIO.setup(motor_RightRear_in4, GPIO.OUT)
GPIO.setup(motor_LeftFront_in1, GPIO.OUT)
GPIO.setup(motor_LeftFront_in2, GPIO.OUT)
GPIO.setup(motor_LeftRear_in3, GPIO.OUT)
GPIO.setup(motor_LeftRear_in4, GPIO.OUT)

def ultrasound(TRIG, ECHO):
    GPIO.output(TRIG, 0)
    time.sleep(0.01)
    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)
    start = time.time()
    while GPIO.input(ECHO) == 0:
        start = time.time()
    while GPIO.input(ECHO) == 1:
        stop = time.time()
    distance = (stop - start) * 34000 / 2
    print(distance)

def forward():
    GPIO.output(motor_RightFront_in1,True)
    GPIO.output(motor_RightFront_in2, False)
    GPIO.output(motor_LeftFront_in1,True)
    GPIO.output(motor_LeftFront_in2, False)    

def stop():
    GPIO.output(motor_RightFront_in1,False)
    GPIO.output(motor_RightFront_in2, False)
    GPIO.output(motor_LeftFront_in1,False)
    GPIO.output(motor_LeftFront_in2, False) 

def main():
    try:
        forward()
        ultrasound(ultrasound_Forward_TRIG, ultrasound_Forward_ECHO)
        ultrasound(ultrasound_Left_TRIG, ultrasound_Left_ECHO)
        ultrasound(ultrasound_Right_TRIG, ultrasound_Right_ECHO)
        stop()
    except KeyboardInterrupt:
        GPIO.cleanup()
if __name__ == '__main__':
    main()

