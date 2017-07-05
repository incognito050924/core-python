obj1 = complex(3, 4) # 복소수 객체
obj2 = [1, 2, 3] # 리스트 객체
obj3 = 3 +4j

# 객체 비교
def compare(a, b):
    if a is b:
        print('a와 b는 동일한 객체이다.')
    if a == b:
        print('a와 b는 동일한 값을 갖는다.')
    if type(a) is type(b):
        print('a와 b는 동일한 타입이다.')

# Type comparison
def typeCompare(o):
    if isinstance(o, type(o)): # isinstance 연산자는 상속관계를 인식하기 때문에 객체 타입 비교는 이 연산을 이용하는 것이 좋음.
        print('This object is Type ' + str(type(o)))
    if isinstance(o, list):
        print('This object is list')


print(id(obj1)) # 인터프리터의 구현에 따라 다르지만 보통 객체의 신원(메모리 상의 위치)를 나타냄.

typeCompare(obj1)
typeCompare(obj2)
compare(obj1, obj3)
