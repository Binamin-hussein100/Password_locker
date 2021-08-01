class Details:
    """
    generates new instances of details  
    """
    
    storage_list = []
    def __init__(self,Username,password):
        self.name = Username
        self.passcode = password
        
    def save(self):
        Details.storage_list.append(self)