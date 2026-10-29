import copy
with open('2015/Day18/test') as f:
    lines = f.read().splitlines()
    grid=[]
    for line in lines:
        grid.append(list(line))

def all_nbrs(x, y):
    nbrs = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx != 0 or dy != 0:  # Exclude the cell itself
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    nbrs.append(grid[nx][ny])
    return nbrs
def next_state():
    global grid
    new_grid = copy.deepcopy(grid)
    for i in  range(100):
        for j in range(100):
            on_count = all_nbrs(i, j).count('#')
            if grid[i][j] == '#':
                if on_count not in [2, 3]:
                    new_grid[i][j] = '.'
            else:
                if on_count == 3:
                    new_grid[i][j] = '#'
    grid = new_grid

for a in range(100):
    next_state()
s=0
for i in range(100):
    for j in range(100):
        if grid[i][j]=='#':
            s+=1
print(s)


