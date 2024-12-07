with open("aoc6example.txt", "r") as file:
    lines = file.readlines()

# Convert lines to a list of lists
grid = [list(line.strip()) for line in lines]

def find_starting_point(grid):
    for row_index, row in enumerate(grid):
        for col_index, char in enumerate(row):
            if char == '^':
                return (row_index, col_index)
    return None

def turn_right(direction):
    directions = ['up', 'right', 'down', 'left']
    return directions[(directions.index(direction) + 1) % 4]

def move_character(grid, start, direction):
    y, x = start
    move_count = 0
    visited_positions = set()
    visited_positions.add((y, x))
    
    while True:
        if direction == 'up':
            new_y, new_x = y - 1, x
        elif direction == 'down':
            new_y, new_x = y + 1, x
        elif direction == 'left':
            new_y, new_x = y, x - 1
        elif direction == 'right':
            new_y, new_x = y, x + 1

        # Check if the character is out of bounds
        if new_y < 0 or new_y >= len(grid) or new_x < 0 or new_x >= len(grid[0]):
            print(f"Character '^' has left the grid at ({new_y}, {new_x}) after {move_count} moves")
            print(f"Number of distinct positions visited: {len(visited_positions)}")
            break

        # Check if the next position is a blocker
        if grid[new_y][new_x] == '#':
            print(f"Character '^' encountered a blocker at ({new_y}, {new_x}) and is turning right")
            direction = turn_right(direction)
        else:
            y, x = new_y, new_x
            move_count += 1
            visited_positions.add((y, x))
            print(f"Character '^' moved to ({y}, {x})")

# Example usage
start = find_starting_point(grid)
if start:
    move_character(grid, start, 'up')  # Change initial direction as needed
else:
    print("Starting point '^' not found in the grid")








