def check_true(list_turtles):
    k = 0

    for index, i in enumerate(list_turtles):
        if i[0] == index and i[1] == len(list_turtles) - index - 1:
            k += 1

    return k


n = int(input())

list_turtles = []
for i in range(n):
    list_turtles.append(tuple(map(int, input().split())))

list_turtles = sorted(list_turtles, key=lambda x: (x[1], -x[0]), reverse=True)

print(check_true(list_turtles))
