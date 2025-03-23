def count_nums(n):
    count_ = 0
    for i in range(1, n + 1):
        count_ += len(str(i))

    return count_


n = int(input())
print(count_nums(n))
