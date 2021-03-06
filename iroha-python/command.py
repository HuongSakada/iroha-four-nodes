from iroha import Iroha, IrohaGrpc, IrohaCrypto
from colorama import Style

network = IrohaGrpc('localhost:50051')

def sign_transaction(transaction_tx, private_key):
  IrohaCrypto.sign_transaction(transaction_tx, private_key)
  network.send_tx(transaction_tx)
  tx_status_stream = network.tx_status_stream(transaction_tx)

  for status in tx_status_stream:
    print(f'{Style.DIM}{status}')

  return status
    
def add_asset_quantity(asset_id, amount, creator_account_id, private_key):
  iroha = Iroha(creator_account_id)
  transaction_tx = iroha.transaction(
    [
      iroha.command(
        'AddAssetQuantity',
        asset_id=asset_id,
        amount=amount
      )
    ]
  )
  status = sign_transaction(transaction_tx, private_key)

  return status

def transfer_asset(**kwargs):
  iroha = Iroha(kwargs['creator_account_id'])
  transaction_tx = iroha.transaction(
    [
      iroha.command(
        'TransferAsset',
        src_account_id=kwargs['src_account_id'],
        dest_account_id=kwargs['dest_account_id'],
        asset_id=kwargs['asset_id'],
        description=kwargs['description'],
        amount=kwargs['amount']
      )
    ]
  )
  status = sign_transaction(transaction_tx, kwargs['private_key'])

  return status

def add_signatory(account_id, public_key, creator_account_id, private_key):
  iroha = Iroha(creator_account_id)
  transaction_tx = iroha.transaction(
    [
      iroha.command(
        'AddSignatory',
        account_id=account_id,
        public_key=public_key
      )
    ]
  )
  status = sign_transaction(transaction_tx, private_key)

  return status

def remove_signatory(account_id, public_key, creator_account_id, private_key):
  iroha = Iroha(creator_account_id)
  transaction_tx = iroha.transaction(
    [
      iroha.command(
        'RemoveSignatory',
        account_id=account_id,
        public_key=public_key
      )
    ]
  )
  status = sign_transaction(transaction_tx, private_key)

  return status

def set_account_quorum(account_id, quorum, creator_account_id, private_key):
  iroha = Iroha(creator_account_id)
  transaction_tx = iroha.transaction(
    [
      iroha.command(
        'SetAccountQuorum',
        account_id=account_id,
        quorum=quorum
      )
    ]
  )
  status = sign_transaction(transaction_tx, private_key)

  return status

def grant_permission(account_id, permission, creator_account_id, private_key):
  iroha = Iroha(creator_account_id)
  transaction_tx = iroha.transaction(
    [
      iroha.command(
        'GrantPermission',
        account_id=account_id,
        permission=permission
      )
    ]
  )
  status = sign_transaction(transaction_tx, private_key)

  return status

def revoke_permission(account_id, permission, creator_account_id, private_key):
  iroha = Iroha(creator_account_id)
  transaction_tx = iroha.transaction(
    [
      iroha.command(
        'RevokePermission',
        account_id=account_id,
        permission=permission
      )
    ]
  )
  status = sign_transaction(transaction_tx, private_key)

  return status

# add_asset_quantity(
#   khr_id,
#   '1000000',
#   root_account_id,
#   root_private_key
# )

# transfer_asset(
#   src_account_id=alice_account_id,
#   dest_account_id=bob_account_id,
#   asset_id=usd_id,
#   description='',
#   amount='1',
#   creator_account_id=alice_account_id,
#   private_key=alice_private_key
# )

# add_signatory(
#   alice_account_id,
#   bob_public_key,
#   alice_account_id,
#   alice_private_key
# )
# remove_signatory(
#   alice_account_id,
#   bob_public_key,
#   alice_account_id,
#   alice_private_key
# )

# set_account_quorum(
#   alice_account_id,
#   2
# )

# grant_permission(
#   bob_account_id,
#   primitive_pb2.can_transfer_my_assets,
#   alice_account_id,
#   alice_private_key
# )
# revoke_permission(
#   bob_account_id,
#   primitive_pb2.can_transfer_my_assets,
#   alice_account_id,
#   alice_private_key
# )
