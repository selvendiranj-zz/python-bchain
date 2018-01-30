"""
Building the Blockchain: From Transactions to Blocks
"""
import json
import fingerprint as fgp

# Great! This becomes the first element from which everything else will be linked.
def getGenesisBlock(state):
    """
    Generate a genesis block from the intial state
    """
    genesisBlockTxns = [state]
    genesisBlockContents = {
        u'blockNumber':0,
        u'parentHash':None,
        u'txnCount':1,
        u'txns':genesisBlockTxns}
    genesisHash = fgp.hashMe(genesisBlockContents)
    genesisBlock = {u'hash': genesisHash, u'contents': genesisBlockContents}
    genesisBlockStr = json.dumps(genesisBlock, sort_keys=True)

    print('\n')
    print('genesisBlockTxns:', genesisBlockTxns)
    print('genesisBlockContents:', genesisBlockContents)
    print('genesisHash:', genesisHash)
    print('genesisBlock:', genesisBlock)
    print('genesisBlockStr:', genesisBlockStr)

    return genesisBlock


def makeBlock(txns, chain):
    """
    For each block, we want to collect a set of transactions,
    create a header, hash it, and add it to the chain
    """
    parentBlock = chain[-1]
    parentHash = parentBlock[u'hash']
    blockNumber = parentBlock[u'contents'][u'blockNumber'] + 1
    txnCount = len(txns)
    blockContents = {u'blockNumber':blockNumber, u'parentHash':parentHash,
                     u'txnCount':len(txns), 'txns':txns}
    blockHash = fgp.hashMe(blockContents)
    block = {u'hash':blockHash, u'contents':blockContents}

    return block
