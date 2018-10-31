from flask import Flask, Response, request, json
import usb.core, usb.util

map = {\
    'base': {\
        'none': [None, 0b00000000, None],\
        'anticlockwise': [None, 0b00000010, None],\
        'clockwise': [None, 0b00000001, None],\
    },\
    'shoulder': {\
        'none': [0b00000000, None, None],\
        'up': [0b01000000, None, None],\
        'down': [0b10000000, None, None],\
    },\
    'elbow': {\
        'none': [0b00000000, None, None],\
        'up': [0b00010000, None, None],\
        'down': [0b00100000, None, None],\
    },\
    'wrist': {\
        'none': [0b00000000, None, None],\
        'up': [0b00000100, None, None],\
        'down': [0b00001000, None, None],\
    },\
    'grip': {\
        'none': [0b00000000, None, None],\
        'close': [0b00000001, None, None],\
        'open': [0b00000010, None, None],\
    },\
    'light': {\
        'on': [None, None, 1],\
        'off': [None, None, 0],\
    }\
}

armMask = [0, 0, 0]

app = Flask(__name__)
RoboArm = usb.core.find(idVendor=0x1267, idProduct=0x001)

@app.route('/move', methods = ['PATCH'])
def move():
    global armMask

    data = json.loads(request.data)
    newMask = armMask

    for component, value in data.items():
        if component in map and value in map[component]:
            maskArr = map[component][value]
            for i in range(0, 3):
                if (maskArr[i] is not None):
                    newMask[i] = ~newMask[i] & maskArr[i]

    armMask = newMask
    RoboArm.ctrl_transfer(0x40, 6, 0x100, 0, armMask, 3)

    return Response(json.dumps(armMask), mimetype='application/json')

@app.route('/move', methods = ['DELETE'])
def reset():
    global armMask

    armMask = [0, 0, 0]
    RoboArm.ctrl_transfer(0x40, 6, 0x100, 0, armMask, 3)

#    for i in range(0, 2):
#        if (map[i] is not None):
#            mask[i] = mask[i] ^ map[i]
#
#    RoboArm.ctrl_transfer(0x40, 6, 0x100, 0, mask, 3)

    return Response(json.dumps(armMask), mimetype='application/json')

#if __name__ == "__main__":
#    print("Hello World")

#app.run(host = '127.0.0.1', port = 8000)
app.run(host = '0.0.0.0', port = 8000)
