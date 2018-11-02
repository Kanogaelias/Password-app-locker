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
    