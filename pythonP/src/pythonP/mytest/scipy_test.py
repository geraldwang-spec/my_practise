from typing import cast
from numpy.typing import NDArray
import numpy  as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import scipy
from scipy import constants
from scipy.optimize import OptimizeResult, root

def system(vars: NDArray[np.float64])->NDArray[np.float64]:
    x:float = cast(float, vars[0])
    y:float = cast(float, vars[1])
    f1:float = x + 0.5 * (x - y)**3 -1
    f2:float = 0.5 * (y - x)**3 + y
    return np.array([f1, f2], dtype=np.float64)

def plot_results(sol:NDArray[np.float64])->None:
    _, ax = cast(tuple[Figure, Axes], plt.subplots(figsize=(6, 6) ))

    theta:NDArray[np.float64] = np.linspace(0, 2*np.pi, 100)
    _ = ax.plot(2*np.cos(theta), 2*np.sin(theta), label='x^2 + y^2 = 4')

    line_x:NDArray[np.float64] = np.linspace(-2, 2, 10)
    _ = ax.plot(line_x, line_x, label='y = x', linestyle='--')
    root_x:float = cast(float, sol[0])
    root_y:float = cast(float, sol[1])

    _ = ax.plot(root_x, root_y, 'ro', markersize=10, label=f'Found Root: ({root_x:.2f}, {root_y:.2f})')

    _ = ax.set_aspect(aspect='equal') # 確保圓圓的
    _ = ax.legend()
    _ = ax.grid(visible=True)
    plt.show()

def scipy_04()->None:
    res:OptimizeResult  = root(system, np.array([1.0,1.0], dtype=np.float64))
    if res.success:
        final_solution:NDArray[np.float64] = cast(NDArray[np.float64], res.x)
        plot_results(final_solution)
    else:
        print(f"not found solution")


def scipy_03()->None:
    res:OptimizeResult  = root(system, np.array([0,0], dtype=np.float64))
    sol:NDArray[np.float64] = cast(NDArray[np.float64], res.x)
    print(f"x and y result = {sol}")

def eqn(x: NDArray[np.float64])->NDArray[np.float64]:
    return x + np.cos(x)

def scipy_02()->None:
    myroot:OptimizeResult = root(eqn, np.array([0.0]))
    final_x:NDArray[np.float64] = cast(NDArray[np.float64], myroot.x)
    print(f"myroot = {final_x}")

def scipy_01()->None:
    print(constants.liter)
    print(scipy.__version__)
    print(f"pi = {constants.pi}")
    print(f"list all units \n {dir(constants)}")

def scipy_example()->None:
    # scipy_01()
    # scipy_02()
    # scipy_03()
    scipy_04()

