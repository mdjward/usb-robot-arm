import usb
from eu.mattdw.usbrobotarm.mapper import Mapper
from eu.mattdw.usbrobotarm.specification import Specification

class ArmController:
    
    _usb_vendor_id = 0x1267
    _usb_product_id = 0x001
    _robot_arm = None
    _specification = None

    def __init__(self, robot_arm, initial_specification=None):
        if (robot_arm is None):
            raise(TypeError('Missing USB resource'))

        specification = initial_specification if isinstance(initial_specification, Specification) else Specification({})
        ArmController.__validate_specification(specification)

        self._robot_arm = robot_arm
        self._specification = specification

    def __validate_specification(specification):
        if (type(specification) is not Specification):
            raise(TypeError('Invalid specification; expected: instance of Specification'))

        return True

    def move(self, specification):
        self._specification = specification if isinstance(specification, Specification) else Specification(specification)

        self._robot_arm.ctrl_transfer(0x40, 6, 0x100, 0, Mapper.map_specification(specification), 3)
        #print(Mapper.map_specification(self._specification))

        return self._specification

    def also_move(self, additional_instructions):
        return self.move(self._specification.union(additional_instructions.get_all_settings() if isinstance(additional_instructions, Specification) else additional_instructions))

    def reset(self):
        return self.move(Specification({}))

    def create_usb_device():
        return usb.core.find(idVendor=ArmController._usb_vendor_id, idProduct=ArmController._usb_product_id)
