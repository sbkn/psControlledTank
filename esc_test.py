#!/usr/bin/env python

# esc_start.py
# 2015-04-14
# Public Domain
#
# Sends the servo pulses needed to initialise some ESCs
#
# Requires the pigpio daemon to be running
#
# sudo pigpiod

import time
import pigpio

SERVO = 13

pi = pigpio.pi() # Connect to local Pi.

print('calibrating at 1500 ..')

pi.set_servo_pulsewidth(SERVO, 1500)

time.sleep(5)

print('calibration done.')

print('testing min throttle ..')

pi.set_servo_pulsewidth(SERVO, 1000) # Minimum throttle.

time.sleep(2)

print('resetting to 1500 ..')

pi.set_servo_pulsewidth(SERVO, 1500)

time.sleep(1)

print('testing max throttle ..')

pi.set_servo_pulsewidth(SERVO, 2000) # Maximum throttle.

time.sleep(2)

print('1800:')

pi.set_servo_pulsewidth(SERVO, 1800)

time.sleep(2)

print('1600:')

pi.set_servo_pulsewidth(SERVO, 1600)

time.sleep(2)

print('1500:')

pi.set_servo_pulsewidth(SERVO, 1500)

time.sleep(1)

print('1400:')

pi.set_servo_pulsewidth(SERVO, 1400)

time.sleep(2)

print('1300:')

pi.set_servo_pulsewidth(SERVO, 1300)

time.sleep(2)

print('1200:')

pi.set_servo_pulsewidth(SERVO, 1200)

time.sleep(2)

print('1100:')

pi.set_servo_pulsewidth(SERVO, 1100)

time.sleep(2)

print('1000:')

pi.set_servo_pulsewidth(SERVO, 1000)

time.sleep(2)

print('stopping pulses ..')

pi.set_servo_pulsewidth(SERVO, 0) # Stop servo pulses.

pi.stop() # Disconnect from local Raspberry Pi.
