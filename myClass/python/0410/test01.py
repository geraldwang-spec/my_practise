
def test02()->None:
    high = eval(input("請輸入身高(cm):")) / 100
    weight = eval(input("請輸入體重(kg): "))
    
    bmi = weight/(high ** 2)
    print(f"身高:{high} cm | 體重:{weight} kg | BMI: {bmi}")


def test01()->None:
    print("Gerald Wang")
    print("It is very good class")

    x:int = 0
    for i in range(11):
        x = x + i
        print("total = ", x)

if __name__ == "__main__":
    # test01()
    test02()
