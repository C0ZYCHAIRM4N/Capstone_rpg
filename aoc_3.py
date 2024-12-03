import re

# Open and read the file
with open('aoc_3.txt', 'r') as file:
    text = file.read()

# Regex pattern to match mul(x,y) where x and y are integers
pattern = r'mul\((\d+),(\d+)\)'

# Find all matches
matches = re.findall(pattern, text)

# Initialize the sum of products
sum_of_products = 0

# Print the matches and their products, and calculate the sum of products
for match in matches:
    x, y = int(match[0]), int(match[1])
    product = x * y
    sum_of_products += product
    print(f"mul({x},{y}) = {product}")

# Print the sum of the products
print(f"Sum of products: {sum_of_products}")

