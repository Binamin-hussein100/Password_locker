import pyperclip
from credencials_all import Credencials

class Details:
    """
    generates new instances of account 
    """
    
    storage_list = []
    def __init__(self,Username,password,user):
        self.name = Username
        self.passcode = password
        self.user = user
        
    def save(self):
        """
        saves users to the storage list
        """
        Details.storage_list.append(self)
    
    # @classmethod
    # def display_accounts(cls,user):
    #     for account in cls.credencials_list:
    #         if account.user == user:
    #             cls.user_accounts
    
    @classmethod
    def log_in(cls,profile_name,sec):
        for user in storage_list:
            if user.profile_name == profile_name and user.password == sec:
                return user 
    