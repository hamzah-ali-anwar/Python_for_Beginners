number = int(input("Please enter a positive integer: "))
number_init = number

sum = 0
while number > 0:
    sum += number 
    number -= 1

print((f"User entered: {number_init}"))
print(f"The sum of the positive integers is: {sum}")

