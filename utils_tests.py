import unittest
from utils import utils

class TestUtils(unittest.TestCase):
    
    # --- Tests for reversed function ---
    def test_reversed_with_integers(self):
        """Test reversed function with integer inputs."""
        self.assertEqual(utils.reversed(123), 321)
        self.assertEqual(utils.reversed(-456), -654)
        self.assertEqual(utils.reversed(0), 0)

    def test_reversed_with_floats(self):
        """Test reversed function with float inputs (expecting conversion or value error)."""
        with self.assertRaises((ValueError, TypeError)):
            utils.reversed(12.34)

    def test_reversed_with_strings(self):
        """Test reversed function with string inputs (expecting type/value error)."""
        with self.assertRaises((ValueError, TypeError)):
            utils.reversed("123")

    # --- Tests for formatter function ---
    def test_formatter_with_integers(self):
        """Test formatter function with integer inputs."""
        self.assertEqual(utils.formatter(5), ('0b101', '0o5'))
        self.assertEqual(utils.formatter(0), ('0b0', '0o0'))

    def test_formatter_with_floats(self):
        """Test formatter function with float inputs (expecting TypeError for binary/octal)."""
        with self.assertRaises(TypeError):
            utils.formatter(5.5)

    def test_formatter_with_strings(self):
        """Test formatter function with string inputs (expecting TypeError for binary/octal)."""
        with self.assertRaises(TypeError):
            utils.formatter("5")

if __name__ == '__main__':
    unittest.main()
