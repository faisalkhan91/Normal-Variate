# Normal-Variate
This program performs a statistical analysis of a set of random numbers sampled from a Gaussian distribution.

normalstats is the implementation of lists and loops in python.

normalstats2 is improved version rewritten to be more python like and efficient. For example, I rewrote the form of some of the for loops to simply iterate through the list values, rather than the index values, since the indices weren't actually being used. The biggest efficiency was replacing the call to the list count() function in the mode calculation by a simple search with a loop that would just find how long the consecutive set of same values was at any point in the list.
