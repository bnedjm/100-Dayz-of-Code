import random

a = 0 
b = 5
#random.randint(a,b) generates random int values between a and b inclusive
c = random.randint(a,b)
print(c)

#random.random() generates floating point numbers between 0 and 1 not inclusive
d = random.random()
print(d)

#in order to expend the range of random numbers, we multiply the randomized value with the max value in our range
f = d * 5
print(f)

#sample solution
score = random.randint(1, 100)
print(score)

#lists
sample_1 = [0,1,2,2,3]
sample_2 = ["hey", "Yow", "No"]

#you can access the list's elements using negative indication as well
print(sample_1[-1])

#append > adds an item to the end of the list 
sample_2.append("Hellanoo!")
print(sample_2[-1])

#extend > adds a list of items to an exsisting list
sample_1.extend([3, 5])
print(type(sample_1[-1]))
print(sample_1[-1])
