t = int(input())
for case in range(1, t+1):
    d, p = [x for x in input().split(" ")]
    d = int(d)
    p = [x for x in p]

    power = 1
    damage = 0
    for i in range(len(p)):
        if p[i] == "C":
            power *= 2
            p[i] = power
        else:
            damage += power
            p[i] = -1 * power

    if damage <= d:
        print("Case #" + str(case) + ": 0")
        continue

    swap_count = 0
    success = False
    for i in range(len(p)-2, -1, -1):
        if p[i] > 0:
            for j in range(i, len(p)-1):
                p[j], p[j+1] = p[j+1], p[j]
                swap_count += 1
                damage -= p[j+1]/2
                p[j] = p[j]/2
                if damage <= d:
                    print("Case #" + str(case) + ": " + str(swap_count))
                    success = True
                    break
        if success:
            break

    if not success:
        print("Case #" + str(case) + ": IMPOSSIBLE")

