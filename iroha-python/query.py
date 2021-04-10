from iroha import Iroha, IrohaGrpc, IrohaCrypto
import os

root_account_id = 'root@sorakh'
bob_account_id = 'bob@sorakh'
alice_account_id = 'alice@sorakh'
usd_id = 'usd#sorakh'
khr_id = 'khr#sorakh'

direct = 'docker/keys'
root_private_key = open(os.path.join(direct, 'root@sorakh.priv')).read()
alice_private_key = open(os.path.join(direct, 'alice@sorakh.priv')).read()
bob_private_key = open(os.path.join(direct, 'bob@sorakh.priv')).read()

network = IrohaGrpc('localhost:50051')

def sign_query (query, private_key):
  IrohaCrypto.sign_query(query, private_key)
  data = network.send_query(query)

  return data

def get_account(account_id, creator_account_id, private_key):
  iroha = Iroha(creator_account_id)
  query = iroha.query(
    'GetAccount',
    account_id=account_id
  )

  response = sign_query(query, private_key)
  data = response.account_response
  print(data)

def get_account_asset(account_id, creator_account_id, private_key):
  iroha = Iroha(creator_account_id)
  query = iroha.query(
    'GetAccountAssets', 
    account_id=account_id
  )

  response = sign_query(query, private_key)
  data = response.account_assets_response.account_assets

  for asset in data:
    print(asset)

def get_signatories(account_id, creator_account_id, private_key):
  iroha = Iroha(creator_account_id)
  query = iroha.query(
    'GetSignatories',
    account_id=account_id
  )

  response = sign_query(query, private_key)
  print(response)

# get_account(alice_account_id, alice_account_id, alice_private_key)
# get_account_asset(bob_account_id, bob_account_id, root_private_key)
# get_signatories(alice_account_id, alice_account_id, alice_private_key)