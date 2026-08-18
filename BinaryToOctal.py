#Binary to Octal Conversion
def binary_to_octal(n):
    # Convert binary to decimal
    decimal = int(n, 2)
    
    # Convert decimal to octal
    octal = oct(decimal)
    
    return octal[2:]  # Remove the '0o' prefix