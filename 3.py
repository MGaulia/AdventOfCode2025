part1 = 0
for i in open("data/3demo.txt").readlines():
    maxjoltage = 0
    left = 0
    while left != len(i) - 2:
        right = left + 1
        while right != len(i) - 1:
            maxjoltage = max(maxjoltage, int(i[left] + i[right]))
            right += 1
        left += 1

    part1 += maxjoltage

print("Part 1:", part1)


def getearliestmaxid(list):
    list = list[::-1]
    maxid = -1
    max = -1
    for i in range(len(list)):
        val = int(list[i])
        if val >= max:
            max = val
            maxid = i

    return len(list) - 1 - maxid


part2 = 0
for i in open("data/3.txt").readlines():
    i = i.rstrip()
    startfrom = 0
    needed = 12
    length = len(i)
    res = ""
    while len(res) != 12:
        earliestmaxid = getearliestmaxid(i[startfrom : length - needed + 1])
        res += i[startfrom + earliestmaxid]
        startfrom = startfrom + earliestmaxid + 1
        needed -= 1
    part2 += int(res)

print("Part 2:", part2)
