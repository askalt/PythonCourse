
def zero_data(n, m):
    return [[0] * m for _ in range(n)]


class Matrix:
    _cache = {}

    @staticmethod
    def clear_cache():
        Matrix._cache = {}

    def __init__(self, ma) -> None:
        self.n_ = len(ma)
        if self.n_ == 0:
            raise ValueError("matrix must have at least one row")
        row0 = ma[0]
        for row in ma:
            if len(row) != len(row0):
                raise ValueError("all rows must have equal size")
        self.m_ = len(row0)
        self.ma_ = ma

    def shape(self):
        return (self.n_, self.m_)

    def __add__(self, oth):
        if self.shape() != oth.shape():
            raise ValueError("matrices must have equal shape for add")
        n, m = self.shape()
        result_data = zero_data(n, m)
        for i in range(n):
            for j in range(m):
                result_data[i][j] = self.ma_[i][j] + oth.ma_[i][j]
        result = Matrix(result_data)
        return result

    def __mul__(self, oth):
        if self.shape() != oth.shape():
            raise ValueError("matrices must have equal shape for mul")

        n, m = self.shape()
        result_data = zero_data(n, m)
        for i in range(n):
            for j in range(m):
                result_data[i][j] = self.ma_[i][j] * oth.ma_[i][j]

        result = Matrix(result_data)
        return result

    def __matmul__(self, oth):
        n, m_ = self.shape()
        m__, k = oth.shape()
        if m_ != m__:
            raise ValueError("matrices shapes are incompatible for mul")

        hash_key = (hash(self), hash(oth))
        if cached := Matrix._cache.get(hash_key):
            return cached

        m = m_
        result_data = zero_data(n, k)
        for i in range(n):
            for j in range(k):
                for p in range(m):
                    result_data[i][j] += self.ma_[i][p] * oth.ma_[p][j]

        result = Matrix(result_data)
        Matrix._cache[hash_key] = result
        return result

    def __str__(self) -> str:
        return "\n".join(map(lambda row: " ".join(map(str, row)), self.ma_))

    def __eq__(self, oth):
        if not isinstance(self, Matrix):
            return False
        return self.ma_ == oth.ma_

    def __hash__(self) -> int:
        # Take xor of n, m and data.
        h = self.n_ ^ self.m_
        for row in self.ma_:
            for i in row:
                h ^= i
        return h
