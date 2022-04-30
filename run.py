from user import User
from credentials import Credentials

def create_account(username,password):

    new_account = Credentials(username,password)

    return new_account

def save_account(account):
    account.save_account()

    
def generate_password(account):
    account.generate_password()
    
def save_multiple_users(account): #function that saves multiple credentials

    account.save_multiple_users()

def my_accounts():   #function that displays credentials
    return User.my_accounts()  

def delete_accounts(account):  #function that deletes credentials
    account.delete_accounts()
