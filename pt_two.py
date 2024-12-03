import re

with open("aoc_3.txt", "r") as file:
    text = file.read()

# Pattern to match "don't()" followed by any text and then "do()"
dont_do_pattern = r"don't\(\).*?do\(\)"
# Pattern to match mul(x,y) where x and y are integers
mul_pattern = r"mul\((\d+),(\d+)\)"

# Find all matches of the "don't()" followed by any text and then "do()" pattern
dont_do_matches = re.finditer(dont_do_pattern, text, re.DOTALL)
dont_do_ranges = [(match.start(), match.end()) for match in dont_do_matches]

# Initialize the sum of products
sum_of_products = 0

# Find all mul(x,y) expressions
all_mul_matches = re.finditer(mul_pattern, text)

# Check each mul(x,y) expression to see if it falls within any "don't()" to "do()" range
for mul_match in all_mul_matches:
    mul_start = mul_match.start()
    mul_end = mul_match.end()
    in_dont_do_block = any(start <= mul_start < end for start, end in dont_do_ranges)
    
    if not in_dont_do_block:
        x, y = int(mul_match.group(1)), int(mul_match.group(2))
        product = x * y
        sum_of_products += product
        print(f"mul({x},{y}) = {product}")

# Print the sum of the products
print(f"Sum of all products: {sum_of_products}")