from pydoc import doc


class User: 
    '''
    class that generates new instances of users
    '''

    user_list = []

    def __init__(self,username,password): 
        '''
        The __init__ method helps to define properties for our objects.The __init__ function is called every time an object is created from a class.
        '''
        
        self.username = username
        self.password = password
    
    def save_user(self):
        '''
        Save_user method saves the user object into the user list.
        '''


        User.user_list.append(self)

    def delete_user(self):
         '''
        delete_user method deletes the user object from the user list.
        '''



         User.user_list.remove(self)


         
    @classmethod
    def my_credentials(cls):



        return cls.user_list

    @classmethod
    def find_by_user_name(cls,username):



        for account in cls.user_list:
            if account.username == username:

                return account
