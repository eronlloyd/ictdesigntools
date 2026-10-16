from unittest import TestCase
from cabling.optical import IECFiberPerformance, CWDM_BANDS, Wavelength, OpticalCable


class ReferenceValues(TestCase):

    def test_cwdm_bands(self):
        self.assertEqual(CWDM_BANDS, [1271, 1291, 1311, 1331, 1351, 1371, 1391, 1411, 1431, 
                                      1451, 1471, 1491, 1511, 1531, 1551, 1571, 1591, 1611])


class WavelengthTests(TestCase):

    def test_instance_is_valid(self):
        w = Wavelength('1550', 1550)
        self.assertIsInstance(w, Wavelength) 

    def test_instance_configuration(self):
        w = Wavelength("1310", 1310)
        self.assertEqual(w.nominal_nm, 1310)

class OpticalCableTests(TestCase):

    def test_cable_instance_is_valid(self):
        cable = OpticalCable('F1-01', IECFiberPerformance.OS2)
        print(cable)
        print(cable.itu_recommendation)
        self.assertIsInstance(cable, OpticalCable)