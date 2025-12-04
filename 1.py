def rotate(startdial, direction, count):
    toucheszero = 0

    click = 1
    if direction == "L":
        click = -1

    for i in range(count):
        if startdial == 0:
            toucheszero += 1
        if startdial == 99 and click == 1:
            startdial = 0
        elif startdial == 0 and click == -1:
            startdial = 99
        else:
            startdial += click

    return startdial, startdial == 0, toucheszero


dial = 50
part1 = 0
part2 = 0
for i in open("data/1.txt"):
    dial, iszero, toucheszero = rotate(dial, i[0], int(i[1:]))
    part1 += iszero
    part2 += toucheszero

print("Part 1: ", part1)
print("Part 2: ", part2)
