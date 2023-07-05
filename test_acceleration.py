import unittest
import accelerate

class TestMovement(unittest.TestCase):

    def test_accel(self):
        result = accelerate.acceleration(7)
        self.assertEqual(result, True)

        result = accelerate.acceleration(1)
        self.assertEqual(result, False)

    # def test_time(self):
    #     result_1 = accelerate.time(0.01)
    #     self.assertEqual(result_1, False)

    def is_number(self, acceleration):
        try:
            float(acceleration)
            return True
        except ValueError:
            return False
    def is_string(self, acceleration):
        try:
            str(acceleration)
            return False
        except ValueError:
            return True

if __name__ == '__main__':
    unittest.main()