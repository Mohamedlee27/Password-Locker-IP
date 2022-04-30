import unittest
from user import User

class testUser(unittest.TestCase):

     def setUp(self):


        self.new_user = User('Lee','Flash123')
    
     def tearDown(self):



        User.user_list = []



     def test_init(self):




        self.assertEqual(self.new_user.username,'Lee')
        self.assertEqual(self.new_user.password,'Flash123')