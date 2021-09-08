import unittest
import unittest.mock
import io
import sudokusolve


class MyTestCase(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, expected_output, func, mock_stdout, **kwargs):
        func(**kwargs)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_check_sdm_input(self):
        self.assertEqual(sudokusolve.check_sdm_input('AAAA'), False)
        self.assertEqual(sudokusolve.check_sdm_input('004006079000000602056092300078061030509000406020540890007410920105000000840600100'), True)
        self.assertEqual(sudokusolve.check_sdm_input('0040060790000006020560923000780A1030509000406020540890007410920105000000840600100'), False)

    def test_sdm_to_puzzle(self):
        with self.assertRaises(SystemExit):
            kwargs = {'string': 'AAAA'}
            self.assert_stdout(
                'you need put a valid string with 81 digits\n',
                sudokusolve.sdm_to_puzzle,
                **kwargs
            )
            kwargs = {'string': '0040060790000006020560923000780A1030509000406020540890007410920105000000840600100'}
            self.assert_stdout(
                'you need put a valid string with 81 digits\n',
                sudokusolve.sdm_to_puzzle,
                **kwargs
            )
        expected_puzzle = [
            [0, 0, 4, 0, 0, 6, 0, 7, 9],
            [0, 0, 0, 0, 0, 0, 6, 0, 2],
            [0, 5, 6, 0, 9, 2, 3, 0, 0],
            [0, 7, 8, 0, 6, 1, 0, 3, 0],
            [5, 0, 9, 0, 0, 0, 4, 0, 6],
            [0, 2, 0, 5, 4, 0, 8, 9, 0],
            [0, 0, 7, 4, 1, 0, 9, 2, 0],
            [1, 0, 5, 0, 0, 0, 0, 0, 0],
            [8, 4, 0, 6, 0, 0, 1, 0, 0]
        ]
        sdm_string = '004006079000000602056092300078061030509000406020540890007410920105000000840600100'
        self.assertEqual(sudokusolve.sdm_to_puzzle(sdm_string), expected_puzzle)

    def test_puzzle_to_sdm(self):
        puzzle = [
            [0, 0, 4, 0, 0, 6, 0, 7, 9],
            [0, 0, 0, 0, 0, 0, 6, 0, 2],
            [0, 5, 6, 0, 9, 2, 3, 0, 0],
            [0, 7, 8, 0, 6, 1, 0, 3, 0],
            [5, 0, 9, 0, 0, 0, 4, 0, 6],
            [0, 2, 0, 5, 4, 0, 8, 9, 0],
            [0, 0, 7, 4, 1, 0, 9, 2, 0],
            [1, 0, 5, 0, 0, 0, 0, 0, 0],
            [8, 4, 0, 6, 0, 0, 1, 0, 0]
        ]
        expected_sdm_string = '004006079000000602056092300078061030509000406020540890007410920105000000840600100'
        self.assertEqual(sudokusolve.puzzle_to_sdm(puzzle), expected_sdm_string)

    def test_valid_puzzle(self):
        puzzle = [
            [0, 0, 4, 0, 0, 6, 0, 7, 9],
            [0, 0, 0, 0, 0, 0, 6, 0, 2],
            [0, 5, 6, 0, 9, 2, 3, 0, 0],
            [0, 7, 8, 0, 6, 1, 0, 3, 0],
            [5, 0, 9, 0, 0, 0, 4, 0, 6],
            [0, 2, 0, 5, 4, 0, 8, 9, 0],
            [0, 0, 7, 4, 1, 0, 9, 2, 0],
            [1, 0, 5, 0, 0, 0, 0, 0, 0],
            [8, 4, 0, 6, 0, 0, 1, 0, 0]
        ]
        self.assertEqual(sudokusolve.valid_puzzle(puzzle, 1, (0, 0)), False)
        self.assertEqual(sudokusolve.valid_puzzle(puzzle, 2, (0, 0)), True)
        self.assertEqual(sudokusolve.valid_puzzle(puzzle, 2, (1, 0)), False)

    def test_solve(self):
        puzzle = [
            [0, 0, 4, 0, 0, 6, 0, 7, 9],
            [0, 0, 0, 0, 0, 0, 6, 0, 2],
            [0, 5, 6, 0, 9, 2, 3, 0, 0],
            [0, 7, 8, 0, 6, 1, 0, 3, 0],
            [5, 0, 9, 0, 0, 0, 4, 0, 6],
            [0, 2, 0, 5, 4, 0, 8, 9, 0],
            [0, 0, 7, 4, 1, 0, 9, 2, 0],
            [1, 0, 5, 0, 0, 0, 0, 0, 0],
            [8, 4, 0, 6, 0, 0, 1, 0, 0]
        ]
        expected_puzzle = [
            [2, 8, 4, 1, 3, 6, 5, 7, 9],
            [9, 1, 3, 7, 5, 4, 6, 8, 2],
            [7, 5, 6, 8, 9, 2, 3, 4, 1],
            [4, 7, 8, 9, 6, 1, 2, 3, 5],
            [5, 3, 9, 2, 8, 7, 4, 1, 6],
            [6, 2, 1, 5, 4, 3, 8, 9, 7],
            [3, 6, 7, 4, 1, 5, 9, 2, 8],
            [1, 9, 5, 3, 2, 8, 7, 6, 4],
            [8, 4, 2, 6, 7, 9, 1, 5, 3]
        ]

        self.assertEqual(sudokusolve.solve(puzzle), (True, expected_puzzle))
        puzzle = [
            [0, 0, 4, 0, 0, 6, 0, 7, 9],
            [0, 0, 0, 0, 0, 0, 6, 0, 2],
            [1, 5, 6, 0, 9, 2, 3, 0, 0],
            [0, 7, 8, 0, 6, 1, 0, 3, 0],
            [5, 0, 9, 5, 0, 0, 4, 0, 6],
            [0, 2, 0, 5, 4, 0, 8, 9, 0],
            [0, 0, 7, 4, 1, 0, 9, 2, 0],
            [1, 0, 5, 0, 0, 0, 0, 0, 0],
            [8, 4, 0, 6, 0, 0, 1, 0, 0]
        ]
        self.assertEqual(sudokusolve.solve(puzzle), (False, False))

    def test_find_empty(self):
        puzzle = [
            [0, 0, 4, 0, 0, 6, 0, 7, 9],
            [0, 0, 0, 0, 0, 0, 6, 0, 2],
            [0, 5, 6, 0, 9, 2, 3, 0, 0],
            [0, 7, 8, 0, 6, 1, 0, 3, 0],
            [5, 0, 9, 0, 0, 0, 4, 0, 6],
            [0, 2, 0, 5, 4, 0, 8, 9, 0],
            [0, 0, 7, 4, 1, 0, 9, 2, 0],
            [1, 0, 5, 0, 0, 0, 0, 0, 0],
            [8, 4, 0, 6, 0, 0, 1, 0, 0]
        ]
        self.assertEqual(sudokusolve.find_empty(puzzle), (0, 0))
        puzzle = [
            [1, 5, 4, 3, 8, 6, 6, 7, 9],
            [2, 4, 8, 4, 9, 8, 6, 7, 2],
            [3, 5, 6, 7, 9, 2, 3, 3, 8],
            [1, 7, 8, 1, 6, 1, 0, 3, 0],
            [5, 0, 9, 0, 0, 0, 4, 4, 6],
            [0, 2, 0, 5, 4, 0, 8, 9, 0],
            [0, 0, 7, 4, 1, 0, 9, 2, 0],
            [1, 0, 5, 0, 0, 0, 0, 0, 0],
            [8, 4, 0, 6, 0, 0, 1, 0, 0]
        ]
        self.assertEqual(sudokusolve.find_empty(puzzle), (3, 6))
        puzzle = [
            [2, 8, 4, 1, 3, 6, 5, 7, 9],
            [9, 1, 3, 7, 5, 4, 6, 8, 2],
            [7, 5, 6, 8, 9, 2, 3, 4, 1],
            [4, 7, 8, 9, 6, 1, 2, 3, 5],
            [5, 3, 9, 2, 8, 7, 4, 1, 6],
            [6, 2, 1, 5, 4, 3, 8, 9, 7],
            [3, 6, 7, 4, 1, 5, 9, 2, 8],
            [1, 9, 5, 3, 2, 8, 7, 6, 4],
            [8, 4, 2, 6, 7, 9, 1, 5, 3]
        ]
        self.assertEqual(sudokusolve.find_empty(puzzle), None)


if __name__ == '__main__':
    unittest.main()
