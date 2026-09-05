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

    #Gets the currency code used to retrieve the exchange rate from the API
    if user_choice == 1:
          user_currency = 'EUR'
          return user_currency
    elif user_choice == 2:
          user_currency = 'USD'
          return user_currency
    elif user_choice == 3:
          sys.exit()

def get_conversion_amount():
      while True:
            print('-- Please enter how much you wish to convert --')
            conversion_amount = input('>> £')
            print(' ')

            #Checks the inputted amount of money is a number
            if conversion_amount.isdigit() == True:
                  return conversion_amount
            elif conversion_amount.isdigit() == False:
                  print('Only numbers are allowed to be entered')
                  time.sleep(1)
                  print('Please try again')
                  time.sleep(1)

def get_conversion_result(user_currency):
      #Checks that the program can get responses from the REST API
      try:
            response = requests.get(
                  f"https://api.frankfurter.app/latest?from=GBP&to={user_currency}"
            )
            response.raise_for_status()
      except requests.RequestException:
            print('Unable to retrieve conversion rates')
            time.sleep(1)
            print('We apologise for this inconvenience')
            time.sleep(1)
            main_menu()

      #Puts the data from the API response into a JSON
      data = response.json()

      #Extracts the conversion rate from the JSON file
      conversionrate = data['rates'][user_currency]

      #Multiplies the amount the user inputted by the conversion rate, then rounds to 2 decimal places
      conversionresult = round((float(user_conversion_amount) * conversionrate),2)

      return conversionresult

def output_conversion(user_currency, user_conversion_amount, conversionresult):
      print('---- Converted Amount ----')
      print(' ')
      print(f'GBP: {user_conversion_amount}')
      print(f'{user_currency}: {conversionresult}')
      print(' ')
      print('-'*26)
      sys.exit()

user_currency = main_menu()
user_conversion_amount = get_conversion_amount()
conversionresult = get_conversion_result(user_currency)
output_conversion(user_currency, user_conversion_amount, conversionresult)