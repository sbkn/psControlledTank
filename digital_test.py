#!/usr/bin/env python
# Requires the pigpio daemon to be running:
# sudo pigpiod

from evdev import InputDevice, categorize, ecodes
import time
import pigpio

SERVO = 13
pi = pigpio.pi()

print('calibrating at 1500 PWM ..')
pi.set_servo_pulsewidth(SERVO, 1500)
time.sleep(3)

print('calibration done.')

gamepad = InputDevice('/dev/input/event7')
print(gamepad)

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        catEvent = categorize(event)
        #print(event)
        #print('======')
        #print(categorize(event))
        #print('>>>>>>>>>>>>>')
        if event.code == ecodes.ecodes['BTN_SOUTH']:
            if catEvent.keystate == catEvent.key_down:
                print('X pressed!')
                pi.set_servo_pulsewidth(SERVO, 1300)
            else:
                print('X released')
                pi.set_servo_pulsewidth(SERVO, 1500)
        elif event.code == ecodes.ecodes['BTN_NORTH']:
            if catEvent.keystate == catEvent.key_down:
                print('TRIANGLE pressed!')
                pi.set_servo_pulsewidth(SERVO, 1700)
            else:
                print('TRIANGLE released')
                pi.set_servo_pulsewidth(SERVO, 1500)
        elif event.code == ecodes.ecodes['BTN_TR2']:
            print('R2 pressed, escaping ..')
            break


print('stopping pulses ..')
pi.set_servo_pulsewidth(SERVO, 0)
pi.stop()
time.sleep(1)
