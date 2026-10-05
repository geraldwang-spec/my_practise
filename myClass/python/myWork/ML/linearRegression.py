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

    def linear_practise(self):
        rng = np.random.RandomState(1)
        temp = rng.uniform(12, 38, 100)
        holiday =rng.randint(0, 2, 100)
        cups = 12 * temp + 80 * holiday - 50 + rng.randn(100) * 30   # 當天賣出杯數
        print(temp)
        print(cups)

        from sklearn.linear_model import LinearRegression
        model = LinearRegression(fit_intercept=true)
        model.fit(temp[:, np.newaxis], cups)

        tempfit = np.linspace(0, 10, 1000)
        cupsfix = model.predict(tempfit[:, np.newaxis])
        print("Model slope:", model.coef_[0])
        print("model intercept:", model.intercept_)



