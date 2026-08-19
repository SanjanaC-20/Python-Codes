#decimal to hexadecimal
def hexadecimal():
    n = int(input("Enter a decimal number: "))
    return hex(n)[2:]

print(hexadecimal())