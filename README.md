# Bloom-Filter
A Bloom Filter is one of many different probabilistic data Structures.

# Description
Bloom Filters take advantage of hashing to keep records of data with a very low false positive rate. By combining hashing and a bit-array, Bloom Filters can store a lot of data in a very small space. However, as with most randomness, Bloom Filters have an inherent tradeoff, high space efficiency vs a small false positive probability.  
A Bloom Filter consists of:  
__1.__ an n bit array, A, initialized to 0's.  
__2.__ k-independent, random hash functions. We assume the hash functions, h1,...,hk, map uniformly and randomly to the range 0,...,n-1. A hash function h maps strings of length p to shorter strings of length q. That is h: {0, 1}^p -> {0, 1}^q. In the case of a Bloom Filter, p is the length of the input and q is simply log(n).  
Bloom Filters have two basic operations:  
__Insertion:__ for an element sj the bits A[hi(sj )] are set to 1. If A[hi(sj )] = 1, don't change it.  
__Lookup:__ to check if si is in the Bloom Filter, check if every bit that it hashes to is set to 1. If not, you have not inserted it to the filter. If all the bits are one, then we are in one of two cases:  
1. True positive: si is in the Bloom Filter  
2. False positive: si is not in the Bloom Filter. But because of previous insertions we performed, these bits have happened to be set to 1.  
We have run in to the fundamental trade-off of Bloom Filters--we have no idea whether we have a false positive or a true positive when we run a lookup. For this reason, our goal will be to design the Bloom Filter in a way that minimizes the false positive probability, so that most of the time our lookups will return true positives.
