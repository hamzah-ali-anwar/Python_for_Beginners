def factorial(num):

    returned = 1
    for i in range(num, 1, -1):
        returned *= i

    return returned
    
print(factorial(3))
print(factorial(4))
print(factorial(5))

    