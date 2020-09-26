denary = int(input("Enter a denary number: "))
binary = ""

while denary > 0:
    binary = str(denary%2) + binary
    denary = denary // 2

print("Your binary number is: ", binary)
