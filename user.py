import random
import string

class User:
    '''
    Class to manage user accounts.
    '''
    
    users_list = []
    def __init__(self, name,username, password) :
        """__init__ method to generate credentials objects.
         
        """
        self.name = name
        self.username = username
        self.password = password

    def save_user(self):
        """save_user method that saves user objects into the users list.
        """
        User.users_list.append(self)

    @classmethod
    def user_login(cls, username, password):
        """user_login that handles users logging in.
        """
        for user in cls.users_list:
            if user.username == username and user.password == password:
                return user

    def delete_user(self):
        """delete_user that removes a user from the list of users.
        """
        User.users_list.remove(self)
        
class Credentials:
    '''
    Class to generate credentials.
    '''
    accounts_list = []
    user_accounts = []
    def __init__(self, account_name, email, username, password, user):
        """__init__ method to help use define the properties of our credentials objects.
        """
        self.account_name = account_name
        self.email = email
        self.username = username
        self.password = password
        self.user = user


    def save_account(self):
        """save_account method saves credential objects into accounts_list
        """
        Credentials.accounts_list.append(self)
        
        
    @classmethod
    def set_password(cls,security):
        """set_password method that sets a given password.
        """
        return security



    @classmethod
    def display_accounts(cls, user):
        """display_accounts that loops through the accounts list and filters only those that belong to the currently logged in user.
        """
        for account in cls.accounts_list:
            if account.user == user:
                cls.user_accounts.append(account)
        return cls.user_accounts

    @classmethod
    def generate_password(cls,length):
        """generate_password method that generates a random password.
        """
        security = ''.join(random.choice(string.ascii_letters) for i in range(length))
        return security

    
    
    def delete_account(self):
        """delete_account method that removes a saved credential from the credentials list.
        """
        Credentials.accounts_list.remove(self)
