import unittest
from eu.mattdw.usbrobotarm.specification import *

class SpecificationTest(unittest.TestCase):

    def test_it_will_throw_unrecognised_component_exception_for_unrecognised_components(self):
        with self.assertRaises(UnrecognisedComponentException, msg='Unrecognised component(s): something,else'):
            try:
                Specification({'something': '', 'else': ''})
            except UnrecognisedComponentException as ex:
                self.assertEqual(frozenset(['something', 'else']), ex.get_invalid_components())

                raise ex


    def test_it_will_throw_invalid_component_setting_exception_for_invalid_component_setting(self):
        with self.assertRaises(InvalidComponentSettingException, msg='Unrecognised setting \'other\' for component: shoulder'):
            try:
                Specification({'light': 'none'})
            except InvalidComponentSettingException as ex:
                self.assertEqual('light', ex.get_component_name())
                self.assertEqual('none', ex.get_invalid_setting())
                raise ex

    def test_it_will_throw_unrecognised_component_exception_for_single_unrecognised_component_name(self):
        with self.assertRaises(UnrecognisedComponentException, msg='Unrecognised component(s): another'):
            Specification({'shoulder': 'up'}).get_settings_for_component('another')

    def test_it_will_return_recognised_component_setting(self):
        self.assertEqual('down', Specification({'elbow': 'down'}).get_settings_for_component('elbow'))

    def test_it_will_fill_defaults_for_component_settings_not_given(self):
        spec = Specification({'shoulder': 'down', 'base': 'anticlockwise'})
        all_settings = spec.get_all_settings()

        self.assertEqual('anticlockwise', spec.get_settings_for_component('base'))
        self.assertEqual('anticlockwise', all_settings['base'])
        self.assertEqual('down', spec.get_settings_for_component('shoulder'))
        self.assertEqual('down', all_settings['shoulder'])
        self.assertEqual('none', spec.get_settings_for_component('elbow'))
        self.assertEqual('none', all_settings['elbow'])
        self.assertEqual('none', spec.get_settings_for_component('wrist'))
        self.assertEqual('none', all_settings['wrist'])
        self.assertEqual('none', spec.get_settings_for_component('grip'))
        self.assertEqual('none', all_settings['grip'])
        self.assertEqual('off', spec.get_settings_for_component('light'))
        self.assertEqual('off', all_settings['light'])

    def test_it_can_create_a_union_based_on_existing_settings(self):
        spec = Specification({'shoulder': 'down', 'base': 'anticlockwise'}).union({'base': 'clockwise', 'elbow': 'up'})
        all_settings = spec.get_all_settings()

        self.assertEqual('clockwise', spec.get_settings_for_component('base'))
        self.assertEqual('clockwise', all_settings['base'])
        self.assertEqual('down', spec.get_settings_for_component('shoulder'))
        self.assertEqual('down', all_settings['shoulder'])
        self.assertEqual('up', spec.get_settings_for_component('elbow'))
        self.assertEqual('up', all_settings['elbow'])
        self.assertEqual('none', spec.get_settings_for_component('wrist'))
        self.assertEqual('none', all_settings['wrist'])
        self.assertEqual('none', spec.get_settings_for_component('grip'))
        self.assertEqual('none', all_settings['grip'])
        self.assertEqual('off', spec.get_settings_for_component('light'))
        self.assertEqual('off', all_settings['light'])

if __name__ == '__main__':
    unittest.main()
