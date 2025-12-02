# file = open("AoC2-1-test.txt")
file = open("AoC2-1-puzz.txt")
contents = file.read()
ranges = contents.split(",")
accumulator = 0
for ranges in ranges:
    boundries = ranges.split("-")
    for int_id in range(int(boundries[0]), int(boundries[1]) + 1, 1):
        str_id = str(int_id)
        if len(str_id) % 2 != 0:  # odd number of characters can't be a repeated set
            continue
        mp = len(str_id) // 2  # mp is midpoint
        if str_id[:mp] == str_id[mp:]:
            accumulator += int_id
print(accumulator)
# part 1 test answer is 1227775554
