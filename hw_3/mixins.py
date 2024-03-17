import numpy as np


class DataSetterGetterMixin:
    @property
    def data(self):
        print("data getting side effect")
        return self.data_

    @data.setter
    def data(self, value):
        print("data setting side effect")
        self.data_ = value


class StrMixin:
    def __str__(self) -> str:
        return str(self.data)


class FileDumperMixin:
    def flush(self, path):
        with open(path, "w") as f:
            f.write(str(self))


# https://numpy.org/doc/stable/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html
# MyMatrix ensures that result of any operation is MyMatrix.
class MyMatrix(
        np.lib.mixins.NDArrayOperatorsMixin,
        DataSetterGetterMixin,
        StrMixin, FileDumperMixin):

    def __init__(self, data):
        self.data = np.asarray(data)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        # Omit logic with out kwarg in the name of simplicity.
        inputs = tuple(x.data if isinstance(x, MyMatrix) else x
                       for x in inputs)
        result = getattr(ufunc, method)(*inputs, **kwargs)
        if type(result) is tuple:
            # multiple return values
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            # no return value
            return None
        else:
            # one return value
            return type(self)(result)
