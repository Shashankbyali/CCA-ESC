print("Enter 1 to convert Decimal to Binary")
print("Enter 2 to convert Decimal to Octal")
print("Enter 3 to convert Decimal to Hexadecimal")
print("Enter 4 to convert Binary to Decimal")
print("Enter 5 to convert Binary to Octal")
print("Enter 6 to convert Binary to Hexadecimal")
print("Enter 7 to convert Octal to Decimal")
print("Enter 8 to convert Octal to Binary")
print("Enter 9 to convert Octal to Hexadecimal")
print("Enter 10 to convert Hexadecimal to Decimal")
print("Enter 11 to convert Hexadecimal to Binary")
print("Enter 12 to convert Hexadecimal to Ocatal")
print("Enter 13 to exit")

while True:
    n=int(input("Enter The Choice:"))  
    def decimal_to_binary(decimal_number):
        if decimal_number == 0:
         return "0"
        binary_number = ""
        while decimal_number > 0:
            binary_number = str(decimal_number % 2) + binary_number
            decimal_number = decimal_number // 2
        return binary_number



    def decimal_to_octal(decimal_number):
        if decimal_number == 0:
            return "0"
        octal_number = ""
        while decimal_number > 0:
            octal_number = str(decimal_number % 8) + octal_number
            decimal_number = decimal_number // 8
        return octal_number


    def decimal_to_hexadecimal(decimal_number):
        if decimal_number == 0:
           return "0"
        hex_digits = "0123456789ABCDEF"
        hexadecimal_number = ""
        while decimal_number > 0:
          remainder = decimal_number % 16
          hexadecimal_number = hex_digits[remainder] + hexadecimal_number
          decimal_number = decimal_number // 16
        return hexadecimal_number

    def binary_to_decimal(binary_number):
        decimal_number = 0
        binary_number = str(binary_number) 
        for i, digit in enumerate(reversed(binary_number)):
            decimal_number += int(digit) * (2 ** i)
        return decimal_number


    def binary_to_octal(binary_number):
        decimal_number = 0
        binary_number = str(binary_number) 
        for i, digit in enumerate(reversed(binary_number)):
            decimal_number += int(digit) * (2 ** i)
        octal_number = ""
        while decimal_number > 0:
            octal_number = str(decimal_number % 8) + octal_number
            decimal_number = decimal_number // 8
        return octal_number or "0"

    def octal_to_decimal(octal_number):
        decimal_number = 0
        octal_number = str(octal_number)  
        for i, digit in enumerate(reversed(octal_number)):
            decimal_number += int(digit) * (8 ** i)
        return decimal_number


    def hexadecimal_to_decimal(hexadecimal_number):
        hex_digits = "0123456789ABCDEF"
        decimal_number = 0
        hexadecimal_number = hexadecimal_number.upper()  
        for i, digit in enumerate(reversed(hexadecimal_number)):
            decimal_number += hex_digits.index(digit) * (16 ** i)
        return decimal_number



    if(n==1):
        decimal_number = int(input("Enter a decimal number: "))
        binary_result = decimal_to_binary(decimal_number)
        print(f"The binary representation of {decimal_number} is {binary_result}")

    if(n==2):   
        decimal_number = int(input("Enter a decimal number: "))
        octal_result = decimal_to_octal(decimal_number)
        print(f"The octal representation of {decimal_number} is {octal_result}")
    if(n==3):
        decimal_number = int(input("Enter a decimal number: "))
        hexadecimal_result = decimal_to_hexadecimal(decimal_number)
        print(f"The hexadecimal representation of {decimal_number} is {hexadecimal_result}")
    if(n==4):
        binary_number = input("Enter a binary number: ")
        decimal_result = binary_to_decimal(binary_number)
        print(f"The decimal representation of {binary_number} is {decimal_result}")
    if(n==5):
        binary_number = input("Enter a binary number: ")
        octal_result = binary_to_octal(binary_number)
        print(f"The octal representation of {binary_number} is {octal_result}")
    if(n==6):
        binary_number = input("Enter a binary number: ")
        decimal_number = int(binary_number, 2) 
        hexadecimal_result = hex(decimal_number)[2:].upper()  
        print(f"The hexadecimal representation of {binary_number} is {hexadecimal_result}")
    if(n==7):
        octal_number = input("Enter an octal number: ")
        decimal_result = octal_to_decimal(octal_number)
        print(f"The decimal representation of {octal_number} is {decimal_result}")
    if(n==8):
        octal_number = input("Enter an octal number: ")
        decimal_number = int(octal_number, 8)  
        binary_result = bin(decimal_number)[2:]  
        print(f"The binary representation of {octal_number} is {binary_result}")
    if(n==9):
        octal_number = input("Enter an octal number: ")
        decimal_number = int(octal_number, 8)  
        hexadecimal_result = hex(decimal_number)[2:].upper()  
        print(f"The hexadecimal representation of {octal_number} is {hexadecimal_result}")
    if(n==10):
        hexadecimal_number = input("Enter a hexadecimal number: ")
        decimal_result = hexadecimal_to_decimal(hexadecimal_number)
        print(f"The decimal representation of {hexadecimal_number} is {decimal_result}")
    if(n==11):
        hexadecimal_number = input("Enter a hexadecimal number: ")
        decimal_number = int(hexadecimal_number, 16)  
        binary_result = bin(decimal_number)[2:]  
        print(f"The binary representation of {hexadecimal_number} is {binary_result}")
    if(n==12):
        hexadecimal_number = input("Enter a hexadecimal number: ")
        decimal_number = int(hexadecimal_number, 16)  
        octal_result = oct(decimal_number)[2:]  
        print(f"The octal representation of {hexadecimal_number} is {octal_result}")
    if(n>13 or n<=0):
        print("Invalid Number Enter Number Between 1 to 13")
    if(n==13):
        break;


