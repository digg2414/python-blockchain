class Block(): 
    """
    Block: a unit of storage.
    Store transactions in a blockchain that supports a cryptocurrency.
    """
    
    def __init__(self, timestamp, last_hash ,data, hash): 
        self.data = data
        self.timestamp = tmie
        
    def __repr__(self): 
        return f'Block: - data = {self.data}'
    
def main():
    block = Block('foo')
    print(block)
    print(f'block.py __name__: {__name__}')
    
if __name__ == '__main__': 
    main()
