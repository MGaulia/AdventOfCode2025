from collections import deque

ranges = []

startends = []
res = 0
for i in open("data/5.txt").readlines():
    i = i.rstrip()
    if i == "":
        continue
    if "-" in i:
        start, end = i.split("-")
        ranges.append(range(int(start), int(end) + 1))
        startends.append((int(start), int(end)))
    else:
        for r in ranges:
            if int(i) in r:
                res += 1
                break

print("Part 1:", res)

startends = sorted(startends)
dq = deque()
for i in startends:
    dq.append(i)

temp = []
while dq:
    s, e = dq.popleft()
    if not dq:
        temp.append((s, e))
        break
    ss, ee = dq.popleft()
    if ss <= e:
        dq.appendleft((min(s, ss), max(e, ee)))
    else:
        temp.append((s, e))
        dq.appendleft((ss, ee))

res = 0
for s, e in temp:
    res += e - s + 1

print("Part 2:", res)
