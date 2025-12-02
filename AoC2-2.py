def is_valid_id(id_number):
    id_str = str(id_number)
    length = len(id_str)
    # A pattern must repeat at least twice, so max pattern length is length/2
    for pattern_length in range(1, length // 2 + 1, 1):
        # Only check if the pattern divides evenly into the total length
        if length % pattern_length == 0:
            pattern = id_str[:pattern_length]
            repetitions = length // pattern_length
            # Check if repeating this pattern recreates the entire ID
            if pattern * repetitions == id_str:
                return False  # Invalid - found a repeating pattern
    return True  # Valid - no repeating pattern found


# file = open("AoC2-1-test.txt")
file = open("AoC2-1-puzz.txt")
contents = file.read()
ranges = contents.split(",")
accumulator = 0
for ranges in ranges:
    boundries = ranges.split("-")
    # print(boundries)
    for int_id in range(int(boundries[0]), int(boundries[1]) + 1, 1):
        if is_valid_id(int_id) == False:
            print(int_id, is_valid_id(int_id))
            accumulator += int_id
print(accumulator)
# part 2 test answer is 4174379265
