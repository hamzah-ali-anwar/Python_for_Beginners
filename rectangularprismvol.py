length = int(input("What is the length of the rectangular prism? "))
width = int(input("What is the width of the rectangular prism? "))
height = int(input("What is the height of the rectangular prism? "))

def prism_vol(l, v, h):
    return l * v * h

print("The volume of the rectangular prism is" + str(prism_vol(length, width, height)) + "cubic units.")