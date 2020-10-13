def input_file_to_list(file_path):
    with open(file_path, 'r') as input_file:
        output = list(map(int, input_file.read().splitlines()))
    return output


def calculate_fuel(mass, fuel_required=0):
    fuel_calculation = (mass // 3) - 2
    if fuel_calculation <= 0:
        return fuel_required
    else:
        return calculate_fuel(fuel_calculation, fuel_required + fuel_calculation)


if __name__ == '__main__':
    assert calculate_fuel(12) == 2
    assert calculate_fuel(14) == 2
    assert calculate_fuel(1969) == 966
    assert calculate_fuel(100756) == 50346

    mass_by_module = input_file_to_list('day1_input.txt')
    fuel_by_module = list(map(calculate_fuel, mass_by_module))
    total_fuel_requirement = sum(fuel_by_module)

    print(total_fuel_requirement)
