def isValid(row, col, n):
            for i in range(9):
                if board[row][i] == n:
                    return False
                if board[i][col] == n:
                    return False
                row_box = 3 * (row // 3) + i // 3
                col_box = 3 * (col // 3) + i % 3
                if board[row_box][col_box] == n:
                    return False
            return True

def solve(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        for n in range(1, 10):
                            if isValid(row, col, n):
                                board[row][col] = n
                                if solve(board):
                                    return True
                                else:
                                    board[row][col] = "."
                        return False
            return True
