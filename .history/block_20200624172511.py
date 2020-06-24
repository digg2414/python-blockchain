def mine_block(last_block, data):


class Block(): 
    """
    Block: a unit of storage.
    Store transactions in a blockchain that supports a cryptocurrency.
    """
    
    def __init__(self, timestamp, last_hash ,data, hash): 
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
    
if __name__ == '__main__': 
    main()
