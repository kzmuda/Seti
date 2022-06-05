# def decimal_to_binary(decimal_number):
#     binary_numbers_list = []
#     while decimal_number > 0:
#         binary_number = decimal_number % 2
#         binary_numbers_list.append(binary_number)
#         #decimal_number = (decimal_number - binary_number) / 2
#         decimal_number = decimal_number // 2
#     #binary_numbers_list = list(reversed(binary_numbers_list))
#     return binary_numbers_list[::-1]

def decimal_to_binary(decimal_number):
    decimal_to_base(decimal_number,2)

# def binary_to_decimal(binary_digits):
#     decimal = 0
#     power = 0
#     for x in binary_digits[::-1]:
#         binary = x * (2**power)
#         decimal += binary
#         power += 1

#     #     for x in range(1, (len(binary_digits)+1)):
#     #
#     #         binary = binary_digits[-x] * (2 ** power)
#     #         decimal += binary
#     #         power += 1
#     return decimal
#     #         # 01010
#     #         #  0 8 0 2 0 = 10


def decimal_to_base(decimal_number, destination_base):
    """Returns the digits in destination_base representation of the decimal number"""
    binary_numbers_list = []
    while decimal_number > 0:
        binary_number = decimal_number % destination_base
        binary_numbers_list.append(binary_number)
        
        decimal_number = decimal_number // destination_base
    #binary_numbers_list = list(reversed(binary_numbers_list))
    return binary_numbers_list[::-1]

    
def binary_to_decimal(binary_digits):
    base_to_decimal(binary_digits,2)


def base_to_decimal(digits, original_base):
    """Returns the decimal (number) representation of an array of digits given in original_base"""
    decimal = 0
    power = 0
    for x in digits[::-1]:
        binary = x * (original_base**power)
        decimal += binary
        power += 1

    return decimal


def digits_as_string(digits, base):
    """Returns the string representation of an array of digits given in base"""
    pass


def convert_base(original_digits, original_base, destination_base):
    """Conversion from any base to any other base"""
    pass 
# print(binary_to_decimal([1,0,1,0]))
# lista =bin(int(10))[2::]
# print(lista)
# list = [5, 4, 3, 2, 1]
# print(list[::-1])
print(decimal_to_base(20,2))