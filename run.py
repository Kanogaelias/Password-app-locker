#!/usr/bin/env python3.6
import string,random,time
from locker import Credentials,UsersData

def new_account(id,user_name,password):
    '''
    Function to creating new account
    '''
    new_user = Credentials(id,user_name,password)
    return new_user

def create_user(user):
    '''
    Function that saves the user's credentials
    '''
    user.create_account()

def authenticate(username,passkey):
    '''
    Function responsible for signing in
    '''
    return Credentials.authenticate_account(username,passkey)


def my_new_data(user_id,data_id,website,web_key):
    '''
    Function that creates new data for storing password
    '''
    new_data = UsersData(user_id,data_id,website,web_key)
    return new_data

def add_data(data):
    '''
    Function that saves the new data created
    '''
    data.add_password()

def display_data(data,number):
    '''
    Function that displays the user data
    '''
    return UsersData.display_data(data,number)