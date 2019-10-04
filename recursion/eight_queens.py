""" Write an algorithm to print all ways of 
    arranging eight queens on an 8x8 chess board 
    so that none of them share the same row, column, 
    or diagonal. In this case, "diagonal" means all 
    diagonals, not just the two that bisect the board.
"""

board = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1]
]


def get_available_row(board):
    # If any row is available, return
    for row in board:
        


def place_queens(board=[]):
    # Recurse every row that's left as possible placing option
    row_idx = get_available_row(board)
    for col_idx in range(len(board[row_idx])):
        if col[0] == None:
            continue
        # Place

