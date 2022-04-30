import random

class Credentials:
    '''
    class that helps the users get their account
    '''

    credentials_list = []

    def __init__(self, account, username, password):
        self.account = account
        self.username = username
        self.password = password

    def save_credentials(self):
        '''Saves the  credentials in the  credentials list.'''
        Credentials.credentials_list.append(self)
        
    # def delete_credentials(self):
    #     Credentials.credentials_list.remove(self)

    # @classmethod
    # def display_credentials(cls, account):
    #     return cls.credentials_list

    @classmethod
    def check_account(cls, account, username, password):
        for credential in cls.credentials_list:
            if credential.account == account and credential.username == username and credential.password == password:
                return True
        return False 