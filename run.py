from user import User
from credentials import Credentials

def create_account(username,password):

    new_account = Credentials(username,password)

    return new_account

def save_account(account):
    account.save_account()

    
def generate_password(account):
    account.generate_password()