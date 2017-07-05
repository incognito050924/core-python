import sys

a = 37 # 값 37을 가지는 객체 생성
b = a # 37에 대한 참조 횟수 증가
c = []
c.append(b) # 37에 대한 참조 횟수 증가

# 객체의 참조 횟수 조회 - immutable 객체의 경우 메모리 절약을 위해 여러 곳에서 최대한 공유하고 있어 예상과 다른 값인 경우가 많음
print(sys.getrefcount(a))

del a # 37에 대한 참조 횟수 감소
b = 42 # 37에 대한 참조 횟수 감소
c[0] = 2 # 37에 대한 참조 횟수 감소


# 순환 의존성 - 두 객체가 서로의 참조 값을 가지기 때문에 참조 횟수가 0이 되지 못하여 gc가 일어나지 않아 메모리 누수 발생
# 인터프리터는 주기적으로 접근 불가능한 객체들의 순환참조를 감지하는 cycle detector를 구동함.
# gc module의 함수를 사용하여 garbage collection 과정을 직접 제어할 수 있음.
d1={}
d2={}
d1['d2'] = d2
d2['d1'] = d1

del d1
del d2