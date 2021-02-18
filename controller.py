from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input/event7')

print(gamepad)

actualSticks = {
    'ABS_X': 128,
    'ABS_Y': 128
}

for event in gamepad.read_loop():
    if event.type == ecodes.EV_ABS:
        #print(event)
        #print('======')
        #print(categorize(event))
        #print(event.code, event.value)
        catEvent = categorize(event)
        #print(ecodes.bytype[catEvent.event.type][catEvent.event.code], catEvent.event.value)
        if ecodes.bytype[catEvent.event.type][catEvent.event.code] == 'ABS_X':
            actualSticks['ABS_X'] = catEvent.event.value
        elif ecodes.bytype[catEvent.event.type][catEvent.event.code] == 'ABS_Y':
            actualSticks['ABS_Y'] = catEvent.event.value
        print(actualSticks)
        print('>>>>>>>>>>>>>')
    if event.code == ecodes.ecodes['BTN_TR2']:
        break
    
