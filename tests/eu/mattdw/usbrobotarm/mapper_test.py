import unittest
from eu.mattdw.usbrobotarm.mapper import *
from eu.mattdw.usbrobotarm.specification import *

class MapperTest(unittest.TestCase):

    def test_it_will_produce_zero_bitmap_for_default_specification(self):
        self.assertEqual([0, 0, 0], Mapper.map_specification(Specification({})))

    def test_it_will_produce_correct_bitmap_for_simple_specifications(self):
        self.assertEqual([0b00000000, 0b00000010, 0b00000000], Mapper.map_specification(Specification({'base': 'anticlockwise'})))
        self.assertEqual([0b00000000, 0b00000001, 0b00000000], Mapper.map_specification(Specification({'base': 'clockwise'})))

        self.assertEqual([0b10000000, 0b00000000, 0b00000000], Mapper.map_specification(Specification({'shoulder': 'down'})))
        self.assertEqual([0b01000000, 0b00000000, 0b00000000], Mapper.map_specification(Specification({'shoulder': 'up'})))

        self.assertEqual([0b00100000, 0b00000000, 0b00000000], Mapper.map_specification(Specification({'elbow': 'down'})))
        self.assertEqual([0b00010000, 0b00000000, 0b00000000], Mapper.map_specification(Specification({'elbow': 'up'})))

        self.assertEqual([0b00001000, 0b00000000, 0b00000000], Mapper.map_specification(Specification({'wrist': 'down'})))
        self.assertEqual([0b00000100, 0b00000000, 0b00000000], Mapper.map_specification(Specification({'wrist': 'up'})))

        self.assertEqual([0b00000010, 0b00000000, 0b00000000], Mapper.map_specification(Specification({'grip': 'open'})))
        self.assertEqual([0b00000001, 0b00000000, 0b00000000], Mapper.map_specification(Specification({'grip': 'close'})))

        self.assertEqual([0b00000000, 0b00000000, 0b00000001], Mapper.map_specification(Specification({'light': 'on'})))
        self.assertEqual([0b00000000, 0b00000000, 0b00000000], Mapper.map_specification(Specification({'light': 'off'})))

    def test_it_will_produce_correct_bitmap_for_compound_specifications(self):
        self.assertEqual([0b01010110, 0b00000001, 0b00000001], Mapper.map_specification(Specification({'base': 'clockwise', 'shoulder': 'up', 'elbow': 'up', 'wrist': 'up', 'grip': 'open', 'light': 'on'})))
        self.assertEqual([0b10000101, 0b00000010, 0b00000000], Mapper.map_specification(Specification({'base': 'anticlockwise', 'shoulder': 'down', 'elbow': 'none', 'wrist': 'up', 'grip': 'close', 'light': 'off'})))

if __name__ == '__main__':
    unittest.main()
