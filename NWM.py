
class NWMatrix(object):
    def __init__(self, str1: str, str2: str, match=1, mismatch=-1, gap=-1):
        self.__str1 = str1
        self.__str2 = str2
        self.__h = len(str1) + 1
        self.__w = len(str2) + 1
        self.__mtrx = [[0 for _ in range(self.__w)] for _ in range(self.__h)]
        self.__sc_match = match
        self.__sc_mismatch = mismatch
        self.__sc_gap = gap

    def weight(self) -> int:
        return self.__mtrx[self.__h - 1][self.__w - 1]

    def diff(self, a: chr, b: chr) -> int:
        if a == b:
            return self.__sc_match
        else:
            return self.__sc_mismatch

    def construct_matrix(self):
        for i in range(self.__h):
            self.__mtrx[i][0] = self.__sc_gap * i
        for j in range(self.__w):
            self.__mtrx[0][j] = self.__sc_gap * j
        for i in range(1, self.__h):
            for j in range(1, self.__w):
                self.__mtrx[i][j] = max(self.__mtrx[i - 1][j - 1] + self.diff(self.__str1[i - 1], self.__str2[j - 1]),
                                      self.__mtrx[i - 1][j] + self.__sc_gap,
                                      self.__mtrx[i][j - 1] + self.__sc_gap)

    def print_matrix(self, cell_width: int):
        print(' ' * cell_width, end=' ')
        for j in range(self.__w):
            print(' ' * (cell_width - 1), (' ' + self.__str2)[j], end=' ', sep='')
        print()

        for i in range(self.__h):
            print(' ' * (cell_width - 1), (' ' + self.__str1)[i], end=' ', sep='')
            for j in range(self.__w):
                print(format(self.__mtrx[i][j], f'{cell_width}d'), end=' ')
            print()

    def find_best(self) -> (str, str):
        res1 = ''
        res2 = ''
        i = self.__h - 1
        j = self.__w - 1
        while i != 0 or j != 0:
            this = self.__mtrx[i][j]
            diag = self.__mtrx[i - 1][j - 1]
            left = self.__mtrx[i][j - 1]
            if this == diag + self.diff(self.__str1[i - 1], self.__str2[j - 1]):
                res1 = self.__str1[i - 1] + res1
                res2 = self.__str2[j - 1] + res2
                i -= 1
                j -= 1
            elif this == left + self.__sc_gap:
                res1 = '_' + res1
                res2 = self.__str2[j - 1] + res2
                j -= 1
            else:
                res1 = self.__str1[i - 1] + res1
                res2 = '_' + res2
                i -= 1
        return res1, res2
