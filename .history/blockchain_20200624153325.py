from block import Block

class Blockchain(): 
    """
    Blockchain: a digital public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions.
    """
    
    def __init__(self):
        self.chain = []
        
    def add_block(self, data): 
        self.chain.append(Block(data))
        
    def __repr__(self):
        return f'Blockchain: {self.chain}'
        


print(blockchain)
print(f'blockchain.py __name__: {__name__}')
