'''
replication of the game https://en.gamesaien.com/game/fruit_box/

This generates a board that is clearable using some sequence of boxes.
The idea is to generate boxes in the reverse order that they should be drawn.

The first box will encompass the entire board, since the last move has to clear out everything
If a new box overlaps with a previous box, the tiles in their overlap must be cleared by the new box.
To achieve this, we will number the boxes in increasing order.
Each tile will be given a number, representing the highest box number that contains that tile. This tile must be cleared by that box.
The tiles that have a box number will be called the necessarily filled tiles for that box.

This box generation must continue until each box number has less than 10 tiles with that number. Realistically, this number should probably
be smaller than 10, or there should be some upper bound for how many boxes there can be with an "obscene" number of necessarily filled tiles.

In addition, there should not be any boxes that only have 1 necessarily filled tiles. While it's easy to avoid new boxes having size 1,
we need to ensure the new numbering doesn't leave behind exactly 1 of any number.

In theory, we can make box generation pretty liberal, but this may make reaching the stopping condition difficult.
While there are certainly workarounds, such as skewing the box dimensions towards smaller boxes,
or gradually skewing as more boxes are generated,
I will be lazy and impose a maximum box size. With a small enough box size,
the only "obscenely" large box would be the initial one encompassing the whole board.
Evidently, this is not ideal, since obscene boxes are fine, as long as the number of necessarily filled tiles is not.

For the exact box generation algorithm, I'm not sure what approach would be best.
My current thoughts:
Give each box a priority 0
Generate a box by picking a top left + bottom right corner, subject to the prior restraints
Update the priority for the contained tiles (and any metadata). Maybe there's something you can do with rectangle bounding to make this faster
continue until each box priority has 1 < x < 10 necessarily filled tiles.
For each priority, we can easily partition 10 into the necessarily filled tiles.
Then, iterate through the board, populating the tiles with the next fill value for that priority.
'''

import random

MAX_AREA = 20
BOARD_WIDTH = 5
BOARD_HEIGHT = 5
BOX_TOTAL = 10


board = []
priority = []
for i in range(BOARD_HEIGHT):
    board.append([0] * BOARD_WIDTH)
    priority.append([0] * BOARD_WIDTH)

def print_board(grid):
    for i in range(BOARD_HEIGHT):
        print(grid[i])
# how many tiles each priority has
tile_counts = {0 : BOARD_WIDTH * BOARD_HEIGHT}
#in reverse order
box_order = [((0,0), (BOARD_HEIGHT, BOARD_WIDTH))]

def generate_rectangle(box_count):
    '''
    each rectangle will be a pair of coordinates ((h_upper, w_left), (height, width))
    This rectangle will be inclusive of the top left corner, but exclusive of the bottom right corner.
    So the actual rectangle will span from h_upper -> h_upper + height - 1, w_left -> w_left + width - 1.
    '''

    h_upper = random.randint(0, BOARD_HEIGHT) % BOARD_HEIGHT
    w_left = random.randint(0, BOARD_WIDTH) % BOARD_WIDTH
    width = min(random.randint(1, MAX_AREA), BOARD_WIDTH - w_left)
    if (width == 1 and h_upper == BOARD_HEIGHT - 1):
        return False
    #ensure box will be bounded by max area and the board
    height = min(random.randint(1, MAX_AREA // width), BOARD_HEIGHT - h_upper)
    #ensure we don't have a 1x1 rectangle
    if (width == 1):
        while (height == 1):
            height = min(random.randint(1, MAX_AREA // width), BOARD_HEIGHT - h_upper)
    
    def validate_box():
        #checks that we will not lower the number of necessary tiles to <= 1 for any priorities of tiles in the new box
        counts = {}
        for i in range(h_upper, h_upper + height):
            for j in range(w_left, w_left + width):
                if (priority[i][j] not in counts):
                    counts[priority[i][j]] = tile_counts[priority[i][j]]
                counts[priority[i][j]] -= 1
                if (counts[priority[i][j]] <= 1):
                    return False
        return True
    if not validate_box():
        return False
    
    def update_priority():
        tile_counts[box_count] = height * width
        box_order.append(((h_upper, w_left), (height, width)))
        for i in range(h_upper, h_upper + height):
            for j in range(w_left, w_left + width):
                tile_counts[priority[i][j]] -= 1
                priority[i][j] = box_count

    update_priority()
    return True

def stopping_condition(upper_bd):
    for prio in tile_counts.keys():
        if (tile_counts[prio] >= upper_bd):
            return False
    return True

def generate_priorities():
    curr = 1
    # note: if max_area <= board_total, then it's sufficient to only check the initial box has few enough necessarily filled tiles.
    # this would need to be modified if we used a different box generation logic that allowed for bigger boxes.
    # we don't need any lower bound checking since that's checked during generation
    while (not stopping_condition(5)):
        success = generate_rectangle(curr)
        if success:
            curr += 1
    return curr



def partition(num_parts):
    parts = [1] * num_parts
    remainder = BOX_TOTAL - num_parts
    for i in range(num_parts):
        split = random.randint(0, remainder)
        remainder -= split
        parts[i] += split
        if (remainder == 0):
            break
    parts[-1] += remainder
    random.shuffle(parts)
    return parts


num_rect = generate_priorities()
print(priority)
print(tile_counts)
print(box_order)
# dictionary of {priority:[] queue of the partition}
board_tiles = {}

def generate_numbers(num_rect):
    for i in range(num_rect):
        board_tiles[i] = partition(tile_counts[i])

generate_numbers(num_rect)
print(board_tiles)

def populate_board():
    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH):
            prio = priority[i][j]
            board[i][j] = board_tiles[prio][-1]
            board_tiles[prio].pop()

populate_board()

print()
print_board(priority)
print()
print_board(board)
box_order.reverse()
print(box_order)