from user import User
from credentials import Credentials

def create_account(username,password):

    new_account = Credentials(username,password)

    return new_account

def save_account(account):
    account.save_account()

    
def generate_password(account):
    account.generate_password()

def save_multiple_users(account): 

    account.save_multiple_users()

def my_accounts():   
    return User.my_accounts()  

def delete_accounts(account):  
    account.delete_accounts()

def create_credential(username,password):  
    new_credential = User(username,password)
    return new_credential

def save_user(credential):  

    credential.save_user()

def save_multiple_users(account): 

    account.save_multiple_users()

def my_accounts():   
    return User.my_accounts()  

def delete_accounts(account):  
    account.delete_accounts()



def main():
    print('Greetings and Welcome to PasswordLock!!!')
    print('Please Follow the instructions and Choose the following short codes and key them in to proceed: ')
    print('ca - to create an account')
    print('lg - to log in to your account')
