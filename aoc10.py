def parse_grid(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    grid = [list(map(int, line.strip())) for line in lines]
    return grid

def is_valid_position(x, y, width, height):
    return 0 <= x < width and 0 <= y < height

def find_trailhead(grid, x, y):
    width, height = len(grid[0]), len(grid)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    stack = [(x, y, 0)]  # (current x, current y, current number in sequence)
    visited = set()

    while stack:
        cx, cy, num = stack.pop()
        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))

        if grid[cy][cx] == num:
            if num == 9:
                return True
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if is_valid_position(nx, ny, width, height):
                    stack.append((nx, ny, num + 1))
    return False

def find_all_trailheads(grid):
    trailheads = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0 and find_trailhead(grid, x, y):
                trailheads.append((x, y))
    return trailheads

filename = 'aocexample10.txt'
grid = parse_grid(filename)
trailheads = find_all_trailheads(grid)
print(f"Trailheads found at: {trailheads}")
