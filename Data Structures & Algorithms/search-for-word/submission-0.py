class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = set()

        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, visited, i, j, 0):
                    return True
        
        return False
    
    def dfs(self, board, word, visited, x, y, idx):
        if idx == len(word):
            return True
        if not (0 <= x < len(board) and 0 <= y < len(board[0])):
            return False
        if (x, y) in visited or board[x][y] != word[idx]:
            return False
        
        visited.add((x, y))

        found = (
            self.dfs(board, word, visited, x + 1, y, idx + 1) or
            self.dfs(board, word, visited, x - 1, y, idx + 1) or
            self.dfs(board, word, visited, x, y + 1, idx + 1) or
            self.dfs(board, word, visited, x, y - 1, idx + 1)
        )

        visited.remove((x, y))

        return found