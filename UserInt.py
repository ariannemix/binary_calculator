from Converter import BinaryConverter
from Calculator import Calculator


class User:

    def __init__(self):
        self.open = True

    def binary(self):
        binary = input("Enter a binary number to convert: ")
        converter = BinaryConverter(binary=binary)
        try:
            print(f"\n{binary} = {converter.bin_to_dec()}\n")
        except:
            print("\nPlease enter a valid input.")

    def decimal(self):
        integer = int(input("Enter a decimal number to convert: "))
        converter = BinaryConverter(integer=integer)
        try:
            print(f"\n{integer} = {converter.dec_to_bin()}\n")
        except:
            print("\nPlease enter a valid input.")

    def add(self):
        binary1 = input("Enter the first binary number: ")
        binary2 = input("Enter the second binary number: ")
        calc = Calculator(binary1, binary2)
        bin_sum = calc.add_operands()
        print(f"{binary1} + {binary2} = {bin_sum}\n")

    def subtract(self):
        binary1 = input("Enter the first binary number: ")
        binary2 = input("Enter the second binary number: ")
        calc = Calculator(binary1, binary2)
        bin_dif = calc.subtract_operands()
        if bin_dif == 'negative':
            print(
                f"Error: Negative result\n")
        else:
            print(f"{binary1} - {binary2} = {bin_dif}\n")

    def multiply(self):
        binary1 = input("Enter the first binary number: ")
        binary2 = input("Enter the second binary number: ")
        calc = Calculator(binary1, binary2)
        bin_prod = calc.multiply_operands()
        print(f"{binary1} * {binary2} = {bin_prod}\n")

    def divide(self):
        binary1 = input("Enter the first binary number: ")
        binary2 = input("Enter the second binary number: ")
        calc = Calculator(binary1, binary2)
        bin_quot = calc.divide_operands()
        print(f"{binary1} / {binary2} = {bin_quot}\n")

    def quit(self):
        print(f"\nGoodbye!")
        self.open = False
