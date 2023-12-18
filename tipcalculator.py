print("Welcome to the tip calculator")
totalbill = float(input("What was the total bill? $"))
percentips = int(input("What percentage tip would you like to give? 10,12, or 15?"))
people = int(input("How many people to split the bill?"))
subtotal = (percentips/100 * totalbill +totalbill)/people
subtotal = round(subtotal,2)
subtotal = "{:.2f}".format(subtotal)
print(f"Each person should pay: ${subtotal}")