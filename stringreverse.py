my_string = str(input("Please enter a string:"))
reversed = ""

for item in range(len(my_string) - 1, -1, -1):
    reversed += my_string[item]

    print(reversed)