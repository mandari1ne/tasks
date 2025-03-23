def count_nums(n):
    return sum(len(str(i)) for i in range(1, n + 1))


n = int(input())
print(count_nums(n))
