def checker(list_):
    for i in list_:
        if all(x == 1 for x in i):
            return 1
        elif all(x == 2 for x in i):
            return 2

    if (list_[0][0] == list_[1][0] == list_[2][0] == 1 or
            list_[0][1] == list_[1][1] == list_[2][1] == 1 or
            list_[0][2] == list_[1][2] == list_[2][2] == 1 or
            list_[0][0] == list_[1][1] == list_[2][2] == 1 or
            list_[0][2] == list_[1][1] == list_[2][0] == 1):
        return 1
    elif (list_[0][0] == list_[1][0] == list_[2][0] == 2 or
            list_[0][1] == list_[1][1] == list_[2][1] == 2 or
            list_[0][2] == list_[1][2] == list_[2][2] == 2 or
            list_[0][0] == list_[1][1] == list_[2][2] == 2 or
            list_[0][2] == list_[1][1] == list_[2][0] == 2):
        return 2
    elif all(0 not in i for i in list_):
        return 0
    else:
        return -1

list_ = []
for i in range(3):
    list_.append(list(map(int, input().split())))

print(checker(list_))
