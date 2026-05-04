# https://www.codewars.com/kata/525caa5c1bf619d28c000335
import pytest

board = [[2, 1, 1], [0, 1, 2], [2, 1, 0]]


def is_solved(board):
    winning_lines = [
        (board[0][0], board[0][1], board[0][2]),  # 0 row
        (board[1][0], board[1][1], board[1][2]),  # 1 row
        (board[2][0], board[2][1], board[2][2]),  # 2 row
        (board[0][0], board[1][0], board[2][0]),  # 0 column
        (board[0][1], board[1][1], board[2][1]),  # 1 column
        (board[0][2], board[1][2], board[2][2]),  # 2 column
        (board[0][0], board[1][1], board[2][2]),  # 1 main diag
        (board[0][2], board[1][1], board[2][0]),
    ]  # 2 anti diag

    for wline in winning_lines:
        if wline[0] == wline[1] == wline[2] and wline[0] != 0:
            return wline[0]

    if any(0 in row for row in board):
        return -1

    return 0


test_board_A = [[0, 0, 1], [0, 1, 2], [2, 1, 0]]
test_board_B = [[1, 1, 1], [0, 2, 2], [0, 0, 0]]
test_board_C = [[2, 1, 2], [2, 1, 1], [1, 1, 2]]
test_board_D = [[2, 1, 2], [2, 1, 1], [1, 2, 1]]


@pytest.mark.parametrize(
    "board, expected_res",
    [
        (test_board_A, -1),
        (test_board_B, 1),
        (test_board_C, 1),
        (test_board_D, 0),
    ],
)
def test_is_solved(board, expected_res):
    assert is_solved(board) == expected_res
