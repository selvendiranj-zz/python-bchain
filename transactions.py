"""
validate transactions and update balance(state) functions
"""

def updateState(txn, state):
    """
    We will take the first k transactions from the transaction buffer, and turn them into a block
    """
    # Inputs: txn, state: dictionaries keyed with account names,
    # holding numeric values for transfer amount (txn) or account balance (state)
    # Returns: Updated state, with additional users added to state if necessary
    # NOTE: This does not not validate the transaction, just updates the state!

    # If the transaction is valid, then update the state
    # As dictionaries are mutable, let's avoid any confusion
    # by creating a working copy of the data.
    state = state.copy()
    for key in txn:
        if key in state.keys():
            state[key] += txn[key] # Update balance for existing account
        else:
            state[key] = txn[key] # Add balance to new account
    return state


def isValidTxn(txn, state):
    """
    Before we put transactions into blocks, we need to define a method for checking
    the validity of the transactions we've pulled into the block
    """
    # Assume that the transaction is a dictionary keyed by account names

    # Check that the sum of the deposits and withdrawals is 0
    if sum(txn.values()) is not 0:
        return False

    # Check that the transaction does not cause an overdraft
    for key in txn.keys():
        if key in state.keys():
            acct_balance = state[key]
        else:
            acct_balance = 0

        if (acct_balance + txn[key]) < 0:
            return False

    return True
