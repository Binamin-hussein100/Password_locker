import unittest
from user import User
from user import Credentials
# from user import User, Credentials


class Test_credentials(unittest.TestCase):
    """Test class that defines test cases for the credentials class behaviours."""
  

    def setUp(self):
        """setUp method to run before each test cases.
        """
        self.account1 = Credentials('Instagram', 'bin@mail.com', 'king_bin', '12345', 'bin')
        self.account2 = Credentials('pinterest', 'bin@mail.com', 'kingsman', '09876', 'sami')

    def tearDown(self):
        """tearDown method that does clean up after each test case has run.
        """
        Credentials.accounts_list = []

    def test_init(self):
        """test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.account1.account_name, 'Instagram')
        self.assertEqual(self.account1.email, 'bin@mail.com')
        self.assertEqual(self.account1.username, 'king_bin')
        self.assertEqual(self.account1.password, '12345')
        self.assertEqual(self.account1.user, 'bin')

    def test_save_account(self):
        """test_save_account test case to test if the credential object is saved into the credentials list
        """
        self.account1.save_account()
        self.account2.save_account()

        self.assertEqual(len(Credentials.accounts_list), 2)
        self.assertEqual(Credentials.accounts_list[0].account_name, 'Instagram')

    def test_generate_password(self):
        """test_set_password  test case to test whether we can generate a random password given a desired length.
        """
        self.assertEqual(len(Credentials.generate_password(5)), 5)

    def test_set_password(self):
        """test_set_password test case to test whether we can set a password for an object (both credentials and users) when creating one.
        """
        sec = Credentials.set_password('12345')

        self.assertEqual(sec, '12345')

    def test_display_contacts(self):
        """Method returns a list of all credentials whose owner is the currently logged in user, passed as an argument.
        """
        self.account1.save_account()
        self.account2.save_account()
        
        self.assertEqual(Credentials.display_accounts('sami'), Credentials.user_accounts)

    # def test_delete_account(self):
    #     """test_delete_account to test if we can remove a credential from our credentials list.
    #     """
    #     self.account1.save_account()
    #     self.account2.save_account()

    #     self.account1.delete_account()

    #     self.assertEqual(len(Credentials.accounts_list), 3)

class Test_user(unittest.TestCase):
    
    def setUp(self):
        """setUp method to run before each test cases.
        """
        self.user1 = User('salbin','forpeace', 'passcode')
        self.user2 = User('Hurwa','hussein', 'same')
    
    def tearDown(self):
        """tearDown method that does clean up after each test case has run.
        """
        User.users_list = []

    def test_init(self):
        """test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.user1.name, 'salbin')
        self.assertEqual(self.user1.username, 'forpeace')
        self.assertEqual(self.user1.password, 'passcode')

    def test_save_user(self):
        """test_save_user test case to test if the user object is saved into the users list
        """
        self.user1.save_user()
        self.user2.save_user()

        self.assertEqual(len(User.users_list), 2)
        self.assertEqual(User.users_list[0].username, 'forpeace')

    def test_user_login(self):
        """test_save_user test case to test if a user can log in with their username and password.
        """
        self.user1.save_user()
        self.user2.save_user()
        auth_user = User.user_login('forpeace', 'passcode')

        self.assertEqual(auth_user, self.user1)



if __name__ == '__main__':
    unittest.main()