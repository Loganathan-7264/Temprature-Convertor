#This is temprature convertor program

unit = input ("Is this temprature is celcius or Fahrenheit (C/F): ")
temp = float(input("Enter the temprature: "))

if unit == "C":
    temp = round(((temp * 9)/5) + 32, 1)
    print(f"The temprature is {temp} F") 
elif unit == "F":
    temp = round(((temp-32) * 5)/9, 1)
    print(f"The temprature is {temp} C")
else:
    print(f"{unit} is invalid measurement")