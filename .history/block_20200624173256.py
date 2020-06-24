import time

def mine_block(last_block, data):
   """  
   Mine a block based on the last_block and the data. 
   """
   timestamp = time.time_ns()
   last_hash = last_block.hash
   hash = f'{timestamp} - {last_hash}'
   
   return Block(timestamp, last_hash, hash, data)

def genesis(): 
    """ 
    Generate the Genesis Block.
    """
    
    return Block(1, 'genesis_last_hash', 'genesis_hash', [])

class Block(): 
    """
    Block: a unit of storage.
    Store transactions in a blockchain that supports a cryptocurrency.
    """
    
    def __init__(self, timestamp, last_hash, hash, data): 
        self.data = data
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        
    def __repr__(self): 
        return (
            'Block: ('
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, ' 
            f'hash: {self.hash}, '
            f'data: {self.data}'
        )
    
def main():
    block = Block('foo')
    print(block)
    print(f'block.py __name__: {__name__}')
    
    genesis_block = gene
    
if __name__ == '__main__': 
    main()
