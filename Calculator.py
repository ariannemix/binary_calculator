from Converter import BinaryConverter


class Calculator():

    def __init__(self, operand1, operand2):
        self.operand1 = BinaryConverter(binary=operand1).bin_to_dec()
        self.operand2 = BinaryConverter(binary=operand2).bin_to_dec()

    def add_operands(self):
        added = self.operand1 + self.operand2
        binary_added = BinaryConverter(integer=added).dec_to_bin()
        return binary_added

    def subtract_operands(self):
        difference = self.operand1 - self.operand2
        if difference >= 0:
            binary_difference = BinaryConverter(
                integer=difference).dec_to_bin()
        else:
            binary_difference = 'negative'
        return binary_difference

    def multiply_operands(self):
        product = self.operand1 * self.operand2
        binary_product = BinaryConverter(integer=product).dec_to_bin()
        return binary_product

    def divide_operands(self):
        quotient = int(self.operand1 / self.operand2)
        print(quotient)
        binary_quotient = BinaryConverter(integer=quotient).dec_to_bin()
        return binary_quotient
