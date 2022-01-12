from collections import defaultdict
from time import time

ALL = set(range(1,10))
MODES = (1,2,3)

class Sudoku:

    def __init__(self, G, mode):
        self.G = G
        assert mode in MODES
        self._mode = mode

    def valid_row(self, row):
        return {n for n in ALL if n not in self.G[row]}

    def valid_col(self, column):
        return ALL - {self.G[i][column] for i in range(9)}

    def valid_box(self, row, col):
        rs, cs = row-row%3, col-col%3
        return ALL - {self.G[r][c] for r in range(rs, rs+3) for c in range(cs, cs+3)} 

    def valid_vv(self, r, c):
        return self.valid_row(r) & self.valid_col(c) & self.valid_box(r, c)

    def done(self):
        return 0 not in [j for k in self.G for j in k]

    def solve(self):
        if self._mode == 1:
            return self._solve1()
        elif self._mode == 2:
            return self._solve2()
        elif self._mode == 3:
            return self._solve3()

    def _solve1(self):
        """
        Process cell by cell without any priorization.
        """
        if self.done():
            return self.G

        for r in range(9):
            for c in range(9):
                if self.G[r][c] == 0:
                    vv = self.valid_vv(r, c)
                    if not vv:
                        return None
                    for v in vv:
                        self.G[r][c] = v
                        if self.solve():
                            return self.G
                        self.G[r][c] = 0

        return None


    def _solve2(self):
        """
        Process cells with fewer possibilities first but go deep immediately.
        """
        if self.done():
            return self.G

        mn = None
        for r in range(9):
            for c in range(9):
                if self.G[r][c] == 0:
                    vv = self.valid_vv(r, c)
                    if not vv:
                        return None
                    if mn is None or len(vv) < len(mn[1]):
                        mn = (r,c), vv

        (r,c), vv = mn
        for v in vv:
            self.G[r][c] = v
            if self.solve():
                return self.G
            self.G[r][c] = 0

    def _solve3(self):
        """
        First fill all cells with just one possibility and repeat as long as
        there are such cells. Then continue with cells prioritizing ones with
        fewer possibilites.
        """
        if self.done():
            return self.G

        CH = set()
        OPEN = set()
        for r in range(9):
            for c in range(9):
                if self.G[r][c] == 0:
                    vv = self.valid_vv(r, c)
                    if not vv:
                        for r,c in CH:
                            self.G[r][c] = 0
                        return None
                    if len(vv) == 1:
                        CH.add((r,c))
                        self.G[r][c] = next(iter(vv))
                    else:
                        OPEN.add((r,c))

        if self.done():
            return self.G
        
        if CH:
            if self.solve():
                return self.G
        elif OPEN:
            nx = None
            for r,c in OPEN:
                vv = self.valid_vv(r, c)
                if not vv:
                    break
                if nx is None or len(nx[1]) > len(vv):
                    nx = (r,c), vv

            (r,c), vv = nx
            for v in vv:
                self.G[r][c] = v
                if self.solve():
                    return self.G
                self.G[r][c] = 0

        for r,c in CH:
            self.G[r][c] = 0
        return None

    def _solve4(self):
        """
        First fill all cells with just one possibility and repeat as long as
        there are such cells. Then continue with cells prioritizing ones with
        fewer possibilites.
        """
        if self.done():
            return self.G

        OPEN = set()
        while 1:
            for r in range(9):
                for c in range(9):
                    if self.G[r][c] == 0:
                        vv = self.valid_vv(r, c)
                        if not vv:
                            for r,c in CH:
                                self.G[r][c] = 0
                            return None
                        if len(vv) == 1:
                            CH.add((r,c))
                            self.G[r][c] = next(iter(vv))
                        else:
                            OPEN.add((r,c))

            
        CH = set()
        OPEN = set()
        for r in range(9):
            for c in range(9):
                if self.G[r][c] == 0:
                    vv = self.valid_vv(r, c)
                    if not vv:
                        for r,c in CH:
                            self.G[r][c] = 0
                        return None
                    if len(vv) == 1:
                        CH.add((r,c))
                        self.G[r][c] = next(iter(vv))
                    else:
                        OPEN.add((r,c))

        if self.done():
            return self.G
        
        if CH:
            if self.solve():
                return self.G
        elif OPEN:
            nx = None
            for r,c in OPEN:
                vv = self.valid_vv(r, c)
                if not vv:
                    break
                if nx is None or len(nx[1]) > len(vv):
                    nx = (r,c), vv

            (r,c), vv = nx
            for v in vv:
                self.G[r][c] = v
                if self.solve():
                    return self.G
                self.G[r][c] = 0

        for r,c in CH:
            self.G[r][c] = 0
        return None
    
    def __repr__(self):
        res = ''
        for r in range(9):
            if r % 3 == 0 and r != 0:
                res += ("-"*11) + "\n"
            for c in range(9):
                if c % 3 == 0 and c != 0:
                    res += "|"
                res += str(self.G[r][c])
            res += '\n'
        return res


