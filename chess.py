def pawn_move_tracker(moves):
    board = [
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        [".", ".", ".", ".", ".", ".", ".", "."]
    ]

    check = 0
    for i in moves:
        if check % 2 == 0:
            if 'x' in i:
                num1 = ord(i[0]) - ord('a')
                num2 = ord(i[2]) - ord('a')

                row_to = 8 - int(i[3])

                if abs(num1 - num2) != 1:
                    return f'{i} is invalid'
                if board[row_to][num2] != 'p':
                    return f'{i} is invalid'

                board[row_to][num2] = 'P'
                board[row_to + 1][num1] = '.'
            else:
                num = ord(i[0]) - ord('a')
                row_to = 8 - int(i[1])

                if row_to + 1 < 8 and board[row_to + 1][num] == 'P' and board[row_to][num] == '.':
                    board[row_to + 1][num] = '.'
                    board[row_to][num] = 'P'
                elif row_to + 2 < 8 and board[row_to + 2][num] == 'P' and board[row_to + 1][num] == '.' and row_to == 4:
                    board[row_to + 2][num] = '.'
                    board[row_to][num] = 'P'
                else:
                    return f'{i} is invalid'
        else:
            if 'x' in i:
                num1 = ord(i[0]) - ord('a')
                num2 = ord(i[2]) - ord('a')
                row_to = 8 - int(i[3])

                if abs(num1 - num2) != 1:
                    return f'{i} is invalid'
                if board[row_to][num2] != 'P':
                    return f'{i} is invalid'

                board[row_to][num2] = 'p'
                board[row_to - 1][num1] = '.'
            else:
                num = ord(i[0]) - ord('a')
                row_to = 8 - int(i[1])

                if row_to - 1 >= 0 and board[row_to - 1][num] == 'p' and board[row_to][num] == '.':
                    board[row_to - 1][num] = '.'
                    board[row_to][num] = 'p'
                elif row_to - 2 >= 0 and board[row_to - 2][num] == 'p' and board[row_to - 1][num] == '.' and row_to == 3:
                    board[row_to - 2][num] = '.'
                    board[row_to][num] = 'p'
                else:
                    return f'{i} is invalid'

        check += 1

    return board
