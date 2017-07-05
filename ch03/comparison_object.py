class Class1():
    def __hash__(self):
        return hash(self)

    def __lt__(self, other):
        return self < other

    def __le__(self, other):
        return self <= other

    def __gt__(self, other):
        return self > other

    def __ge__(self, other):
        return  self >= other

    def __eq__(self, other):
        return self == other

    def __ne__(self, other):
        return self != other

    @classmethod
    def __inst


class Class2():
    pass

a = "abcd"
b = "abcde"
print(hash(a))
print(hash(b))

print(bool(a))