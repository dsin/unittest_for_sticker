import unittest

from am_i_handsome import am_i_handsome

class am_i_handsome_test(unittest.TestCase):
    def test_am_i_handsome(self):        
        self.assertEqual(am_i_handsome(), True)
        
if __name__ == '__main__':
    unittest.main()