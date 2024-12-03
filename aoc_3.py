import re

with open("aoc_3.txt", "r") as file:
    text = file.read()

# Pattern to match "don't()" and "do()"
dont_pattern = r"don't\(\)"
do_pattern = r"do\(\)"
# Pattern to match mul(x,y) where x and y are integers
mul_pattern = r"mul\((\d+),(\d+)\)"

# Initialize the state as enabled
enabled = True

# Initialize the sum of products
sum_of_products = 0

# Find all instructions in the text
instructions = re.finditer(r"don't\(\)|do\(\)|mul\((\d+),(\d+)\)", text)

# Process each instruction
for instruction in instructions:
    if instruction.group() == "don't()":
        enabled = False
    elif instruction.group() == "do()":
        enabled = True
    else:
        if enabled:
            x, y = int(instruction.group(1)), int(instruction.group(2))
            product = x * y
            sum_of_products += product
            print(f"mul({x},{y}) = {product}")

# Print the sum of the products
print(f"Sum of all products: {sum_of_products}")

