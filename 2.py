def invalid(numberstr):
    mid = len(numberstr) // 2
    return numberstr[:mid] == numberstr[mid:]


def part2invalid(numberstr):
    lennumberstr = len(numberstr)
    for chunksize in range(1, lennumberstr):
        if lennumberstr % chunksize == 0:
            if (
                len(        
                    set(
                        [
                            numberstr[i : i + chunksize]
                            for i in range(0, lennumberstr, chunksize)
                        ]
                    )
                )
                == 1
            ):
                return True


data = [i.split("-") for i in open("data/2demo.txt").readlines()[0].split(",")]
part1 = 0
part2 = 0
for first, last in data:
    for i in range(int(first), int(last) + 1):
        istr = str(i)
        if invalid(istr):
            part1 += i
        if part2invalid(istr):
            part2 += i

print("Part 1:", part1)
print("Part 2:", part2)
