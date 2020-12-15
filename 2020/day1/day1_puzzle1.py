def input_file_to_list(file_path):
    with open(file_path, 'r') as input_file:
        output = list(map(int, input_file.read().splitlines()))
    return output