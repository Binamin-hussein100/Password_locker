import unittest
import pyperclip



class TestDetails(unittest.TestCase):
    """
    unittest.TestCase: TestCase class that helps us in creating testcases
    """
    
    def setUp(self):
        """
        method to run before each test case
        """
        self.new_details = Details("Binamin","123456")
        
    def test_check(self):
        """
        check for proper initialization
        """
        self.assertEqual(self.new_details.name,"Binamin")
        self.assertEqual(self.new_details.passcode,"123456")
       
    def test_save(self):
        """
        object saved into contact list
        """
        self.new_details.save()
        self.assertEqual(len(Details.storage_list),1)
    
    def tearDown(self):
        """
        clears the list after each case is run
        """
        Details.storage_list = []  
        
    
class TestCredencials(unittest.TestCase):
    
    

if __name__ == '__main__':
    unittest.main()