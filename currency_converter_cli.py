import requests

import time

import sys

def main_menu():
    print('----- Currency Converter -----')
    print(' ')
    print('1. GBP -> EUR')
    print('2. GBP -> USD')
    print('3. Exit')
    print(' ')

    # Checks that the input is a number
    # Also checks that the input is one of the menu options
    while True:
            try:
                user_choice = int(input('>> '))
                options_list = [1,2,3]
                if user_choice in options_list:
                      break
                elif user_choice not in options_list:
                      print('Please choose an option listed on the Menu')
                      time.sleep(1)
                      print('Please try again')
                      time.sleep(1)
            except ValueError:
                  print('Please input a number')
                  time.sleep(1)
                  print('Please try again')
                  time.sleep(1)

    #Gets the currency code used to gather the exchange rate from the API
    if user_choice == 1:
          user_currency = 'EUR'
    elif user_choice == 2:
          user_currency = 'USD'
    elif user_choice == 3:
          sys.exit()
          
main_menu()