
class Calculator:
    def addNumbers(x, y):
        return x + y
    
    @staticmethod
    def multNumbers(x,y):
        return x*y

# create addNumbers static method
Calculat = staticmethod(Calculator.addNumbers)

print('Addition:', Calculat(15, 110))
print('Multiplication:', Calculator.multNumbers(15, 110))


