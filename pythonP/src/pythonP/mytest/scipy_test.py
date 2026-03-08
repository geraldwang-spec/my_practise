from typing import cast
from numpy.typing import NDArray
import numpy  as np
import scipy
from scipy import constants
from scipy.optimize import OptimizeResult, root

def system(vars: NDArray[np.float64])->NDArray[np.float64]:
    x:float = cast(float, vars[0])
    y:float = cast(float, vars[1])
    f1:float = x + 0.5 * (x - y)**3 -1
    f2:float = 0.5 * (y - x)**3 + y
    return np.array([f1, f2], dtype=np.float64)

def scipy_03()->None:
    res:OptimizeResult  = root(system, np.array([0,0], dtype=np.float64))
    sol:NDArray[np.float64] = cast(NDArray[np.float64], res.x)
    print(f"x and y result = {sol}")

def eqn(x: NDArray[np.float64])->NDArray[np.float64]:
    return x + np.cos(x)

def scipy_02()->None:
    myroot: OptimizeResult = root(eqn, np.array([0.0]))
    final_x = cast(NDArray[np.float64], myroot.x)
    print(f"myroot = {final_x}")

def scipy_01()->None:
    print(constants.liter)
    print(scipy.__version__)
    print(f"pi = {constants.pi}")
    print(f"list all units \n {dir(constants)}")

def scipy_example()->None:
    # scipy_01()
    # scipy_02()
    scipy_03()

