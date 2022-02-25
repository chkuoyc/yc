from numpy import random
import numpy as np

y = input("Enter your number: ")
x = random.randint(y)
print(x)
x = random.rand()
print(x)
x = random.choice([2,4,6,8], p=[0.16,0.3,0.34,0.2], size=(10))
print(x)

print('....................')

arr = np.array([1,2,3,4,5,6])
random.shuffle(arr)
print(arr)