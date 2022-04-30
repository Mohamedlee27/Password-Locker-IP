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