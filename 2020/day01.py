
def orderFile(infile):
    with open(infile, "r") as f:
        lines = list(map(int, f))
        values = sorted(lines)
    lowit = 0
    topit = len(values)-1
    while values[lowit]+values[topit] > 2020:
        topit -= 1
    while lowit < topit:
        curSum = values[lowit]+values[topit]
        if curSum == 2020:
            return values[lowit]*values[topit]
        if curSum < 2020:
            lowit += 1
            topit += 1
        else:
            topit -= 1
    return -1

def memoization(infile):
    seen = {}
    with open(infile, "r") as f:
        for line in f:
            n = int(line)
            if (2020-n) in seen:
                return n * (2020-n)
            seen[n] = True
    return -1

if __name__ == '__main__':
    print(orderFile("inputs/day01.txt"))
    print(memoization("inputs/day01.txt"))
