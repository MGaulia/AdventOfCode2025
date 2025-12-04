grid = []
for i in open("data/4demo.txt").readlines():
    i = i.rstrip()
    grid.append([j for j in i])


def isrollofpaper(row, col):
    return row in range(0, ROWS) and col in range(0, COLS) and grid[row][col] == "@"


def canaccess(x, y):
    res = 0
    diff = [-1, 0, 1]
    for dx in diff:
        for dy in diff:
            if dx == 0 and dy == 0:
                continue
            res += isrollofpaper(x + dx, y + dy)
            if res > 3:
                return False
    return True


def removepapers(grid, editgrid=True):
    removed = 0
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == "@" and canaccess(i, j):
                removed += 1
                if editgrid:
                    grid[i][j] = "."
    return grid, removed


ROWS = len(grid)
COLS = len(grid[0])

removed = -1
_, part1 = removepapers(grid, False)
part2 = 0
while removed != 0:
    grid, removed = removepapers(grid)
    part2 += removed


print("Part 1:", part1)
print("Part 2:", part2)
