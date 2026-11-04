class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    # This problem can be viewed as a grid validation problem.
    # Each row, column, and 3 by 3 square can't have duplicate digits and only contain digits from 1 to 9.
    # To solve it, I use three hash maps to track rows, columns, and squares.
    # When I see a digit, I check whether it already exists in the corresponding row, column, or 3 by 3 square.
    # If it does, I return false; otherwise, I add it.
    # The time and space complexity are both O(n^2), where n is the size of the board, since each cell is visited at most once.

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        n = len(board)
        for i in range(n):
            for j in range(n):
                if board[i][j] != ".":
                    num = board[i][j]
                    if num in rows[i] or num in cols[j] or num in squares[(i // 3, j // 3)]:
                        return False
                    rows[i].add(num)
                    cols[j].add(num)
                    squares[(i // 3, j // 3)].add(num)
        
        return True
        