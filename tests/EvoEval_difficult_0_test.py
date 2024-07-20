
import numpy as np
from numpy import nan, inf # for some outputs.
import sys

sys.set_int_max_str_digits(0)

from enum import IntEnum, auto

def is_floats(x) -> bool:
    # check if it is float; List[float]; Tuple[float]
    # TODO: search for any close floats? (other data structures)
    if isinstance(x, float):
        return True
    if isinstance(x, (list, tuple)):
        return all(isinstance(i, float) for i in x)
    if isinstance(x, np.ndarray):
        return x.dtype == np.float64 or x.dtype == np.float32
    return False


class DataType(IntEnum):
    Float = auto()
    Bool = auto()
    Int = auto()
    Str = auto()
    Null = auto()
    Tuple = auto()
    List = auto()
    Dict = auto()
    Set = auto()
    Type = auto()
    Unknown = auto()


def get_type(x):
    if x is None:
        return DataType.Null
    elif isinstance(x, bool):
        return DataType.Bool
    elif isinstance(x, int):
        return DataType.Int
    elif isinstance(x, str):
        return DataType.Str
    elif is_floats(x):
        return DataType.Float
    elif isinstance(x, tuple):
        return DataType.Tuple
    elif isinstance(x, list):
        return DataType.List
    elif isinstance(x, dict):
        return DataType.Dict
    elif isinstance(x, set):
        return DataType.Set
    elif isinstance(x, type):
        return DataType.Type
    else:
        return DataType.Unknown


def is_equal(x, y) -> tuple[bool, str]:
    x_type, y_type = get_type(x), get_type(y)
    if x_type != y_type:
        return False, "Type mismatch: {} vs {}".format(str(x_type), str(y_type))

    if x_type in [DataType.Int, DataType.Bool, DataType.Null, DataType.Str, DataType.Set, DataType.Type]:
        if x == y:
            return True, None
        try:
            error_msg = "INT/BOOL/NULL/ Value mismatch: {} vs {}".format(repr(x)[:300], repr(y)[:300])
        except:
            error_msg = "Value mismatch: too large for display"
        return False, error_msg
    elif x_type == DataType.Float:
        if np.allclose(x, y, equal_nan=True, atol=1e-6): # guard against nan
            return True, None
        else:
            return False, "FLOAT Value mismatch: {} vs {}".format(x, y)
    elif x_type in [DataType.List, DataType.Tuple]:
        if len(x) != len(y):
            return False, "Length mismatch: {} vs {}".format(len(x), len(y))
        for i in range(len(x)):
            equal, msg = is_equal(x[i], y[i])
            if not equal:
                return False, msg
        return True, None
    elif x_type == DataType.Dict:
        if len(x) != len(y):
            return False, "Length mismatch: {} vs {}".format(len(x), len(y))
        for k, v in x.items():
            if k not in y:
                return False, "DICT Value mismatch: key {} in {} but not in {}".format(k, x, y)
            equal, msg = is_equal(v, y[k])
            if not equal:
                return False, msg
        return True, None
    else:
        try:
            if x == y:  # e.g., object comparison
                return True, None
            else:
                return False, "ELSE Value mismatch: {} vs {}".format(x, y)
        except:
            return False, "Unsupported type: {} <-- {}".format(x_type, type(x))

def check(candidate):
    inputs = [eval(f"[{i}]") for i in ['[(1.0, 2.0), (2.0, 3.0), (3.0, 4.0)], 0.5', '[(1.0, 2.8), (2.9, 3.0), (4.0, 5.0), (2.0, 2.1)], 0.3', '[(1.0, 2.0), (2.0, 3.0), (3.0, 4.0)], 1.0', '[(1.0, 2.0), (3.0, 4.0), (2.0, 3.0)], 0.5', '[(1.0, 2.8), (2.9, 3.0), (1.0, 1.2)], 0.2', '[(0.0, 0.0), (0.0, 0.0)], 0.0', '[(-1.0, -0.9), (-1.0, -0.8), (-1.0, -0.7)], 0.2', '[(1.0, 2.0)], 0.5', '[(1.0, 2.8), (2.1, 2.9), (2.0, 2.7), (2.1, 2.8)], 0.001', '[(1.0, 2.0), (1.0 + 1e-9, 2.0 + 1e-9)], 1e-10', '[(1.0, 2.0), (2.0, 1.0), (3.0, 4.0), (4.0, 3.0)], 1.0', '[(1.0, 1.0), (1.1, 1.1), (1.2, 1.2)], 0.15', '[(5.0, 5.0), (10.0, 10.0), (15.0, 15.0)], 5.1', '[(-1.0, -2.0), (-3.0, -4.0), (-5.0, -6.0)], 2.0', '[(1.0, 2.0), (1.0001, 2.0001)], 0.00001', '[(0.99999, 0.99999), (1.0, 1.0), (1.00001, 1.00001)], 0.00002', '[(1.0, 1000000.0), (2.0, 1000001.0), (3.0, 1000002.0)], 0.5', '[(1.0, 2.0)], 0.5', '[(1.5, 2.7), (2.4, 3.1), (3.2, 4.5), (4.6, 5.8), (5.9, 7.0)], 0.2', '[(0.1, 0.2), (0.2, 0.4), (0.3, 0.5), (0.4, 0.6), (0.5, 0.7)], 0.1', '[(10.0, 20.0), (20.0, 30.0), (30.0, 40.0), (40.0, 50.0), (50.0, 60.0)], 10.0', '[(1.23, 2.34), (3.45, 4.56), (5.67, 6.78), (7.89, 8.90)], 2.22', '[(100.1, 200.2), (300.3, 400.4), (500.5, 600.6), (700.7, 800.8), (900.9, 1000.0)], 200.2', '[(0.01, 0.02), (0.03, 0.04), (0.05, 0.06), (0.07, 0.08), (0.09, 0.10)], 0.02', '[(1.11, 2.22), (3.33, 4.44), (5.55, 6.66), (7.77, 8.88), (9.99, 10.10)], 2.22', '[(0.001, 0.002), (0.003, 0.004), (0.005, 0.006), (0.007, 0.008), (0.009, 0.010)], 0.002']]
    outputs = [False, False, False, False, False, False, True, False, False, False, False, True, True, False, False, True, False, False, False, True, False, True, True, False, True, False]
    for i, (inp, exp) in enumerate(zip(inputs, outputs)):
        exact_match, _ = is_equal(candidate(*inp), exp)
        assert exact_match
    
