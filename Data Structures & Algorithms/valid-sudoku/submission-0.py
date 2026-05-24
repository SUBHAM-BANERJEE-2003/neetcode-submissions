class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board[row])):
                cell = board[row][col]
                if cell == ".":
                    continue
                box = (row // 3, col // 3)
                if cell in rows[row] or cell in cols[col] or cell in boxes[box]:
                    return False
                rows[row].add(cell)
                cols[col].add(cell)
                boxes[box].add(cell)
        return True


