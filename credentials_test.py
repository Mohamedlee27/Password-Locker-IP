import unittest
from credentials import Credentials


class testCredentials(unittest.TestCase):
    '''
    A test class for testing the credential class 
    '''

    def setUp(self):

     self.new_credentials=Credentials("Facebook",'Lee','Flash123')
    
     def tearDown(self):
      '''A code to be executed to clean up after each test case has run'''
    
     Credentials.credentials_list = []

    def test_init(self):


      '''method tests for proper initialization'''


      self.assertEqual(self.new_credentials.account,'Facebook')
      self.assertEqual(self.new_credentials.username,'Lee')
      self.assertEqual(self.new_credentials.password,'Flash123')