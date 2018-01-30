"""
test all the building blocks of block chain
"""
import json
import blocks as bck
import exchange as exc
import transactions as txn
import blockchain as chn
import chainvalidity as chv

"""
Here are a set of sample transactions, some of which are fraudulent
but we can now check their validity!
"""
state = {u'Alice':5, u'Bob':5}  # Define the initial state
print('\n')
print(txn.isValidTxn({u'Alice': -3, u'Bob': 3}, state))  # Basic transaction. this works great!
print(txn.isValidTxn({u'Alice': -4, u'Bob': 3}, state))  # We can't create or destroy tokens!
print(txn.isValidTxn({u'Alice': -6, u'Bob': 6}, state))  # We can't overdraft our account.
print(txn.isValidTxn({u'Alice': -4, u'Bob': 2, 'Lisa':2}, state)) # Creating new users is valid
print(txn.isValidTxn({u'Alice': -4, u'Bob': 3, 'Lisa':2}, state)) # But the same rules still apply!

# create a large set of transactions, we will chunk them into blocks.
txnBuffer = [exc.makeTransaction() for i in range(30)]
state = {u'Alice':50, u'Bob':50}  # Define the initial state
chain = [bck.getGenesisBlock(state)] # Define the genesisBlock
state, chain = chn.buildBlockChain(txnBuffer, state, chain)

print('\n')
print('chainLength:', len(chain))
print('chaindata:', chain)
print('state:', state)

# check the validity of the state
print('\n')
print('chainValidity:', chv.checkChain(chain))

# if we are loading the chain from a text file, e.g. from backup or loading it for
# the first time, we can check the integrity of the chain and create the current state
chainAsText = json.dumps(chain,sort_keys=True)
print('chainValidity:', chv.checkChain(chainAsText))
