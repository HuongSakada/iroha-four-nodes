from iroha import Iroha, IrohaGrpc, IrohaCrypto

network = IrohaGrpc('localhost:50051')

def sign_query(query, private_key):
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
  
  return data

def get_account_asset(account_id, creator_account_id, private_key):
  iroha = Iroha(creator_account_id)
  query = iroha.query(
    'GetAccountAssets', 
    account_id=account_id
  )

  response = sign_query(query, private_key)
  data = response.account_assets_response.account_assets

  return data

def get_signatories(account_id, creator_account_id, private_key):
  iroha = Iroha(creator_account_id)
  query = iroha.query(
    'GetSignatories',
    account_id=account_id
  )

  response = sign_query(query, private_key)
  
  return response