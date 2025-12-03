def lnl(bank):  # largest not last
    # make it a set
    set_bank = set(bank)
    largest = max(set_bank)  # find the biggest
    # account for multiple positions of the largest that include the last
    if bank.find(largest) == (len(bank) - 1):  # make sure its not the last number
        set_bank.remove(largest)  # disqualify number
        return max(set_bank)  # take second choice
    else:
        return largest


# file = open("AoC3-1-test.txt")
file = open("AoC3-1-puzz.txt")
banks = file.read().splitlines()
# print(banks)
# print(len(banks))
total = 0
for bank in banks:
    largest = lnl(bank)
    index_of = bank.index(largest)
    second = max(bank[index_of + 1 :])
    answer = int("{}{}".format(largest, second))
    print("bank:", bank)
    print("answer=", answer)
    total += answer
print("total:", total)
# part 1 test answer 98 + 89 + 78 + 92 = 357
