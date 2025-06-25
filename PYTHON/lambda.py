# lambda function

sq=lambda x:x**2
print(sq(4))

# map
from functools import reduce
nums=[1,2,3,4]

squares=list(map(lambda x: x**2, nums))
evens=list(filter(lambda y:y%2==0,nums))
product=reduce(lambda x,  y:x*y, nums)

print(squares,"\t",evens,"\t",product)

#list compherension

square=[x**2 for x in range(6)]
print(squares)

#pure function
def add(a,b):
    return a+b
print(add(1,2))

#recursion
def factorial(n):
    if (n==0):
        return 1
    else:
        return (n * (factorial(n-1)))
print(factorial(5))