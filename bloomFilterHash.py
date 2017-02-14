'''
Bloom Filter lab - Hash Functions
CS237, Sharon Goldberg
'''
import numpy as np
import hashlib
class bloomFilterHash(object):
    '''
    hash utilizing the hashlib in Python. It only works for array lengths which are
    multiples of F in hexadecimal - that is F = 15, FF = 255, FFF= 4095 etc.
    '''    
    def hash_i(self, key, i):
        h = hashlib.sha1(str(i))
        h.update(str(key))
        hashArray = h.hexdigest()
        hashVal = ''
        count = 0
        for i in range(len(hex(self.numBits)) - 2):
            hashVal += hashArray[i]
            count += 1
        hashVal = int(hashVal, 16) - 1
        return hashVal 
        
        
    '''
    pairwiseHash_i utilizes pairwise independent hash functions. 
    '''
   
    def pairwiseHash_i(self, key, i):
        (a,b) = self.pairwiseHashFunctions[i]
        return int(((a*float(key) + b) % 20333) % self.numBits)
    
    '''
    Constructor
    '''
    def __init__(self, numBits, numHashFunctions):
        self.numBits = numBits
        self.numHashFunctions = numHashFunctions
        self.pairwiseHashFunctions = [0]*numBits
        #Generate pairwise-independent hash functions
        for i in range(self.numBits):
            a = np.random.randint(20333)
            b = np.random.randint(20333)            
            self.pairwiseHashFunctions[i]= (a,b)    
        return 
