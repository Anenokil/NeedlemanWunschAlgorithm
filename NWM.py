
class ScoreMatrix(object):
    def __init__(self, seq1: str, seq2: str, match=1, mismatch=-1, gap=-1):
        # score for match, mismatch and gap
        self.__sc_match = match
        self.__sc_mismatch = mismatch
        self.__sc_gap = gap
        # two sequences
        self.__seq1 = seq1
        self.__seq2 = seq2
        # score matrix and its size
        self.__h = len(seq1) + 1  # score matrix height
        self.__w = len(seq2) + 1  # score matrix width
        self.__mtrx = [[0 for _ in range(self.__w)] for _ in range(self.__h)]  # score matrix
        # construct score matrix
        self.__construct_matrix()

    def score(self) -> int:
        """ return score of the best alignment """
        return self.__mtrx[self.__h - 1][self.__w - 1]

    def __diff(self, a: chr, b: chr) -> int:
        """ return pairs score """
        if a == b:
            return self.__sc_match
        else:
            return self.__sc_mismatch

    def __construct_matrix(self):
        """ construct score matrix """
        for i in range(self.__h):
            self.__mtrx[i][0] = self.__sc_gap * i
        for j in range(self.__w):
            self.__mtrx[0][j] = self.__sc_gap * j
        for i in range(1, self.__h):
            for j in range(1, self.__w):
                self.__mtrx[i][j] = max(self.__mtrx[i - 1][j - 1] + self.__diff(self.__seq1[i - 1], self.__seq2[j - 1]),
                                        self.__mtrx[i - 1][j] + self.__sc_gap,
                                        self.__mtrx[i][j - 1] + self.__sc_gap)

    def print_matrix(self, cell_width: int):
        """ print score matrix """
        print(' ' * cell_width, end=' ')
        for j in range(self.__w):
            print(' ' * (cell_width - 1), (' ' + self.__seq2)[j], end=' ', sep='')
        print()

        for i in range(self.__h):
            print(' ' * (cell_width - 1), (' ' + self.__seq1)[i], end=' ', sep='')
            for j in range(self.__w):
                print(format(self.__mtrx[i][j], f'{cell_width}d'), end=' ')
            print()

    def best_alignment(self) -> (str, str):
        """ return the best alignment """
        res1 = ''
        res2 = ''
        i = self.__h - 1
        j = self.__w - 1
        while i != 0 or j != 0:
            this = self.__mtrx[i][j]
            diag = self.__mtrx[i - 1][j - 1]
            left = self.__mtrx[i][j - 1]
            if this == diag + self.__diff(self.__seq1[i - 1], self.__seq2[j - 1]):
                res1 = self.__seq1[i - 1] + res1
                res2 = self.__seq2[j - 1] + res2
                i -= 1
                j -= 1
            elif this == left + self.__sc_gap:
                res1 = '_' + res1
                res2 = self.__seq2[j - 1] + res2
                j -= 1
            else:
                res1 = self.__seq1[i - 1] + res1
                res2 = '_' + res2
                i -= 1
        return res1, res2
