board = []
for i in range(21):
    row = [0]*15
    board.append(row)

occupied = [(0,8),(0,10),
            (1,7),(1,8),(1,11),(1,12),
            (2,3),(2,5),(2,6),(2,14),
            (3,5),(3,6),(3,11),(3,14),
            (4,2),(4,3),(4,6),(4,8),(4,9),(4,11),
            (5,3),(5,5),(5,6),(5,8),(5,11),(5,13),
            (6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(6,14),
            (7,0),(7,3),(7,5),(7,6),(7,7),(7,8),(7,9),(7,11),(7,14),
            (8,0),(8,3),(8,4),(8,10),(8,13),(8,14),
            (9,2),(9,3),(9,8),
            (10,7),(10,9),
            (11,5),(11,6),(11,7),(11,11),(11,12),(11,13),
            (12,4),(12,6),(12,13),
            (13,3),(13,4),(13,7),(13,9),(13,10),
            (14,0),(14,2),(14,3),(14,4),(14,7),(14,8),(14,10),(14,12),
            (15,3),(15,4),(15,6),(15,7),(15,8),
            (16,0),(16,1),(16,8),(16,9),(16,10),
            (17,2),(17,6),(17,9),(17,10),(17,12),
            (18,1),(18,10),(18,11),(18,12),
            (19,1),(19,2),(19,3),(19,9)]

def printboard():
    #prints the board as you would see it standing from the bottom of the starting gold block
    out = ""
    for i in range(21):
        row = ""
        for j in range(15):
            row += " " + str(board[i][j])
        out = row + '\n' + out
    print(out)

goldstart = (0,2)
goldend = (20,11)
dia1 = (2,9)
dia2 = (8,6)
dia3 = (14,5)

for (a,b) in occupied:
    board[a][b] = 1
printboard()

def validmove(pos):
    a,b = pos
    return a >= 0 and a < 21 and b >= 0 and b < 15 and board[a][b] == 0

def knightmoves(pos):
    a,b = pos
    outmoves = []
    for i in [-2,2]:
        for j in [-1,1]:
            outmoves.append((a + i, b + j))
            outmoves.append((a + j, b + i))
    return outmoves

graph = {}
for i in range(21):
    for j in range(15):
        neighbors = []
        moves = knightmoves((i,j))
        for move in moves:
            if validmove(move):
                neighbors.append(move)
        graph[(i,j)] = neighbors

    
def bfs(start, end):
    distances = {}
    parents = {}
    q = []
    q.append(start)
    distances[start] = 0
    while (len(q) != 0):
        point = q.pop(0)
        if (point == end):
            break
        for neighbor in graph[point]:
            if neighbor not in distances:
                distances[neighbor] = distances[point] + 1
                parents[neighbor] = point
                q.append(neighbor)
    backtrack = []
    curr = end
    while (curr != start):
        backtrack.append(curr)
        curr = parents[curr]
    backtrack.append(start)
    backtrack.reverse()
    print(distances[end])
    return backtrack

print(bfs(dia1, dia2))

print(bfs(goldstart, dia1))
print(bfs(dia2,dia3))
print(bfs(dia3,goldend))


