def max_width(n, m, t):
    left, right = 1, min(n // 2, m // 2)

    while left <= right:
        mid = (left + right) // 2

        if n * m - (n - 2 * mid) * (m - 2 * mid) <= t:
            left = mid + 1
        elif n * m - (n - 2 * mid) * (m - 2 * mid) >= t:
            right = mid - 1

    return right

n = int(input())
m = int(input())
t = int(input())

print(max_width(n, m, t))
