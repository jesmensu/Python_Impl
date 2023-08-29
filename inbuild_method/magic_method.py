class My_Integer:
    # def __init__(self, i):
    #     self.i = i
        
    def __new__(self):
        print("Object created")
    
    def __index__(self):
        return self.i
    
obj = My_Integer()
print(obj)