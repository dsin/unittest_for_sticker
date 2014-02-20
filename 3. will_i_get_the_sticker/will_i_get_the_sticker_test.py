import unittest

from will_i_get_the_sticker import Question

class will_i_get_the_sticker_test(unittest.TestCase):
    def setUp(self):
        self.question = Question()

    def test_will_i_get_the_sticker_1(self):        
        admin_name = 'Bob'
        self.assertEqual(self.question.will_i_get_sticker(admin_name), False)
        
    def test_will_i_get_the_sticker_2(self):        
        admin_name = 'Ann'
        self.assertEqual(self.question.will_i_get_sticker(admin_name), True)
        
    def test_will_i_get_the_sticker_3(self):        
        admin_name = 'Other name you can imagine in the world'
        self.assertEqual(self.question.will_i_get_sticker(admin_name), True)
        
if __name__ == '__main__':
    unittest.main()