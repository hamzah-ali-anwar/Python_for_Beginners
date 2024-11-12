# Create a variable and assign it the string "Just do it!"
my_string = "Just do it!"

# Access the "!" from the variable by index and print() it
print(my_string[10])

# Print the slice "do" from the variable
slice_do = my_string[5:7]
print(slice_do)

# Get and print the slice "it!" from the variable
slice_it = my_string[8:11]
print(slice_it)

# Print the slice "Just" from the variable
slice_just = my_string[0:4]
print(slice_just)

# Get the string slice "do it!" from the variable and concatenate it with the string "Don't ".  Print the resulting string, which should be "Don't do it!" where the "do it!" part is a slice.
concatenation = "Don't" + " " + slice_do + " " + slice_it
print(concatenation)