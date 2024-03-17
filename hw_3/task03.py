from libmatrix import Matrix
import os

artifacts_dir = os.path.join(os.path.dirname(__file__), "artifacts", "3.3")


def write_artifact(name, value):
    with open(os.path.join(artifacts_dir, name+".txt"), "w") as f:
        f.write(value)


A_data = [[1, 2], [3, 4]]
C_data = [[3, 1], [4, 2]]
B_data = [[1, 0], [0, 1]]
D_data = [[1, 0], [0, 1]]

A = Matrix(A_data)
C = Matrix(C_data)
assert hash(A) == hash(C)
assert A != C

B = Matrix(B_data)
D = Matrix(D_data)

write_artifact("A", str(A))
write_artifact("B", str(B))
write_artifact("C", str(C))
write_artifact("D", str(D))

assert B == D
ab_correct = A @ B
write_artifact("AB", str(ab_correct))
print(ab_correct)  # prints correct.

cd_wrong = C @ D
print(cd_wrong)  # prints wrong.

Matrix.clear_cache()
cd_correct = C @ D
print(cd_correct)  # prints correct now.
write_artifact("CD", str(cd_correct))
write_artifact("hash", f"AB: {hash(ab_correct)}\nCD: {hash(cd_correct)}")
