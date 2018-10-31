from eu.mattdw.usbrobotarm.specification import Specification

class Mapper:
    
    _map = {
        'base': {
            'none': [None, 0b00000000, None],
            'anticlockwise': [None, 0b00000010, None],
            'clockwise': [None, 0b00000001, None],
        },
        'shoulder': {
            'none': [0b00000000, None, None],
            'up': [0b01000000, None, None],
            'down': [0b10000000, None, None],
        },
        'elbow': {
            'none': [0b00000000, None, None],
            'up': [0b00010000, None, None],
            'down': [0b00100000, None, None],
        },
        'wrist': {
            'none': [0b00000000, None, None],
            'up': [0b00000100, None, None],
            'down': [0b00001000, None, None],
        },
        'grip': {
            'none': [0b00000000, None, None],
            'close': [0b00000001, None, None],
            'open': [0b00000010, None, None],
        },
        'light': {
            'on': [None, None, 0b00000001],
            'off': [None, None, 0b00000000],
        }
    }

    def map_specification(specification):
        if (type(specification) is not Specification):
            raise TypeError('Specification must be given as a specification object')

        bitmap = [0b00000000, 0b00000000, 0b00000000]

        for component_name, setting in specification.get_all_settings().items():
            Mapper.__map_component(bitmap, component_name, setting)

        return bitmap

    def __map_component(bitmap, component_name, setting):
        current_bitmap = Mapper._map[component_name][setting]

        for i in range(len(current_bitmap)):
            if (current_bitmap[i] is not None):
                bitmap[i] = bitmap[i] | current_bitmap[i]
