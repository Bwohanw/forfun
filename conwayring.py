'''
silly little attempt at implementation of part 3 (life_ring()) from https://courses.grainger.illinois.edu/cs340/sp2024/mp/mp9.html
'''


def life_ring(width, height, ticks, border):
    counts = {}
    alive = set()
    notouchy = set()
    importantcoords = []
    currcoords = (-1,-1)
    neighbordeltas = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

    endidx = width+1
    topsection = border[0:endidx]
    rightsection = border[endidx:endidx+height+1]
    endidx += height + 1
    botsection = border[endidx:endidx + width + 1]
    endidx += width + 1
    leftsection = border[endidx:]


    def initprocess(coor):
        importantcoords.append(currcoords)
        if i == '#':
            alive.add(currcoords)
            for x,y in neighbordeltas:
                neighbor = (currcoords[0] + x, currcoords[1] + y)
                if (neighbor not in counts.keys()):
                    counts[neighbor] = 1
                else:
                    counts[neighbor] += 1
        if (i == '"'):
            notouchy.add(currcoords)

    for i in topsection:
        initprocess(currcoords)
        currcoords = (currcoords[0] + 1, currcoords[1])
    for i in rightsection:
        initprocess(currcoords)
        currcoords = (currcoords[0], currcoords[1] + 1)
    for i in botsection:
        initprocess(currcoords)
        currcoords = (currcoords[0] - 1, currcoords[1])
    for i in leftsection:
        initprocess(currcoords)
        currcoords = (currcoords[0],currcoords[1] - 1)

    def addneighbors(countsdict, coord):#counts neighbors of a coord (assumes the input coord is alive)
        for x,y in neighbordeltas:
            neighbor = (coord[0] + x, coord[1] + y)
            if neighbor in countsdict.keys():
                countsdict[neighbor] += 1
            else:
                countsdict[neighbor] = 1
    
    def tick():
        newcounts = {}
        newalive = set()
        for x,y in counts.keys():
            if (x,y) in notouchy:
                continue
            if (x,y) in alive:
                if (counts[(x,y)] == 3 or counts[(x,y)] == 2):
                    newalive.add((x,y))
                    addneighbors(newcounts, (x,y))
                continue
            if (counts[(x,y)] == 3):
                newalive.add((x,y))
                addneighbors(newcounts, (x,y))
        alive = newalive
        counts = newcounts
    
    for i in range(ticks):
        tick()

    toret = ""
    for x,y in importantcoords:
        coord = (x,y)
        if coord in alive:
            toret += '#'
        elif coord in notouchy:
            toret += '"'
        else:
            toret += ' '

    return toret                




