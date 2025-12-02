# file = open("AoC1-1-test.txt")
file = open("AoC1-1-puzz.txt")
contents = file.read()
lines = contents.splitlines()
# The dial starts by pointing at 50.
pos = 50
zeros = 0
for turn in lines:
    direction = turn[:1]
    clicks = int(turn[1:])
    for i in range(clicks):
        if direction == "L":
            pos -= 1
        else:
            pos += 1
        if pos % 100 == 0:
            zeros += 1
print(zeros)
