"""
Checking Chain Validity
"""

import json
import fingerprint as fgp
import transactions as tns


# A simple helper function that makes sure that the block contents match the hash
def checkBlockHash(block):
    # Raise an exception if the hash does not match the block contents
    expectedHash = fgp.hashMe(block['contents'])
    if block['hash'] != expectedHash:
        raise Exception('Hash does not match contents of block %s'%
                        block['contents']['blockNumber'])
    return

# A simple helper function that makes sure that the block transactions are valid
def checkBlockTxns(block, blockNumber, state):
    # Check transaction validity; throw an error if an invalid transaction was found.
    for txn in block['contents']['txns']:
        if tns.isValidTxn(txn, state):
            state = tns.updateState(txn, state)
        else:
            raise Exception('Invalid transaction in block %s: %s'%(blockNumber, txn))
    return state

# Checks the validity of a block, given its parent and the current system state.
# We want this to return the updated state if the block is valid, and raise an error otherwise.
def checkBlockValidity(block, parent, state):    
    """
    Check the txns in block, hash, parentHash, blocknumber
    """
    parentNumber = parent['contents']['blockNumber']
    parentHash = parent['hash']
    blockNumber = block['contents']['blockNumber']

    # Check for transaction validity
    state = checkBlockTxns(block, blockNumber, state)

    # Check hash integrity; raises error if inaccurate
    checkBlockHash(block)

    # Check blocknumber incremented the parent blocknumber by 1
    if blockNumber != (parentNumber+1):
        raise Exception('Hash does not match contents of block %s'%blockNumber)

    # Check block accurately references the parent block's hash
    if block['contents']['parentHash'] != parentHash:
        raise Exception('Parent hash not accurate at block %s'%blockNumber)

    return state

# Check the validity of the entire chain, and compute the system state
# beginning at the genesis block. This will return the system state if the chain is valid,
# and raise an error otherwise
def checkChain(chain):
    """
    Work through the chain from the genesis block (which gets special treatment),
      checking that all transactions are internally valid,
        that the transactions do not cause an overdraft,
        and that the blocks are linked by their hashes.
      This returns the state as a dictionary of accounts and balances,
        or returns False if an error was detected
    """
    ## Data input processing: Make sure that our chain is a list of dicts
    if type(chain) == str:
        try:
            chain = json.loads(chain)
            assert(type(chain) == list)
        except:  # This is a catch-all, admittedly crude
            return False
    elif type(chain) != list:
        return False

    state = {}
    ## Prime the pump by checking the genesis block
    # We want to check the following conditions:
    # - Each of the transactions are valid updates to the system state
    # - Block hash is valid for the block contents

    for txn in chain[0]['contents']['txns']:
        state = tns.updateState(txn, state)

    checkBlockHash(chain[0])
    parent = chain[0]

    ## Checking subsequent blocks: These additionally need to check
    #    - the reference to the parent block's hash
    #    - the validity of the block number
    for block in chain[1:]:
        state = checkBlockValidity(block, parent, state)
        parent = block

    return state
