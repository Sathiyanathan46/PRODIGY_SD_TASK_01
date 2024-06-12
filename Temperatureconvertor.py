temp = float(input("Enter the temperature: "))
print("Select a unit of your choice from the list given below:")
print("1. Celsius")
print("2. Fahrenheit")
print("3. Kelvin")

unit = int(input("Enter your choice: "))

if unit == 1:
    celsius = temp
    fahrenheit = (temp * 9/5) + 32
    kelvin = temp + 273.15
    print("Temperature in Celsius is:", celsius)
    print("Temperature in Fahrenheit is:", fahrenheit)
    print("Temperature in Kelvin is:", kelvin)
elif unit == 2:
    fahrenheit = temp
    celsius = (temp - 32) * 5/9
    kelvin = celsius + 273.15
    print("Temperature in Fahrenheit is:", temp)
    print("Temperature in Celsius is:", celsius)
    print("Temperature in Kelvin is:", kelvin)
elif unit == 3:
    kelvin = temp
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Kelvin is:", temp)
    print("Temperature in Celsius is:", celsius)
    print("Temperature in Fahrenheit is:", fahrenheit)
else:
    print("You've entered the wrong choice.")
