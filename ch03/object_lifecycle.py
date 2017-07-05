class CustomClass():

    def __new__(cls, arg): # It is called when only extends immutable objects (i.e. initializer)
        super
        print("Generating object.")

    def __init__(self, arg): # i.e. costructor
        self.elements = arg
        print("Initializing object.")

    def __del__(self): # Define statements(tasks) must be completed before destroy.
        print("Destroy object.")

    def get_elements(self):
        return self.elements

    def __repr__(self): # i.e. toString()
        return "This is Custom Class."

    def __str__(self): # c.f. __repr__()
        return "Called __str__()"

obj = CustomClass("str")
print(repr(obj))

del obj