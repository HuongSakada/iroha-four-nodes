from enum import Enum
import os, sys
from colorama import init, Fore, Style

from query import get_account_asset
from command import transfer_asset

class ControlType(Enum):
  TEXT = "Text"
  NUMBER = "Number"

direct = 'docker/keys'

def input_control(name, required = False, type = ControlType.TEXT):
  value = input(f"Please input {name}: ")

  while required == True and value == '':
    print(f"{Fore.RED}{name} is required")
    value = input(f"Please input {name}: ")
  
  if isinstance(type, ControlType):
    if type == ControlType.TEXT:
      return value
    elif type == ControlType.NUMBER:
      while True:
        try:
          value = int(value)
          break
        except ValueError:
          try:
            value = float(value)
            break
          except ValueError:
            print(f"{Fore.RED}{name} must be a number. Please input again!")
            value = input(f"Please input {name}: ")
            continue
    else:
      print(f'{Fore.YELLOW}[{type}]: Unknown control type!')
  else:
    print(f'{Fore.YELLOW}[{type}]: Invalid control type!')

  return value

def welcome():
  welcome = ' Welcome to Sora KH '
  print (f"{Fore.GREEN}\n{welcome.center(60, '#')}\n")

def check_account_id():
  account_id = input_control('Account Id', True)
  validity = os.path.exists(os.path.join(direct, f'{account_id}.priv'))
  
  while os.path.exists(os.path.join(direct, f'{account_id}.priv')) == False:
    print(f"{Fore.RED}Incorrect account id!")
    account_id = input_control('Account Id', True)

  return account_id

def command_list():
  print("""
    Please input the command number:
    1. Get asset info
    2. Transfer asset
    0. Exit
  """)

  return input_control('Command > ', True, ControlType.NUMBER)

def App():
  init(autoreset=True)
  welcome()
  account_id = check_account_id()
  command = command_list()
  private_key = open(os.path.join(direct, f'{account_id}.priv')).read()
  
  while True:
    if command == 1:
      print('\n')
      response = get_account_asset(
        account_id,
        account_id,
        private_key
      )
      for asset in response:
        print(f'{Fore.BLUE}{asset}')
      command = command_list()
    if command == 2:
      amount = input_control('Amount', True, ControlType.NUMBER)
      dest_account_id = input_control('Destination Account ID', True)
      asset_id = input_control('Asset ID', True)
      description = input_control('Description')

      res = transfer_asset(
        src_account_id=account_id,
        dest_account_id=dest_account_id,
        asset_id=asset_id,
        description='',
        amount=f"{amount}",
        creator_account_id=account_id,
        private_key=private_key
      )
      print(res)
      command = command_list()
    if command == 0:
      break
    else:
      print(f"{Fore.RED}Invalid command number!")
      command = command_list()
      continue
    
App()