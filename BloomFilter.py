'''
Bloom Filter
'''
from bloomFilterHash import bloomFilterHash 
import numpy.random as rnd
import matplotlib.pyplot as plt

class BloomFilter(object):
    #Class Variables
    numBits = 0
    bitArray = [0]
    numHashFunctions = 0
    # 16    
    pairwise = False
    # 21
    badInserts = []
    badLookups = []
    personalBF = []    
    
    # 9, 16
    '''Insert function, pass it a key and insert into bloom filter'''
    def insert(self, key):
        if self.pairwise == True:
            for i in range(1, 1 + self.numHashFunctions):
                hashValue = self.hash.pairwiseHash_i(key, i)           
                self.bitArray[hashValue] = 1
        else:
            for i in range(1, 1 + self.numHashFunctions):
                hashValue = self.hash.hash_i(key, i)           
                self.bitArray[hashValue] = 1
        
    '''Lookup function, pass it a key and return true or false'''
    def lookup(self, key):
        if self.pairwise == True:
            for i in range(1, 1 + self.numHashFunctions):
                hashValue = self.hash.pairwiseHash_i(key, i)
                if self.bitArray[hashValue] == 0:
                    return False
        else:
            for i in range(1, 1 + self.numHashFunctions):
                hashValue = self.hash.hash_i(key, i)
                if self.bitArray[hashValue] == 0:
                    return False
        return True
        
    # 10
    '''Insert function, insert a data randomly generated from [0, 10^8]'''
    def rand_inserts(self):
        data = str(rnd.randint(0, 10 ** 8))
        self.insert(data)
        
    # 21
    def adversarialInserts(self):
        self.personalBF = [0]*self.numBits
        self.badInserts = []
        count = 0
        for i in range (16384):
            flag = True
            val = [0] * self.numHashFunctions
            for j in range (self.numHashFunctions):
                val[j] = self.hash.pairwiseHash_i(i, j)
                if self.personalBF[val[j]] != 0:
                    flag = False
            if flag:
                self.badInserts.append(val[j])
                for j in range (self.numHashFunctions):
                    count += 1
                    self.personalBF[val[j]] = 1
        for i in range(len(self.badInserts)):
            self.insert(self.badInserts[i])
        return self.badInserts

    def adversarialLookups(self):
        self.badLookups = []
        for i in range (16384):
            if i not in self.badInserts:
                if self.lookup(i):
                    self.badLookups.append(i)
        count = 0
        for i in range (len(self.badLookups)):
            if self.lookup(self.badLookups[i]):
                count += 1
        return count * 1.0 / len(self.badLookups)    
    
    # 16
    '''Constructor, input: number of bits, number of hash functions, boolean'''
    def __init__(self, numBits, numHashFunctions, pairwise):
        self.numBits = numBits
        self.bitArray = [0] * numBits
        self.numHashFunctions = numHashFunctions
        self.pairwise = pairwise
        self.hash = bloomFilterHash(numBits, numHashFunctions)

# 12
'''calculate average false positive probability
   input: k hash functions, n bits, m insertions '''
def avg_fpp(k, n, m):
    bloom = BloomFilter(n,k)
    for i in range(m):
        bloom.rand_inserts()
        
    total_fpp = 0
    for experiment in range(1000):
        # print "experiment: " + str(experiment)
        numPositive = 0
        
        for lookup in range(10000):
            data = str(rnd.randint(0, 10 ** 8))
            if bloom.lookup(data) == True:
                numPositive += 1
        
        fpp = numPositive / 10000.0
        total_fpp += fpp
    avg_fpp = total_fpp / 1000.0
    print avg_fpp

# avg_fpp(10, 4095, 600)

# 13
'''plot average false positive probability for k in {2,...,30}'''
def plot_k_fpp():
    k_list = [i for i in range(2, 31)]
    #print k_list
    fpp_list = []
    for k in k_list:
        fpp = avg_fpp(k, 4095, 600)
        fpp_list.append(fpp)
    
    #print fpp_list    
    plt.figure(1)
    plt.plot(k_list, fpp_list, 'o')
    plt.xlabel("Number of Hash Functions")
    plt.ylabel("False Positive Probability")
    plt.show()  
    
# plot_k_fpp()    
    
# 18
'''calculate average and max false positive probability 
   input: k, n, m, pairwise'''
def avg_max_fpp(k, n, m, pairwise):
    bloom = BloomFilter(n,k, pairwise)
    for i in range(m):
        bloom.rand_inserts()
        
    total_fpp = 0
    max_fpp = 0
    for experiment in range(1000):
        # print "experiment: " + str(experiment)
        numPositive = 0
        
        for lookup in range(10000):
            data = str(rnd.randint(0, 10 ** 8))
            if bloom.lookup(data) == True:
                numPositive += 1
        
        fpp = numPositive / 10000.0
        total_fpp += fpp
        max_fpp = max(max_fpp, fpp)
        
    avg_fpp = total_fpp / 1000.0
    print "Average FPP: " + str(avg_fpp)
    print "Max FPP: " + str(max_fpp)

# avg_max_fpp(6, 4095, 600, False)

# 19
# avg_max_fpp(6, 4095, 600, True)

# 21
'''calculate average and max false positive probability with adversarialInsert
   input: k, n, pairwise'''
def advInsert_avg_max_fpp(k, n, pairwise):
    bloom = BloomFilter(n,k, pairwise)
    bloom.adversarialInserts()
        
    total_fpp = 0
    max_fpp = 0
    for experiment in range(1000):
        # print "experiment: " + str(experiment)
        numPositive = 0
        
        for lookup in range(10000):
            data = str(rnd.randint(0, 10 ** 8))
            if bloom.lookup(data) == True:
                numPositive += 1
        
        fpp = numPositive / 10000.0
        total_fpp += fpp
        max_fpp = max(max_fpp, fpp)
        
    avg_fpp = total_fpp / 1000.0
    print "Average FPP: " + str(avg_fpp)
    print "Max FPP: " + str(max_fpp)

# advInsert_avg_max_fpp(6, 4095, True)

# 22
'''calculate average and max false positive probability with adversarialInsert
   input: k, n, pairwise'''
def advInsert_advLookup_avg_max_fpp(k, n, pairwise):
    bloom = BloomFilter(n,k, pairwise)
    bloom.adversarialInserts()
        
    total_fpp = 0
    max_fpp = 0
    for experiment in range(1000):
        fpp = bloom.adversarialLookups()
        total_fpp += fpp
        max_fpp = max(max_fpp, fpp)
        
    avg_fpp = total_fpp / 1000.0
    print "Average FPP: " + str(avg_fpp)
    print "Max FPP: " + str(max_fpp)
    
# advInsert_advLookup_avg_max_fpp(6, 4095, True)