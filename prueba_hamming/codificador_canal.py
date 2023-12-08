def binary_file_to_number_list(binary_file):
    """Lee un archivo binario y lo convierte en una lista de números."""
    with open(binary_file, "r") as file:
        binary_content = file.read()

    group_length = 7
    number_list = []

    for i in range(0, len(binary_content), group_length):
        group = binary_content[i:i+group_length].ljust(group_length, '0')
        number_list.append([int(bit) for bit in group])

    return number_list

def save_to_file(file_name, bit_list):
    """Guarda una lista de bits en un archivo."""
    with open(file_name, "w") as file:
        file.writelines(''.join(map(str, sublist)) for sublist in bit_list)