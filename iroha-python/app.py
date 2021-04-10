from enum import Enum
import os
from query import get_account_asset
from command import transfer_asset

class ControlType(Enum):
  TEXT = "Text"
  NUMBER = "Number"

direct = 'docker/keys'
CRED = '\033[91m'
CEND = '\033[0m'

def input_control(name, required = False, type = ControlType.TEXT):
  value = input(f"Please input {name}: ")

  while required == True and value == '':
    print(f"{CRED}{name} is required{CEND}")
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
            print(f"{CRED}{name} must be a number. Please input again!{CEND}")
            value = input(f"Please input {name}: ")
            continue
    else:
      print('Invalid input!')
  else:
    print('Invalid input!')

  return value
def welcome ():
  print("""\x1b[6;30;42m

  Welcome to Sora Testnet 
  \x1b[0m
  """)
  return input_control('Account Id', True)
def command_list():
  print("""
    Please input the command number:
    1. Get asset info
    2. Transfer asset
    0. Exit
  """)
  return input_control('Command > ', True, ControlType.NUMBER)

def init():
  account_id = welcome()
  command = command_list()
  private_key = open(os.path.join(direct, f'{account_id}.priv')).read()
  while True:
    if command == 1:
      print('\n')
      get_account_asset(
        account_id,
        account_id,
        private_key
      )
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
      print(f"{CRED}Invalid command number!{CEND}")
      command = command_list()
      continue
    

init()