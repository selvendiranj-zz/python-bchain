"""
Create a function to generate exchanges between Alice and Bob.
We'll indicate withdrawals with negative numbers, and deposits with positive numbers.
We'll construct our transactions to always be between the two users of our system
and make sure that the deposit is the same magnitude as the withdrawal
i.e. we're neither creating nor destroying money
"""

import random
random.seed(0)

def makeTransaction(max_value=3):
    """This will create valid transactions in the range of (1, maxValue)"""

    sign = int(random.getrandbits(1)) * 2 - 1   # This will randomly choose -1 or 1
    amount = random.randint(1, max_value)

    alice_pays = sign * amount
    bob_pays = -1 * alice_pays

    # By construction, this will always return transactions
    # that respect the conservation of tokens.
    # However, note that we have not done anything to check
    # whether these overdraft an account
    return {u'Alice': alice_pays, u'Bob': bob_pays}
