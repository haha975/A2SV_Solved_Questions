class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    v = board[r][c]
                    rows[r].add(v)
                    cols[c].add(v)
                    boxes[(r//3)*3 + (c//3)].add(v)

        empty = [(r, c) for r in range(9) for c in range(9) if board[r][c] == "."]

        def solver(idx):
            if idx == len(empty):
                return True

            r, c = empty[idx]
            b = (r//3)*3 + (c//3)

            for k in map(str, range(1, 10)):
                if k not in rows[r] and k not in cols[c] and k not in boxes[b]:

                    board[r][c] = k
                    rows[r].add(k)
                    cols[c].add(k)
                    boxes[b].add(k)

                    if solver(idx + 1):
                        return True

                    board[r][c] = "."
                    rows[r].remove(k)
                    cols[c].remove(k)
                    boxes[b].remove(k)

            return False

        solver(0)