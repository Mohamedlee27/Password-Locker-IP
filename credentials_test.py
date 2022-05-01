import unittest
from credentials import Credentials


class testCredentials(unittest.TestCase):
    '''
    A test class for testing the credential class 
    '''

    def setUp(self):
     '''Test a must to be initialized properly'''
     self.new_credentials=Credentials("Facebook",'Lee','Flash123')


    def test_init(self):
      '''method tests for proper initialization'''
      self.assertEqual(self.new_credentials.account,'Facebook')
      self.assertEqual(self.new_credentials.username,'Lee')
      self.assertEqual(self.new_credentials.password,'Flash123')

    
    def tearDown(self):
      '''A code to be executed to clean up after each test case has run'''
      Credentials.credentials_list = []

      
    def test_save_credentials(self):

       ''' tests if the Save credentials method works properly'''


       self.new_credentials.save_credentials()
       self.assertEqual(len(Credentials.credentials_list), 1)


    def test_save_credentials(self):
      '''Test dsave credentials to save class credentials'''
      self.new_credentials.save_credentials()
      test_credentials = Credentials('account', 'username','password')
      test_credentials.save_credentials()


    # def test_display_all_credentials(self):
    #  '''Method that returns a list of credentials'''
    #  self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)


    def test_login(self):
        ''' tests to get inside account'''
        self.new_credentials.save_credentials()
        login = Credentials('Lee','Flash123')
        login.save_credentials()
        check_account = Credentials.check_account('Lee', 'Flash123')
        self.assertTrue(check_account)




    def test_gen_password(self):
      ''' tests to generate password automatically'''
      self.new_credentials.generate_password()
      self.assertEqual(self.new_credentials.password, 'Flash123')

        
if __name__ == '__main__':
    unittest.main()