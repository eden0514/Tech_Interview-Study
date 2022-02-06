# -*- coding: utf-8 -*-

# 변수
a = 1
# 메모리가 실제로 값을 저장하는 곳 메모리에 주소가 있음
# 변수에는 주소가 있어서 a라는 변수를 불러왔을 때 메모리에 이 값(여기서는 1)을 가져올 수 있는 것.
# 파이썬에서 사용하는 변수는 객체를 가리키는 것.
a = [1,2,3]
b = a # 값을 넘기는 것이 아니라 주소를 넘기므로 a의 값이 변하면 b의 값도 당연히 같이 변함
a[0] = 5
print(id(a)) # 4369101960 주소값이 같음
print(id(b)) # 4369101960
print(a is b) # 같은 주소인지 여부 확인 True 가 나옴

a = [4,5,6]
b = a[:]
print(a is b) # 깊은 복사가 됨(slice로) False

from copy import copy # copy라는 모듈을 가져와서 값을 복사해서 새로운 주소에 할당
a = ['c','o','p','y']
b = copy(a)
a[3] = 'a'
print(a) # ['c', 'o', 'p', 'a']
print(b) # ['c', 'o', 'p', 'y']
print(a is b) # False

# 변수 할당하는 방법
a = 1
a, b = ('hello', 'world')
(a, b) = 'hello', 'world'
[a, b] = ['aa','bb']
a = b = 'same' # 두 값 모두 same
c = 1
d = 2
c,d = d,c # swap 이렇게 사용
print(c) # 2
print(d) # 1
