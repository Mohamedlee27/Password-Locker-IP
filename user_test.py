import unittest
from user import User

class testUser(unittest.TestCase):

     def setUp(self):


        self.new_user = User('Lee','Flash123')
    
     def tearDown(self):



        User.user_list = []



     def test_init(self):
      '''
    method tests for proper initialization
    '''
      self.assertEqual(self.new_user.username,'Lee')
      self.assertEqual(self.new_user.password,'Flash123')



     def test_save_user(self):
      '''
    test to enable user to save information
    '''
      self.new_user.save_user()
      self.assertEqual(len(User.user_list), 1) 



     def test_save_several_users(self):
      '''
    test to save several users at once
    '''
      self.new_user.save_user()
      test_user = User('username','password')
      test_user.save_user()
      self.assertEqual(len(User.user_list), 2)




     def test_see_all_accounts(self):
      '''
    test to reveal all the accounts
    '''
      self.assertEqual(User.my_credentials(),User.user_list)





     def test_find_account(self):
      '''
    test to serach for an account
    '''
      self.new_user.save_user()
      test_user = User('Lee','Flash123')
      test_user.save_user()
      found_account = User.find_by_user_name('Lee')
      self.assertEqual(found_account.password,test_user.password)




     def test_delete_account(self):

      '''
    test to remove the undesired account
    '''
      self.new_user.save_user()
      test_user = User('username','password')
      test_user.save_user()
      self.new_user.delete_user()
      self.assertEqual(len(User.user_list), 1)


if __name__ == '__main__':
   unittest.main()