def read_grid(file_path):
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

def search_word(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    occurrences = []

    def search_direction(x, y, dx, dy):
        for i in range(word_len):
            if not (0 <= x < rows and 0 <= y < cols) or grid[x][y] != word[i]:
                return False
            x += dx
            y += dy
        return True

    directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if search_direction(x, y, dx, dy):
                    occurrences.append((x, y, dx, dy))
    return occurrences

def find_words(grid, words):
    found_words = {}
    for word in words:
        positions = search_word(grid, word)
        if positions:
            found_words[word] = positions
    return found_words


file_path = 'aoc_4.txt'
grid = read_grid(file_path)
words = ['XMAS'] 
found_words = find_words(grid, words)

for word, positions in found_words.items():
    print(f"Word '{word}' found {len(positions)} times at positions: {positions}")

