# -*- coding: utf-8 -*-

b = (1,2,3)
c = ('a','b')
print(b+c)
# 튜플 값을 삭제할 수 없다. 값 추가도 안 됨.
# 인덱싱과 슬라이싱은 가능함. 보는 것이기 때문

# 딕셔너리 - 객체와 똑같음

a = {1 : 'su', 2 : 'hyo'}
print(a.keys()) # [1, 2]
print(a.values()) # ['su', 'hyo']
print(a.items()) # [(1, 'su'), (2, 'hyo')] 리스트 안에 튜플로 묶어서 리턴

# 반복문
for v in a.values():
    print(v)

for k, v in a.items():
    print("키는: " + str(k))
    print("value는: " + v)

print(a[1]) # 'su'
# print(a[4]) 해당 키 값이 없으므로 KeyError를 뱉음
print(a.get(3)) # 없는 키를 넣었을 때 get을 사용하면 Keyerror를 뱉는 것이 아니라 None 값을 리턴.
print(a.get(4,"없음")) # 해당 키 값이 없으면 default 값으로 '없음'을 리턴함.
print(4 in a) # False 불 값으로 리턴

a.clear() # 딕셔너리 안의 값들 다 비울 수 있음
print(a) # {}

# 집합
# 집합은 원소가 중복을 허용하지 않음. 또한 순서가 없다.
# set이 집합을 만드는 메소드/ set 안에 리스트 형태로 넣으면 대괄호 안에 들어가서 보여짐.
s1 = set([1,2,3])
s2 = {1,2,3}
print(s1) # set([1,2,3])
print(s2) # set([1,2,3])

# 리스트의 값 중 중복되는 값들을 제거하고 싶을 때
l = [1,2,3,4,2,3,1,5]
newList = list(set(l))
print(set(l)) # set([1, 2, 3, 4, 5])
print(newList) # [1, 2, 3, 4, 5]

s3 = set("Hello")
print(s3) # set(['H', 'e', 'l', 'o']) 중복 값이 없고, 순서 없음

s1 = set([1,4,3,2,3,5,3])
s2 = set([4,3,1,6,7,5])
print(s1 & s2) # set([1, 3, 4, 5]) 공통적으로 있는 값들을 집합 형태로 리턴됨.
print(s1.intersection(s2)) # 위의 &와 같은 것임.
# 합집합의 경우
print(s1 | s2) # set([1, 2, 3, 4, 5, 6, 7])
print(s1.union(s2)) # 합집합 같은 것.

# 차집합
print(s1 - s2) # set([2]) s1의 값에서 s2와 겹치는 값을 뺀 값
print(s2 - s1) # set([6, 7]) s2의 값에서 s1과 겹치는 값을 뺀 값
print(s2.difference(s1)) # 위의 값과 같은 것.

# 집합에 값 추가하기
s4 = set([1,2,3,4])
s4.add(7)
print(s4) # set([1, 2, 3, 4, 7])
s4.update([5,6,8])
print(s4) # set([1, 2, 3, 4, 5, 6, 7, 8]) 값을 여러 개 추가할 때
# 집합에 값 지우기
s4.remove(1)
print(s4) # set([2, 3, 4, 5, 6, 7, 8])

# 불 True/ False 로 써야 함.
a = True
print(type(a)) # <type 'bool'>

'''
문자형 "python" => True
빈 문자열 "" => False
리스트 [1,2,3] => True
빈 리스트 [] => False
빈 튜플 () => False
빈 딕셔너리 {} => False
숫자 1 => True
숫자 0 => False
None(아무것도 없는 값) => False
'''
a = '안녕'
if a:
    print(a) #안녕
b = ''
if b:
    print(b) # 안 나옴

a = [1,2,3,4]

while a:
    a.pop()
    print(a)
'''
[1, 2, 3]
[1, 2]
[1]
[]
'''
