# function without a parameter
def hello_world_printer():
    print("Hello World!")

hello_world_printer()

# function with a parameter
def name_printer(user_name):
    print(user_name)
    
name = input("What's your name? ")
name_printer(name)