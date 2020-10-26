from hashlib import sha256
import json
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


    def hash(self, data:list=None):  # Create 
        if data == None:
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
            result = self.hash(result)

        return result
        

