from statistics import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np

class ml_example:

    def __init__(self) -> None:
        pass

    def linear_example(self):
        rng = np.random.RandomState(1)
        x = 10 * rng.rand(50)
        print(x)
        y = 3 * x-5+rng.randn(50)
        print(y)
        
        from sklearn.linear_model import LinearRegression
        model = LinearRegression(fit_intercept=True)
        
        model.fit(x[:, np.newaxis], y)
        
        xfit = np.linspace(0, 10, 1000)
        yfit = model.predict(xfit[:, np.newaxis])
        
        plt.scatter(x, y)
        plt.plot(xfit, yfit)
        print("Model slope:", model.coef_[0])
        print("model intercept:", model.intercept_)
        plt.show()


