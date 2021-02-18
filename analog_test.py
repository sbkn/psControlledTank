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

# TODO: Find out how not to hardcode the input device:
#gamepad = InputDevice('/dev/input/event4')
gamepad = InputDevice('/dev/input/event7')
print(gamepad)

actualSticks = {
    'ABS_X': 128,
    'ABS_Y': 128
}

for event in gamepad.read_loop():
    catEvent = categorize(event)
    if event.type == ecodes.EV_ABS:
        if ecodes.bytype[catEvent.event.type][catEvent.event.code] == 'ABS_X':
            actualSticks['ABS_X'] = catEvent.event.value
        elif ecodes.bytype[catEvent.event.type][catEvent.event.code] == 'ABS_Y':
            actualSticks['ABS_Y'] = catEvent.event.value
        print(actualSticks)
        
        # calculate pwm and reduce noise:
        pwm = ((actualSticks['ABS_Y'] + 1) / 255) * 1000 + 1000
        if pwm > 2000:
            pwm = 2000
        elif pwm < 1005:
            pwm = 1000
        elif pwm > 1480 and pwm < 1520:
            pwm = 1500
        print(pwm)
        
        pi.set_servo_pulsewidth(SERVO, pwm)
    if event.type == ecodes.EV_KEY:
        if event.code == ecodes.ecodes['BTN_TR2']:
            print('R2 pressed, escaping ..')
            break


print('stopping pulses ..')
pi.set_servo_pulsewidth(SERVO, 0)
pi.stop()
time.sleep(1)

