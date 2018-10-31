import unittest
import tests.eu.mattdw.usbrobotarm

def my_module_suite():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(tests.eu.mattdw.usbrobotarm)
    return suite
