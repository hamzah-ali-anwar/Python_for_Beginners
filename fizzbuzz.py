for letter in range(1, 51):

    if letter % 3 == 0 and letter % 5 == 0:
        print("FizzBuzz")
    elif letter % 3 == 0:
        print("Fizz")
    elif letter % 5 == 0:
        print("Buzz")
    
    else:
        print(letter)