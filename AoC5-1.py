# file = open("AoC5-1-test.txt")
file = open("AoC5-1-puzz.txt")

fresh = []
ids = []
half = 1

for line in file:
    cl = line.strip()  # cleaned line
    if cl == "":
        half = 2
        continue
    if half == 1:
        fresh.append(cl)
    else:
        ids.append(cl)

obl = []
for rng in fresh:
    rngs = rng.split("-")
    obl.extend((list(range(int(rngs[0]), int(rngs[1])))))

print(set(obl))