gg = [
    [[0, 0, 0, 2, 6, 0, 7, 0, 1],
     [6, 8, 0, 0, 7, 0, 0, 9, 0],
     [1, 9, 0, 0, 0, 4, 5, 0, 0],
     [8, 2, 0, 1, 0, 0, 0, 4, 0],
     [0, 0, 4, 6, 0, 2, 9, 0, 0],
     [0, 5, 0, 0, 0, 3, 0, 2, 8],
     [0, 0, 9, 3, 0, 0, 0, 7, 4],
     [0, 4, 0, 0, 5, 0, 0, 3, 6],
     [7, 0, 3, 0, 1, 8, 0, 0, 0]],

    [[1, 0, 0, 4, 8, 9, 0, 0, 6],
     [7, 3, 0, 0, 0, 0, 0, 4, 0],
     [0, 0, 0, 0, 0, 1, 2, 9, 5],
     [0, 0, 7, 1, 2, 0, 6, 0, 0],
     [5, 0, 0, 7, 0, 3, 0, 0, 8],
     [0, 0, 6, 0, 9, 5, 7, 0, 0],
     [9, 1, 4, 6, 0, 0, 0, 0, 0],
     [0, 2, 0, 0, 0, 0, 0, 3, 7],
     [8, 0, 0, 5, 1, 2, 0, 0, 4]],

    [[0, 2, 0, 6, 0, 8, 0, 0, 0],
     [5, 8, 0, 0, 0, 9, 7, 0, 0],
     [0, 0, 0, 0, 4, 0, 0, 0, 0],
     [3, 7, 0, 0, 0, 0, 5, 0, 0],
     [6, 0, 0, 0, 0, 0, 0, 0, 4],
     [0, 0, 8, 0, 0, 0, 0, 1, 3],
     [0, 0, 0, 0, 2, 0, 0, 0, 0],
     [0, 0, 9, 8, 0, 0, 0, 3, 6],
     [0, 0, 0, 3, 0, 6, 0, 9, 0]],

    [[0, 0, 0, 6, 0, 0, 4, 0, 0],
     [7, 0, 0, 0, 0, 3, 6, 0, 0],
     [0, 0, 0, 0, 9, 1, 0, 8, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 5, 0, 1, 8, 0, 0, 0, 3],
     [0, 0, 0, 3, 0, 6, 0, 4, 5],
     [0, 4, 0, 2, 0, 0, 0, 6, 0],
     [9, 0, 3, 0, 0, 0, 0, 0, 0],
     [0, 2, 0, 0, 0, 0, 1, 0, 0]]
]

for i in range(len(gg)):
    for m in MODES[::-1]:
        if m == 1 and i > 1:
            print(f"g{i+1}, mode{m}, very long")
            continue
        sud = Sudoku([[*row] for row in gg[i]], m)
        s = time()
        assert sud.solve()
        print(f"g{i+1}, mode{m}, {time()-s:.8f}")
    print()

