from math import prod
from itertools import combinations

def input_file_to_list(file_path):
    with open(file_path, 'r') as input_file:
        output = list(map(int, input_file.read().splitlines()))
    return output


if __name__ == '__main__':
    items = input_file_to_list('day1_input.txt')

    double_values = [t for t in combinations(items, 2) if sum(t) == 2020][0]
    triple_values = [t for t in combinations(items, 3) if sum(t) == 2020][0]

    print('Puzzle 1:')
    print(f'Values: {double_values[0]} and {double_values[1]}\nResult: {prod(double_values)}\n')

    print('Puzzle 2:')
    print(f'Values: {triple_values[0]}, {triple_values[1]} and {triple_values[2]}\nResult: {prod(triple_values)}\n')
