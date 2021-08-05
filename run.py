#!/usr/bin/env python3
from os import name
from random import choice
from user import User
from user import Credentials

def create_user(Name,username,password):
    new_user = User(Name,username,password)
    return new_user

def save(user):
    """saves user"""
    user.save_user()
    
def delete_user(user):
    """deletes users"""
    user.delete_user()

def account(account_name, email, username, password, user):
    """
    create new account
    """
    new_account = Credentials(account_name, email, username, password, user)
    return new_account

def save(account):
    """
    saves a credencial
    """
    account.save_account()
  
def setting_password():
    return Credentials.set_password()
    
def display_accounts(user):
    accounts = Credentials.display_accounts(user)
    return accounts

def delete(account):
    """deletes account"""
    account.delete_account()
    
       
    
def random_pass(length):
    """
    creates new random password
    """
    return Credentials.generate_password(length)

def main():
    print("Welcome. we are honoured to have you here")
    
    while True:
        print("What would you like to do? (enter number to select")
        print('--'*25)
        print("CD-create new user.\n LOG-log in into an existing account.\n DEL-remove a user. \n EXIT-to exit")   
        option = input("Enter your option: ")
        
        if option == "CD":
            print("Create user")
            Name = input("Your name: ")
            username = input("User name: ")
            password = input("User password" )
            
            save(create_user(Name,username,password))
            
            print(f"\nNew user {Name} created\n\n")
            
        
# if __name__ == '__main__':
#     main()            