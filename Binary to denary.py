binary = input("Enter a binary number: ")
denary = 0

for digit in binary:
    denary = denary * 2 + int(digit)

print("Your denary number is: ", str(denary))
