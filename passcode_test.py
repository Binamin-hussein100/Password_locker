import unittest
import random
import string
from passcode import Details


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
         

if __name__ == '__main__':
    unittest.main()