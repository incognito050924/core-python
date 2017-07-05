# NULL
print(type(None)) # falsey value in boolean expr

# Numeric <- immutable
print(type(3333333333333333333333333333333)) # int - signed
#print(type(long)) python 2.x
print(type(1.0)) # float - signed
print(type(1j)) # complex - signed
print(type(False)) # bool

# Sequencial
print(type('string')) # str <- immutable
print(type([])) #list
print(type(())) # tuple <- immutable
print(type(range(2))) # range (xrange(): python 2.x)

# Map (Hash Map)
print(type({})) #dict : immutable 객체라면 어떤 객체라도 키값으로 사용 가능함(str, int , tuple(Do not contain any mutable elements)...)

# Set
print(type(set([1, 2, 3, 3]))) # mutable set
print(type(frozenset([1, 2, 3, 4]))) # immutable set

# Callable Types
# User-defined functions(types.FunctionType), Built-in functions(types.BuiltinFunctionType),
# Instance methods(types.MethodType), Classes, type, object

#User-defined functions
def func(x, y):
    '''This is docstring.'''
    return x + y

def func2():
    return lambda x, y: x + y
bar = lambda x: x

print(func.__doc__)
print(func.__name__)
print(func.__dict__)
print(func.__code__)
print(func.__defaults__)
print(func.__globals__)
print(func.__closure__)

print(bar.__name__)

class Class(object): # 매개 변수 생략 가능 default = object
    # Class variables area
    var = 0
    __private = 0 # private variable (The identifier started __ (double underscore))

    def __init__(self, arg): # constructor
        self.__private = self.arg = arg # declare instance variable
        print("Constructor : generate object")

    def instance_method(self, arg):
        self.var = arg # instance variable var
        print("Instance method was called")
        print(self.var)
        print(self.__private)

    @classmethod
    def class_method(cls, arg = 0):
        if arg > 0:
            cls.var = arg
        print("Class method was called")
        print(cls.var)
        print(cls.__private)

    @staticmethod
    def static_method():
        print('Static method was called')

c1 = Class(2)
c2 = Class(3)
c1.instance_method(2)
c2.instance_method(3)
c1.class_method(1)
Class.class_method(0)
c2.class_method(2)
c1.class_method(0)

Class.static_method()

# Bound Method
c3 = Class(1)
bound_method = c3.instance_method
bound_method(2)
print(bound_method.__self__)
print(type(bound_method))

# Unbound Method
unbound_method = Class.instance_method
unbound_method(c3, 3)
print(type(unbound_method))

