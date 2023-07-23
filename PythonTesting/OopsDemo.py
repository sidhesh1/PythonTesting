class Calculator:
    num = 100

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b

        print("I'm called automatically when object of the class is created")

    def getData():
        print("Currently inside method of the class")

    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(20, 30)
print(obj.summation())
