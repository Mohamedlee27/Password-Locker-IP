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

    def generate_password(self):
        digits = "0123456789"
        symbols = "()[],;:_-/?#+"
        uppercase_letters = "ABCDEFGHIJKLMONPQRSTUVWXYZ"
        lowercase_letters = uppercase_letters.lower()
        upper, lower, nums, syms = True,True,True,True
        all = ''
        if upper:
            all += uppercase_letters
        if lower:
            all += lowercase_letters
        if nums:
            all += digits
        if syms:
            all += symbols

        length = 15
        amount = 5

        for x in range(amount):
         password = "".join(random.sample(all,length))

        return password 