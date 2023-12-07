import re

def binary_file_to_number_list(binary_file):
    """Lee un archivo binario y lo convierte en una lista de números."""
    with open(binary_file, "r") as file:
        binary_content = file.read()

    group_length = 7
    bit_groups = re.findall('.{1,' + str(group_length) + '}', binary_content)
    binary_list = [list(group) for group in bit_groups]

    if len(bit_groups[-1]) < group_length:
        binary_list[-1] += ['0'] * (group_length - len(bit_groups[-1]))

    number_list = [[int(bit) for bit in group] for group in binary_list]
    return number_list

def save_to_file(file_name, bit_list):
    """Guarda una lista de bits en un archivo."""
    with open(file_name, "w") as file:
        for sublist in bit_list:
            bits_str = "".join(str(bit) for bit in sublist)
            file.write(bits_str)
