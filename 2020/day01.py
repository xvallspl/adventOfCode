
def findTwoSum(infile, sum):
    with open(infile, "r") as f:
        lines = list(map(int, f))
        values = sorted(lines)
    lowit = 0
    topit = len(values)-1
    while values[lowit]+values[topit] > sum and topit>0:
        topit -= 1
    while lowit < topit:
        curSum = values[lowit]+values[topit]
        if curSum == sum:
            return values[lowit]*values[topit]
        if curSum < sum:
            lowit += 1
            topit += 1
        else:
            topit -= 1
    return -1


def memoizationFindTwoSum(infile, sum):
    seen = {}  # for O(1) lookup
    with open(infile, "r") as f:
        for line in f:
            n = int(line)
            if (sum-n) in seen:
                return n * (sum-n)
            seen[n] = True
    return -1


def findThreeSum(infile, sum):
    with open(infile, "r") as f:
        values = list(map(int, f))
    for n in values:
        m = findTwoSum(infile, sum-n)
        m = memoizationFindTwoSum(infile, sum-n)
        if m>0: break
    return n*m if m > 0 else -1


if __name__ == '__main__':
    print(findTwoSum("inputs/day01.txt", 2020))
    print(memoizationFindTwoSum("inputs/day01.txt", 2020))
    print(findThreeSum("inputs/day01.txt", 2020))
