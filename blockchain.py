"""
process our transaction buffer into a set of blocks
"""
import sys
import blocks as bck
import transactions as txn

blockSizeLimit = 5  # Arbitrary number of transactions per block
                    # this is chosen by the block miner, and can vary between blocks!

def buildBlockChain(txnBuffer, state, chain):
    while len(txnBuffer) > 0:
        """Construct chain of blocks"""
        bufferStartSize = len(txnBuffer)

        ## Gather a set of valid transactions for inclusion
        txnList = []

        while (len(txnBuffer) > 0) & (len(txnList) < blockSizeLimit):
            newTxn = txnBuffer.pop()
            validTxn = txn.isValidTxn(newTxn, state) # This will return False if txn is invalid

            if validTxn: # If we got a valid state, not 'False'
                txnList.append(newTxn)
                state = txn.updateState(newTxn, state)
            else:
                print("ignored transaction")
                sys.stdout.flush()
                continue  # This was an invalid transaction; ignore it and move on

        ## Make a block
        myBlock = bck.makeBlock(txnList, chain)
        chain.append(myBlock)
    return state, chain
