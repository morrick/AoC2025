def check(x, y):
    global all_pos
    if x > 0 and x < w and y > 0 and y < h and rolls[x][y] == "@":
        return True
    else:
        return False


file = open("AoC4-1-test.txt")
# file = open("AoC4-1-puzz.txt")
rolls = file.read().splitlines()

h = len(rolls)
w = len(rolls[0])
all_pos = h * w
newmap = ""

for x in range(w):
    for y in range(h):
        if rolls[x][y] == ".":
            newmap += "."
            continue
        neighbours = 0
        # check N
        if check(x,y-1):
            neighbours += 1
        # check NE
        if check(x+1,y-1):
            neighbours += 1
        # check E
        if check(x+1,y):
            neighbours += 1
        # check SE
        if check(x+1,y+1):
            neighbours += 1
        # check S
        if check(x,y+1):
            neighbours += 1
        # check SW
        if check(x-1,y+1):
            neighbours += 1
        # check W
        if check(x-1,y):
            neighbours += 1
        # check NW
        if check(x-1,y-1):
            neighbours += 1

        if neighbours < 4:
            newmap += "x"
        else:
            newmap += "@"

for i in range(h):
    for j in range(w):
        print(newmap[i * w + j], end="")
    print("")

# The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions.

# part 1 test answer:
"""
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
"""
