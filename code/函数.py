'''from functools import reduce
l = [1,2,3,4,5]
print(reduce(lambda x, y: x+y, l))
print(reduce(lambda x, y: x+y, l, 10))
l2 = [100, 20, 24, 50, 110]
new = list(filter(lambda x: x<50, l2))
print(new)'''


#装饰器
from functools import wraps
def hello(fn):
    @wraps(fn)
    def wrapper():
        print("hello, %s" % fn.__name__)
        fn()
        print("goodby, %s" % fn.__name__)
    return wrapper

@hello
def foo():
    print("I am foo")


foo()
print(foo.__name__)




