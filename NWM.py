
class NWMatrix(object):
    def __init__(self, str1: str, str2: str, match=1, mismatch=-1, gap=-1):
        self.str1 = str1
        self.str2 = str2
        self.h = len(str1) + 1
        self.w = len(str2) + 1
        self.mtrx = [[0 for _ in range(self.w)] for _ in range(self.h)]
        self.sc_match = match
        self.sc_mismatch = mismatch
        self.sc_gap = gap

    def weight(self) -> int:
        return self.mtrx[self.h - 1][self.w - 1]

    def diff(self, a: chr, b: chr) -> int:
        if a == b:
            return self.sc_match
        else:
            return self.sc_mismatch

    def construct_matrix(self):
        for i in range(self.h):
            self.mtrx[i][0] = self.sc_gap * i
        for j in range(self.w):
            self.mtrx[0][j] = self.sc_gap * j
        for i in range(1, self.h):
            for j in range(1, self.w):
                self.mtrx[i][j] = max(self.mtrx[i - 1][j - 1] + self.diff(self.str1[i - 1], self.str2[j - 1]),
                                      self.mtrx[i - 1][j] + self.sc_gap,
                                      self.mtrx[i][j - 1] + self.sc_gap)

    def print_matrix(self, cell_width: int):
        print(' ' * cell_width, end=' ')
        for j in range(self.w):
            print(' ' * (cell_width - 1), (' ' + self.str2)[j], end=' ', sep='')
        print()

        for i in range(self.h):
            print(' ' * (cell_width - 1), (' ' + self.str1)[i], end=' ', sep='')
            for j in range(self.w):
                print(format(self.mtrx[i][j], f'{cell_width}d'), end=' ')
            print()

    def find_best(self) -> (str, str):
        res1 = ''
        res2 = ''
        i = self.h - 1
        j = self.w - 1
        while i != 0 or j != 0:
            this = self.mtrx[i][j]
            diag = self.mtrx[i - 1][j - 1]
            left = self.mtrx[i][j - 1]
            if this == diag + self.diff(self.str1[i - 1], self.str2[j - 1]):
                res1 = self.str1[i - 1] + res1
                res2 = self.str2[j - 1] + res2
                i -= 1
                j -= 1
            elif this == left + self.sc_gap:
                res1 = '_' + res1
                res2 = self.str2[j - 1] + res2
                j -= 1
            else:
                res1 = self.str1[i - 1] + res1
                res2 = '_' + res2
                i -= 1
        return res1, res2
