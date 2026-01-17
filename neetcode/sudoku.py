import random

def generate_sudoku():
    grid = [[0] * 9 for _ in range(9)]

    def is_valid(num, row, col):
        # Check row
        if num in grid[row]:
            return False

        # Check column
        for r in range(9):
            if grid[r][col] == num:
                return False

        # Check 3x3 sub grid
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if grid[r][c] == num:
                    return False

        return True

    def solve():
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    numbers = list(range(1, 10))
                    random.shuffle(numbers)
                    for num in numbers:
                        if is_valid(num, row, col):
                            grid[row][col] = num
                            if solve():
                                return True
                            grid[row][col] = 0
                    return False
        return True

    solve()
    return grid


# Example usage
sudoku = generate_sudoku()
for row in sudoku:
    print(row)
