class Block(): 
    """
    Block: a unit of storage.
    Store transactions in a blockchain that supports a crypt
    """


class Blockchain(): 
    """
    Blockchain: a digital public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions.
    """
    
    def __init__(self):
        self.chain = []