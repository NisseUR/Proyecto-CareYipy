

def binary_file_to_number_list(binary_file):
    """Lee un archivo binario y lo convierte en una lista de números."""
    with open(binary_file, "r") as file:
        binary_content = file.read().replace('\n', '')  

    group_length = 7
    number_list = []
    current_group = []

    for bit in binary_content:
        current_group.append(int(bit))
        if len(current_group) == group_length:
            number_list.append(current_group)
            current_group = []

    if current_group:
        current_group += [0] * (group_length - len(current_group))  # rellena con 0's
        number_list.append(current_group)

    return number_list

def save_to_file(file_name, bit_list):
    """Guarda una lista de bits en un archivo."""
    with open(file_name, "w") as file:
        for sublist in bit_list:
            bits_str = "".join(str(bit) for bit in sublist)
            file.write(bits_str)