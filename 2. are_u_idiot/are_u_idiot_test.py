import unittest

from are_u_idiot import are_u_idiot

class are_u_idiot_test(unittest.TestCase):

    def test_are_u_idiot_1(self):  
        name = 'Phong'
        self.assertEqual(are_u_idiot(name), False)

    def test_are_u_idiot_2(self):        
        name = 'Bob'
        self.assertEqual(are_u_idiot(name), True)
        
if __name__ == '__main__':
    unittest.main()