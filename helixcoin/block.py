from hashlib import sha256
import time
from dataclasses import dataclass

"""
The Block Class
"""
@dataclass
class Block:
    index: int
    transactions: list
    timestamp: float
    previous_hash: str
    nonce: int


    @staticmethod
    def new(cls, index, previous_hash, transactions):  # Static Method to create new Block
        """
        If we make a method static using the @staticmethod decorator, we can call the method without initializing the class
        Now, we can create a new Block by doing Block.new(index, previous_hash, transactions)
        """
        return cls(
            index=index,
            transactions=transactions,
            timestamp=time.time(),
            previous_hash=previous_hash,
            nonce=0
        )

    def find_root(self, data:list=None):  # Calculate the merkle root of the function
        if data == None:  # If data is not specified the data is set to transactions
            data = self.transactions
            
        result = []
        for i,k in zip(data[0::2], data[1::2]):
            try:
                result_i = i.hash() 
                result_k = k.hash()
            except:
                result_i = sha256(str(i).encode()).hexdigest()
                result_k = sha256(str(k).encode()).hexdigest()

            result.append(sha256(f'{result_i}{result_k}'.encode()).hexdigest())

        if len(result) > 1:
            result = self.find_root(data=result)  # Recursion

        return result
        

