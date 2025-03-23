n, m, k = map(int, input().split())

list_mines = []
for i in range(k):
    list_mines.append(tuple(map(int, input().split())))

matrix = [[0 for j in range(m + 2)] for i in range(n + 2)]

for i in list_mines:
    matrix[i[0]][i[1]] = '*'

    if matrix[i[0]][i[1] - 1] != '*':
        matrix[i[0]][i[1] - 1] += 1

    if matrix[i[0] - 1][i[1] - 1] != '*':
        matrix[i[0] - 1][i[1] - 1] += 1

    if matrix[i[0] - 1][i[1]] != '*':
        matrix[i[0] - 1][i[1]] += 1

    if matrix[i[0] - 1][i[1] + 1] != '*':
        matrix[i[0] - 1][i[1] + 1] += 1

    if matrix[i[0]][i[1] + 1] != '*':
        matrix[i[0]][i[1] + 1] += 1

    if matrix[i[0] + 1][i[1] + 1] != '*':
        matrix[i[0] + 1][i[1] + 1] += 1

    if matrix[i[0] + 1][i[1]] != '*':
        matrix[i[0] + 1][i[1]] += 1

    if matrix[i[0] + 1][i[1] - 1] != '*':
        matrix[i[0] + 1][i[1] - 1] += 1


for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(matrix[i][j], end=' ')
    print()
