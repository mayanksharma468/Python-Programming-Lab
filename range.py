# Python code to demonstrate the working of
# randrange()

import random

# Using randrange() to generate numbers from 0-100
print ("Random number from 0-100 is : ",end="")
print (random.randrange(100))

# Using randrange() to generate numbers from 50-100
print ("Random number from 50-100 is : ",end="")
print (random.randrange(50,100))

# Using randrange() to generate numbers from 50-100
# skipping 5
print ("Random number from 50-100 skip 5 is : ",end="")
print (random.randrange(50,100,5))
