"""
Hash function to create a fingerprint for each of our transactions
This hash function links each of our blocks to each other
"""
import hashlib
import json
import sys

def hashMe(msg=""):
    """define a helper function to wrap the python hash function"""

    # For convenience, this is a helper function that wraps our hashing algorithm
    if type(msg) != str:
        # If we don't sort keys, we can't guarantee repeatability!
        msg = json.dumps(msg, sort_keys=True)

    if sys.version_info.major == 2:
        # python 2.x, ignore the pylint error
        return unicode(hashlib.sha256(msg).hexdigest(), 'utf-8')
    else:
        return hashlib.sha256(str(msg).encode('utf-8')).hexdigest()
