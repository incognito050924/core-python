a1 = [1, 2, 3, 4]
b1 = a1
print(b1 is a1) # True
b1[2] = -100
b1.append(100)
print(a1) # a1과 b1이 동일한 객체를 참조하고 있기 때문

# shallow copy : 새로운 객체를 생성하지만 그 안은 원래 객체에 들어있던 참조로 채워짐.
a2 = [1, 2, [3, 4]]
b2 = list(a2)
print(b2 is a2) # False
b2.append(100) # b2만 변화
print(a2)
print(b2)
b2[2][0] = -100 # 원소의 변화는 양측 모두에 발생 : 원소는 공유됨.
print(a2)
print(b2)

# deep copy : 새로운 객체를 생성하고 원래 객체가 담고 있던 모든 객체를 재귀적으로 복사함.
import copy
a3 = [1, 2, [3, 4]]
b3 = copy.deepcopy(a3)
b3[2][0] = -100
print(a3)
print(b3)
