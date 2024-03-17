import numpy as np
from libmatrix import Matrix
import os

artifacts_dir = os.path.join(os.path.dirname(__file__), "artifacts", "3.1")

np.random.seed(0)
a = np.random.randint(0, 10, (10, 10))
b = np.random.randint(0, 10, (10, 10))

ma1 = Matrix(a)
ma2 = Matrix(b)

with open(os.path.join(artifacts_dir, "matrix+.txt"), "w") as f:
    f.write(str(ma1 + ma2))

with open(os.path.join(artifacts_dir, "matrix*.txt"), "w") as f:
    f.write(str(ma1 * ma2))

with open(os.path.join(artifacts_dir, "matrix@.txt"), "w") as f:
    f.write(str(ma1 @ ma2))
