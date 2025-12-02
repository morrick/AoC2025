# file = open("AoC1-1-test.txt")
file = open("AoC1-1-puzz.txt")
contents = file.read()
lines = contents.splitlines()
# The dial starts by pointing at 50.
pos = 50
zero_counter = 0
for turn in lines:
    if turn[:1] == "L":
        pos -= int(turn[1:])
    else:
        pos += int(turn[1:])
    if pos % 100 == 0:
        zero_counter += 1
print(zero_counter)
