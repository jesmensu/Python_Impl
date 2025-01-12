
# unknown number of arguments
def mySum(*args):
    return sum(args)
 
# Driver code
print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))


# ===========================
def fun(a, b, c, d):
    print(a, b, c, d)

my_list = [1, 2, 3, 4]
 
# Unpacking list into four arguments
fun(*my_list)

# ================================
def fun1(a, b, c):
    print(a, b, c)

def fun2(*args):
    args = list(args)

    # Modifying args
    args[0] = 'Geeksforgeeks'
    args[1] = 'awesome'
 
    # UNPACKING args and calling fun1()
    fun1(*args)
 
# Driver code
fun2('Hello', 'beautiful', 'world!')

# ================================
def fun(**kwargs):
 
    # kwargs is a dict
    print(type(kwargs))
 
    # Printing dictionary items
    for key in kwargs:
        print("%s = %s" % (key, kwargs[key]))
 
# Driver code
fun(name="geeks", ID="101", language="Python")


# ===============================================
# dictionary items using **
def fun(a, b, c):
    print(a, b, c)
 
# A call with unpacking of dictionary
d = {'a':2, 'b':4, 'c':10}
fun(**d)