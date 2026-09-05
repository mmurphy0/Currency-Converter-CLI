# Currency Converter CLI

### I am using this project to practice using docker for the first time. So I will not be adding more currencies at the moment

## Description
A Python Command Line Interface which lets people convert Great British Pounds (£) using the currencies listed below:

- Euro (EUR)

- United States Dollar (USD)

This project uses the Frankfurter API for live exchange rates:

https://api.frankfurter.app

No API key is required.

## Usage

- The main menu is displayed where the User is shown a list of the currencies they can convert to
  - The User can type in the number of the currency they wish to convert to
  - If the user does typed in an invalid option, they will be instructed to retry until they have inputted a valid option

- When a currency has been chosen, the User will be prompted to type how many pounds they wish to convert to their chosen currency
  - If a number has not been entered, the User will be instructed to retry until a number has been inputted   

- The conversion rate is retrieved from the Frankfurter REST API which is used to calculate the converted amount
  - If the program cannot connect to the API, The user will be informed of this and returned to the main menu
    - The message to the user is the backup option to keep the program working      
 
- The User will be shown the converted amount and must type 'Return' to be returned back to the main menu

## Tech Stack
- Python 3

- Docker (Coming soon)

- Requests (HTTP client)

- Frankfurter API (exchange rates)
