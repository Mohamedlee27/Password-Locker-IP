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

def main():
    print('Greetings and Welcome to PasswordLock!!!')
    print('Please Follow the instructions and Choose the following short codes and key them in to proceed: ')
    print('ca - to create an account')
    print('lg - to log in to your account')

    short_code = input().lower()
    if short_code == 'ca':
        print('username')
        username = input()
        print('\n')
        print('password')
        password = input()
        print('\n')
        save_account(create_account(username, password))    
        print('\n')
        print(f'Congratulations {username}, your account has been created successfully')
        print('\n')

    elif short_code == 'lg':
        print('\n')
        print('Choose and follow the following codes and press the keys to them in to proceed: ')
        print('cn - to create new credentials')
        print('dc - to display credentials')
        print('dc -delete credentials')
        print('fc - to find credentials')
        my_short_code = input().lower()
        print('\n')    