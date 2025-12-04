def print_map(map):
    for row in map:
        print(row)


def check(map, x, y):
    if x >= 0 and x < w and y >= 0 and y < h and map[x][y] == "@":
        return True
    else:
        return False


def run_map(map):
    global total
    counter = 0
    newmap = ""

    for x in range(w):
        for y in range(h):
            if map[x][y] == ".":
                newmap += "."
                continue

            neighbours = 0
            # check N
            if check(map, x, y - 1):
                neighbours += 1
            # check NE
            if check(map, x + 1, y - 1):
                neighbours += 1
            # check E
            if check(map, x + 1, y):
                neighbours += 1
            # check SE
            if check(map, x + 1, y + 1):
                neighbours += 1
            # check S
            if check(map, x, y + 1):
                neighbours += 1
            # check SW
            if check(map, x - 1, y + 1):
                neighbours += 1
            # check W
            if check(map, x - 1, y):
                neighbours += 1
            # check NW
            if check(map, x - 1, y - 1):
                neighbours += 1

            if neighbours < 4:
                newmap += "x"
                counter += 1
            else:
                newmap += "@"

    if counter == 0:
        return
    else:
        total += counter
        tempmap = []
        for i in range(h):
            temp_char = ""
            for j in range(w):
                temp_char += (
                    "."
                    if newmap[i * w + j] == "." or newmap[i * w + j] == "x"
                    else newmap[i * w + j]
                )
            tempmap.append(temp_char)

        run_map(tempmap)


# file = open("AoC4-1-test.txt")
file = open("AoC4-1-puzz.txt")
rolls = file.read().splitlines()

h = len(rolls)
w = len(rolls[0])

total = 0

run_map(rolls)

print(total)

# part 2 test answer:
# there are 43 x's removed
