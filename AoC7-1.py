file = open("AoC7-1-test.txt")
# file = open("AoC7-1-puzz.txt")
lines = file.readlines()
print(lines)

for line in range(len(lines)):
    for char in range(len(line)):
        if line[char] == "S":
            # starting character only one laser underneath.
