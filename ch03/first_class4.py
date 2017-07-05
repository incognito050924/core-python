# 파이썬의 모든 객체는 1급 객체이다.
# 식별자로 명명할 수 있는 모든 객체는 동일한 지위를 가지며, 데이터로서 취급될 수 있다.
import math

items = {
    'number': 42,
    'text': 'Hello'
}

items["func"] = abs # 함수 추가
items["mod"] = math # 모듈 추가
items["error"] = ValueError # 예외 타입 추가
nums = [1, 2, 3, 4]
items['append'] = nums.append # 다른 객체의 메서드 추가

print(items['func'](-45))
print(items['mod'].sqrt(4))
try:
    x = int("a lot")
except items['error'] as e:
    print("Could`t convert")
items["append"](100)
print(nums)
