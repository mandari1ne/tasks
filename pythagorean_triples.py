def pythagorean_triplet(n):
    list_ = []

    for a in range(1, n // 2):
        for b in range(a + 1, n // 2):
            if n % a == 0 and n % b == 0 and (a ** 2 + b ** 2 == (n / a / b) ** 2):
                list_.append(a)
                list_.append(b)
                list_.append(int(n / a / b))
                break

    return list_


n = int(input())

print(pythagorean_triplet(n))
