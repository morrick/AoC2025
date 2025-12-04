# file = open("AoC3-1-test.txt")
file = open("AoC3-1-puzz.txt")
banks = file.read()


def find_largest_12digit(s):
    """
    Find the largest 12-digit number by selecting digits from left to right.

    Strategy: Use a greedy approach with lookahead to maximize the value.
    For each position in the result, choose the largest digit available
    while ensuring we have enough remaining digits to complete 12 digits.
    """
    n = len(s)
    if n < 12:
        return None  # Not enough digits

    result = []
    start = 0

    for pos in range(12):
        # How many more digits do we need after this one?
        remaining_needed = 12 - pos - 1

        # Latest position we can pick from (must leave enough digits)
        latest_pos = n - remaining_needed - 1

        # Find the maximum digit in the valid range
        max_digit = max(s[start : latest_pos + 1])

        # Find the first occurrence of this max digit
        for i in range(start, latest_pos + 1):
            if s[i] == max_digit:
                result.append(s[i])
                start = i + 1
                break

    return "".join(result)


def process_data(data):
    """Process multiple lines of digit sequences."""
    lines = [line.strip() for line in data.strip().split("\n") if line.strip()]
    results = []

    print("Processing each sequence:")
    print("-" * 50)

    for line in lines:
        largest = find_largest_12digit(line)
        if largest:
            results.append(int(largest))
            print(f"Input:  {line}")
            print(f"Output: {largest}")
            print()

    total = sum(results)
    print("-" * 50)
    print(f"Individual results: {' + '.join(map(str, results))}")
    print(f"Total sum: {total}")

    return results, total


# Run the solution
results, total = process_data(banks)


# part 1 test answer "The total output joltage is now much larger:
# 987654321111
# 811111111119
# 434234234278
# 888911112111
# ------------
# 3121910778619
#

# 144576682019514 is too low
# 170147128753455
