import os
import numpy as np
from mixins import MyMatrix


artifacts_dir = os.path.join(os.path.dirname(__file__), "artifacts", "3.2")
np.random.seed(0)
a = np.random.randint(0, 10, (10, 10))
b = np.random.randint(0, 10, (10, 10))

ma1 = MyMatrix(a)
ma2 = MyMatrix(b)

(ma1 + ma2).flush(os.path.join(artifacts_dir, "matrix+.txt"))
(ma1 * ma2).flush(os.path.join(artifacts_dir, "matrix*.txt"))
(ma1 @ ma2).flush(os.path.join(artifacts_dir, "matrix@.txt"))
