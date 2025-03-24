def check_flats(k1, m, k2, p2, n2):
    floor_k2 = (p2 - 1) * m + n2

    x_min = (k2 + floor_k2 - 1) // floor_k2
    x_max = (k2 - 1) // (floor_k2 - 1) if floor_k2 > 1 else 10 ** 6

    possible = set()

    for x in range(x_min, x_max + 1):
        floor_k2_check = (k2 + x - 1) // x
        p_check = (floor_k2_check + m - 1) // m
        n_check = floor_k2_check - (p_check - 1) * m

        if p_check == p2 and n_check == n2:
            floor_k1 = (k1 + x - 1) // x
            p1 = (floor_k1 + m - 1) // m
            n1 = floor_k1 - (p1 - 1) * m

            possible.add((p1, n1))

    if not possible:
        return -1, -1
    elif len(possible) > 1:
        p_vals = {i[0] for i in possible}
        n_vals = {i[1] for i in possible}

        p1 = 0 if len(p_vals) > 1 else p_vals.pop()
        n1 = 0 if len(n_vals) > 1 else n_vals.pop()

        return p1, n1

    else:
        return possible.pop()


k1, m, k2, p2, n2 = map(int, input().split())
p1, n1 = check_flats(k1, m, k2, p2, n2)
print(p1, n1)
