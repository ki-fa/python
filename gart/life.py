import copy, time, random
width = 100
height = 30
currentCells = [[0]*height for i in range(width)]
for x in range(width):
    for y in range(height):
        if random.randint(0, 1) == 0:
            currentCells[x][y] = '#'
        else:
            currentCells[x][y] = ' '
while True:
    print('\n\n\n\n\n')
    nextCells = copy.deepcopy(currentCells)

    for x in range(width):
        for y in range(height):
            print(nextCells[x][y], end='')

    for x in range(width):
        for y in range(height):
            left = (x - 1) % width
            right = (x + 1)% width
            up = (y + 1)% height 
            down = (y - 1)% height 
            numNeighbors = 0
            
            if nextCells[left][up] == '#':
                numNeighbors += 1
            if nextCells[x][up] == '#':
                numNeighbors += 1
            if nextCells[right][up] == '#':
                numNeighbors += 1
            if nextCells[left][y] == '#':
                numNeighbors += 1
            if nextCells[right][y] == '#':
                numNeighbors += 1
            if nextCells[left][down] == '#':
                numNeighbors += 1
            if nextCells[x][down] == '#':
                numNeighbors += 1
            if nextCells[right][down] == '#':
                numNeighbors += 1

            if nextCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                currentCells[x][y] = '#';
            elif nextCells[x][y] == ' ' and numNeighbors == 3:
                currentCells[x][y] = '#'
            else:
                currentCells[x][y] = ' '
    time.sleep(1)
