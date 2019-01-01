"""Below are a few practice examples using randint and 
random.choice."""

import numpy as np

# When simulating coin flips, we will use 0 to represent
# heads and 1 to represent tails.
# First let's generate a random set of ten tosses.

num_tosses = (int(1e1), 2)
max = 2

rand_set = np.random.randint(max, size=num_tosses)

print(rand_set, '\n')

print('____________________', '\n')

# Next we will simulate 1 million tests of three bias coin flips
# hint: use np.random.choice()
tests = np.random.choice([0, 1], size=(int(1e6), 3), p=(.6, .4))

# sums of all tests
test_sums = tests.sum(axis=1)

# proportion of tests that produced exactly one head
prob_occ = (test_sums == 2).mean()
print(prob_occ, '\n')

print('____________________', '\n')

# simulate the first million die rolls
g = np.arange(1, 7)
size = int(1e6)
first = np.random.choice(g, size=size)

# simulate the second million die rolls
second = np.random.choice(g, size=size)

# proportion of tests where the 1st and 2nd die rolled the same number
prob_equal = (first == second).sum() / size
print(prob_equal, '\n')
