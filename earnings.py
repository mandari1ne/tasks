def find_earning(earnings, k):
    max_d = [0] * (len(earnings) + 1)

    for i in range(1, len(earnings) + 1):
        sum_ = 0
        max_d[i] = max_d[i - 1]

        for j in range(1, min(k, i) + 1):
            sum_ += earnings[i - j]

            if i - j - 1 >= 0:
                max_d[i] = max(max_d[i], sum_ + max_d[i - j - 1])
            else:
                max_d[i] = max(max_d[i], sum_)

    return max_d[len(earnings)]

earnings = list(map(int, input().split()))
k = int(input())

print(find_earning(earnings, k))
