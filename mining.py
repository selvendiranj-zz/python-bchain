"""
Putting it together: The final Blockchain Architecture
"""

import copy

from console import chain, state
from exchange import makeTransaction
from blocks import makeBlock
from chainvalidity import checkBlockValidity

nodeBchain = copy.copy(chain)
nodeBtxns  = [makeTransaction() for i in range(5)]
newBlock   = makeBlock(nodeBtxns, nodeBchain)

print('\n')
print("Blockchain on Node A is currently %s blocks long"%len(chain))

try:
    print("New Block Received; checking validity...", newBlock)
    # Update the state. this will throw an error if the block is invalid!
    state = checkBlockValidity(newBlock, chain[-1], state)
    chain.append(newBlock)
except:
    print("Invalid block; ignoring and waiting for the next block...")

print("Blockchain on Node A is now %s blocks long"%len(chain))
print('\n')
