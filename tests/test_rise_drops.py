import unittest
from services.process_rise_drops import RiseDropProcessor


class TestInputs(unittest.TestCase):
    OUTPUT_ERROR = 'Output does not match'

    def test_1(self):
        a = RiseDropProcessor([(1, 5, 10), (4, 6, 8), (10, 15, 10), (11, 12, 8)])
        a.process_rise_and_drops()
        self.assertEqual(a.result_set, [(1, 10), (5, 8), (6, 0), (10, 10), (15, 0)], self.OUTPUT_ERROR)

    def test_2(self):
        a = RiseDropProcessor([(1, 10, 4), (1, 8, 6), (1, 6, 8)])
        a.process_rise_and_drops()
        self.assertEqual(a.result_set, [(1, 8), (6, 6), (8, 4), (10, 0)], self.OUTPUT_ERROR)

    def test_3(self):
        a = RiseDropProcessor([(0, 6, 2), (5, 10, 8), (7, 8, 12)])
        a.process_rise_and_drops()
        self.assertEqual(a.result_set, [(0, 2), (5, 8), (7, 12), (8, 8), (10, 0)], self.OUTPUT_ERROR)


if __name__ == "__main__":
    unittest.main()
