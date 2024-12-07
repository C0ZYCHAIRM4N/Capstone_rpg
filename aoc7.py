from itertools import product

def convert_file_to_dict(filename):
    result_dict = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            test_value, numbers = line.split(':')
            test_value = int(test_value.strip())
            numbers = list(map(int, numbers.strip().split()))
            result_dict[test_value] = numbers
    return result_dict

def evaluate_expression_left_to_right(numbers, ops):
    result = numbers[0]
    for num, op in zip(numbers[1:], ops):
        if op == '+':
            result += num
        elif op == '*':
            result *= num
        elif op == '||':
            result = int(str(result) + str(num))
    return result

def check_combinations(test_value, numbers):
    operations = ['+', '*', '||']
    for ops in product(operations, repeat=len(numbers)-1):
        if evaluate_expression_left_to_right(numbers, ops) == test_value:
            expression = f"{numbers[0]}"
            for num, op in zip(numbers[1:], ops):
                expression += f" {op} {num}"
            return expression
    return None

filename = 'aoc7.txt'
data_dict = convert_file_to_dict(filename)

total_sum = 0

for test_value, numbers in data_dict.items():
    result = check_combinations(test_value, numbers)
    if result:
        print(f"Found a combination for {test_value}: {result} = {test_value}")
        total_sum += test_value

print(f"Total sum of keys that meet the criteria: {total_sum}")