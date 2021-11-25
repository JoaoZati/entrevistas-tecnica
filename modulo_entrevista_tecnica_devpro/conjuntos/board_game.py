"""
>>> has_move(board_white_unfinished, 1, 1)
True
>>> has_move(board_white_finished, 0, 0)
False
>>> has_move(board_white_finished, 0, 3)
True
>>> has_move(board_white_finished, 3, 2)
True
>>> has_move(board_white_finished, 1, 1)
False
"""

BLACK = 'B'
WHITE = 'W'
EMPTY = 'E'


def has_move(board, line, column):
    """
    Show all moves can be done

    :param board: matrix m x n
    :param line: index line
    :param column: index column
    :return: True or False

    O(m*n) in time and space
    """

    m = len(board)
    if m == 0:
        raise Exception('Board must be one line at least')
    n = len(board[0])
    if n == 0:
        raise Exception('Board must be one line at least')
    color = board[line][column]
    if color == EMPTY:
        raise Exception('Initial position can be EMPTY')

    def adjacents(position):
        def interval(value, max_value):
            return range(max(value - 1, 0), min(value + 2, max_value))

        p_line, p_column = position
        line_interval = interval(p_line, m)
        column_interval = interval(p_column, n)

        return [(l, c) for l in line_interval for c in column_interval]

    def has_empty_adjacents(position):
        return any(board[p_line][p_column] == EMPTY for p_line, p_column in adjacents(position))

    def adjacents_with_same_color(position):
        return [(l, c) for l, c in adjacents(position) if color==board[l][c] ]

    to_be_visited = set([(line, column)])
    visited = set()

    while len(to_be_visited) > 0:
        curr_position = to_be_visited.pop()
        if has_empty_adjacents(curr_position):
            return True
        visited.add(curr_position)
        for p in adjacents_with_same_color(curr_position):
            if p not in visited:
                to_be_visited.add(p)

    return False


board_white_unfinished = [
    [EMPTY, EMPTY, EMPTY, EMPTY, ],
    [EMPTY, WHITE, BLACK, EMPTY, ],
    [EMPTY, WHITE, BLACK, EMPTY, ],
    [EMPTY, EMPTY, EMPTY, EMPTY, ],
]

board_white_finished = [
    [WHITE, WHITE, BLACK, BLACK, ],
    [WHITE, WHITE, BLACK, BLACK, ],
    [WHITE, WHITE, BLACK, BLACK, ],
    [WHITE, WHITE, BLACK, EMPTY, ],
]
