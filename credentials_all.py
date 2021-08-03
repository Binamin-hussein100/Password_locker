import pyperclip
from passcode import Details

class Credencials:
    
    credencials_list = []
    def __init__(self,user_name,email,account,password):
        self.user_name = profile_name
        self.account = account
        self.password = security
        self.email = user_email
        
    def save_account(self):
        """
        save accounts to the credencials list
        """
        Credencials.credencials_list.append(self)
        
    def random_generate_pass(cls,pass_length):
        """
        auto_generate password
        """
        sec = ''.join(random.choice(string.ascii_letters)for in range(pass_length))
        return sec
    
    def delete(self):
        """
        method to delete saved credencials
        """
        Credencials.credencials_list.remove(self)
    
