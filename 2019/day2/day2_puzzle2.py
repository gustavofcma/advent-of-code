TARGET = 19690720


def input_file_to_list(file_path):
    with open(file_path, 'r') as input_file:
        output = list(map(int, input_file.read().split(',')))
    return output


def run_intcode_program(intcode_input):
    index = 0
    while intcode_input[index] in [1, 2]:
        opcode, first_value, second_value, position = intcode_input[index:index+4]
        if opcode == 1:
            intcode_input[position] = intcode_input[first_value] + intcode_input[second_value]
        else:
            intcode_input[position] = intcode_input[first_value] * intcode_input[second_value]

        index += 4

    return intcode_input[0]


def find_target_value(intcode_input, target_value, min_input=0, max_input=99):
    noun = verb = min_input
    match_found = False
    while noun <= max_input and not match_found:
        verb = min_input
        while verb <= max_input and not match_found:
            aux_input = intcode_input[:]
            aux_input[1:3] = noun, verb
            check_result = run_intcode_program(aux_input)
            match_found = check_result == target_value
            verb += 1
        noun += 1

    return match_found, noun-1, verb-1


if __name__ == '__main__':
    assert run_intcode_program([1,9,10,3,2,3,11,0,99,30,40,50]) == 3500
    assert run_intcode_program([1,0,0,0,99]) == 2
    assert run_intcode_program([2,3,0,3,99]) == 2
    assert run_intcode_program([2,4,4,5,99,0]) == 2
    assert run_intcode_program([1,1,1,4,99,5,6,0,99]) == 30

    intcode = input_file_to_list('day2_input.txt')

    result = find_target_value(intcode, TARGET)
    if result:
        noun, verb = result[1:3]
    else:
        noun = verb = 0

    print(f'Result: {100 * noun + verb}')
