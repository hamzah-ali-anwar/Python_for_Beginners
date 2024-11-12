fahrenheit = int(input("What is the temperature in fahrenheit? "))

def temperature(celcius):
    return round(((fahrenheit - celcius) * 5 / 9), 1)

print(f"The celcius equivalent to {fahrenheit} degrees fahreinheit is: " + str(temperature(32)))