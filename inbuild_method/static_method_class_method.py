class MyClass:
    class_variable = 0


    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    def instance_class(self):
        return self.instance_variable

    @classmethod
    def class_method(cls, x):
        cls.class_variable += x


    @staticmethod
    def static_method(x):
        return x


obj = MyClass(5)
print(obj.class_variable)
MyClass.class_method(1)
obj.class_method(2)
print(MyClass.class_variable)  # Output: 3

print(obj.static_method(3))
print(MyClass.static_method(4))
obj1 = MyClass(6)
print(obj1.class_variable)