def solve(board):
    rows = len(board)
    cols = len(board[0])
    # транспонированное поле
    transposed_board = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]

    # print(rows, cols)

    # уникальность элементов
    def check_uniq(board):
        # проверка строк
        for r in range(rows):
            row = [board[r][c] for c in range(cols) if board[r][c] != 0]
            if len(row) > len(set(row)):
                return False

        # проверка столбцов
        for c in range(cols):
            col = [board[r][c] for r in range(rows) if board[r][c] != 0]
            if len(col) > len(set(col)):
                return False

        # проверка 2x2 квадратов
        for r in range(0, rows, 2):
            for c in range(0, cols, 2):
                square = [board[r + i][c + j] for i in range(2) for j in range(2) if board[r + i][c + j] != 0]

                if len(square) != len(set(square)):
                    return False

        return True

    # проверка валидности доски
    def is_valid(board, r, c, num):
        if num in board[r]:
            return False

        if num in transposed_board[c]:
            return False

        return True

    def sudoku(board):
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 0:
                    for n in range(1, 5):
                        if is_valid(board, r, c, n):
                            board[r][c] = n
                            transposed_board[c] = [board[i][c] for i in range(rows)]

                            # рекурсия для дальнейшего решения судоку
                            if sudoku(board):
                                return True

                            # откат изменений
                            board[r][c] = 0
                            transposed_board[c] = [board[i][c] for i in range(rows)]

                    return False
        return True

    if sudoku(board):
        if not check_uniq(board):
            return 'This sudoku is unsolvable!'

        return board
    else:
        return 'This sudoku is unsolvable!'
