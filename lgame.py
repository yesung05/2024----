def neighbor(grid, x, y):
    dir = [(-1, -1), (-1, 0), (-1, 1), 
                  (0, -1),         (0, 1), 
                  (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            count += grid[nx][ny]
    return count

def ng(grid): #Next Generation
    rows, cols = len(grid), len(grid[0])
    NGrid = [[0] * cols for _ in range(rows)]

    for x in range(rows):
        for y in range(cols):
            neighbors = neighbor(grid, x, y)
            if grid[x][y] == 1: 
                if neighbors in [1, 2, 3, 4, 7]:  
                    NGrid[x][y] = 1
                else: 
                    NGrid[x][y] = 0
            else: 
                if neighbors in [3, 7]:  
                    NGrid[x][y] = 1
                else:  
                    NGrid[x][y] = 0
    return NGrid

def CntLive(grid):
    return sum(sum(row) for row in grid)

DefaultGrid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


n = int(input())
Grid = DefaultGrid

for generation in range(n):
    Grid = ng(Grid)

print(CntLive(Grid))# 출력
