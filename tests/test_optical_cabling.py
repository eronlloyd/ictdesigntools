from unittest import TestCase
from cabling.optical import IECFiberPerformance, CWDM_BANDS, OpticalWavelength, OpticalCable


class ReferenceValueTests(TestCase):

    def test_cwdm_bands(self):
        self.assertEqual(CWDM_BANDS, [1271, 1291, 1311, 1331, 1351, 1371, 1391, 1411, 1431, 
                                      1451, 1471, 1491, 1511, 1531, 1551, 1571, 1591, 1611])


class WavelengthTests(TestCase):

    def test_instance_is_valid(self):
        w = OpticalWavelength('1550', 1550)
        self.assertIsInstance(w, OpticalWavelength)

    def test_str_representation(self):
        w = OpticalWavelength('1550', 1550)
        self.assertEqual(str(w), '1550nm')

    def test_instance_configuration(self):
        w = OpticalWavelength("1310", 1310)
        self.assertEqual(w.nominal_nm, 1310)


class OpticalCableTests(TestCase):

    def test_cable_instance_is_valid(self):
        cable = OpticalCable('F1-01', 1000)
        print(cable)
        self.assertIsInstance(cable, OpticalCable)

    def test_coeff_values(self):
        cable = OpticalCable('F1-01', 1000)
        print(cable)
        self.fail()
        #self.assertEqual(cable.loss_coeff, 0.04)