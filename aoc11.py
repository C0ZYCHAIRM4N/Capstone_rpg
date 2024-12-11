import cProfile

def apply_rules(numbers):
    result = []
    for number in numbers:
        if number == 0:
            result.append(1)
        else:
            str_num = str(number)
            num_len = len(str_num)
            if num_len % 2 == 0:
                mid = num_len // 2
                left_half = int(str_num[:mid])
                right_half = int(str_num[mid:])
                if left_half != 0:
                    result.append(left_half)
                result.append(right_half)
            else:
                result.append(number * 2024)
    return result

def main():
    # Read numbers from the file
    with open('aoc11tc.txt', 'r') as file:
        line = file.readline().strip()
        numbers = list(map(int, line.split()))

    # Apply the rules iteratively 75 times
    modified_numbers = numbers
    for _ in range(75):
        modified_numbers = apply_rules(modified_numbers)

    # Print the count of numbers in the 75th list of modified numbers
    print(len(modified_numbers))

if __name__ == "__main__":
    cProfile.run('main()')
