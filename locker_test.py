from locker import Credentials,UsersData
import unittest, pyperclip

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines the test cases for creating and authenticating credentials
    '''
    def setUp(self):
        '''
        Setting up the structure before each test
        '''
        self.new_user = Credentials(1,"richie","uiui")
        
    def tearDown(self):
        '''
        Cleans up after each test has run
        '''
        Credentials.users_list = []
    
    def test_init(self):
        '''
        Test case to test if the case has been initialized properly
        '''
        self.assertEqual(self.new_user.identify,1)
        self.assertEqual(self.new_user.user_name,"richie")
        self.assertEqual(self.new_user.password,"uiui")