"""
this script will take in args a SDM string with 81 digits and it will transform it to a matrix
then it solve it and show the results
"""
import sys


def check_sdm_input(sdm_string: str):
    """
    function checking the format and the length of SDM STRING
    :param sdm_string: str
    :return: boolean
    """
    return sdm_string.isdigit() and len(sdm_string) == 81


def sdm_to_puzzle(string: str):
    """
    function transfromin given SDM string to a matrix
    :param string: str
    :return: list[][]
    """
    if not check_sdm_input(string):
        print('you need put a valid string with 81 digits')
        sys.exit()
    sudoku_puzzle = []
    for i in range(0, 9):
        start = i * 9
        end = (i + 1) * 9
        str = string[start:end]
        sudoku_puzzle.append([int(x) for x in str])
    return sudoku_puzzle


def puzzle_to_sdm(puzzle: list):
    """function transforming a matrix to a SDM STRING
    :param puzzle: list[][] a matrix to transform
    :return string
    """
    sdm = ''
    for i in range(0, 9):
        sdm += ''.join([str(s) for s in puzzle[i]])
    return sdm


def valid_puzzle(puzzle: list, num: int, pos: (int, int)):
    """function checking if a number will be valid in some position or not
    :param puzzle: list[][] a matrix from a sdm string
    :param num: int a number to place in a empty position
    :param pos: (int, int) a position (x, y)
    :return boolean
    ."""
    # Check row
    for i in range(len(puzzle[0])):
        if puzzle[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column
    for i in range(len(puzzle)):
        if puzzle[i][pos[1]] == num and pos[0] != i:
            return False
    # Check puzzlex
    puzzlex_x = pos[1] // 3
    puzzlex_y = pos[0] // 3
    for i in range(puzzlex_y*3, puzzlex_y*3 + 3):
        for j in range(puzzlex_x*3, puzzlex_x*3 + 3):
            if puzzle[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(puzzle: list):
    """
    recursive function trying to solve our soduku puzzle
    :param puzzle:list[][] our soduku puzzle
    :return: boolean, list[][] | string
    """
    find = find_empty(puzzle)
    if not find:  # if find is None or False
        return True, puzzle
    else:
        row, col = find
    for num in range(1, 10):
        if valid_puzzle(puzzle, num, (row, col)):
            puzzle[row][col] = num
            if solve(puzzle)[0]:
                return True, puzzle
            puzzle[row][col] = 0
    return False, 'Unsolvable'


def find_empty(puzzle: list):
    """
    function returning the near empty position in our puzzle
    :param puzzle: list[][] our soduku puzzle
    :return: (int, int) | None
    """
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 0:
                return i, j  # row, column
    return None


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('you need to specify a sdm string of 81 digits')
        print('you need run the script like this: python logparser.py [sdm_string]')
        sys.exit()
    sdm_string_input = sys.argv[1]
    puzzle = sdm_to_puzzle(sdm_string_input)
    solved, puzzle = solve(puzzle)
    if solved:
        sdm_string_output = puzzle_to_sdm(puzzle)
        print(sdm_string_output)
    else:
        print('Unsolvable')
