import sys
data = sys.stdin.readline().rstrip()
print(data[1])
####################
print(1)
print(2)
print(1, 2)
print(7, end=" ")
##################

list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]

result = list(map(lambda a, b: a+b, list1, list2))

print(result)
#############
itertools : #반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리, 순열과 조합
heapq: #Heap 기능을 제공하는 라이브러리. 우선순위 큐 기능을 구현하기 위해 사용
bisect: #이진탑색 (binary search) 기능을 제공하는 라이브러리
collections: #deque, counter 등 자료구조를 포함하고 있는 라이브러리
#####################
eval() ???

#############
#순열과 조합
from itertools import permutations
data ['a','b','c']
result = list(permutations(data,3))
print(result)

from itertools import combinations
data ['a','b','c']
result = list(combinations(data,2))
print(result)

from itertools import product
data ['a','b','c']
result = list(product(data,repeat=2)) #중복을 허용해서 뽑을
print(result)

from itertools import combinations_with_replacement
data ['a','b','c']
result = list(combinations_with_replacement(data,2))때 #중복을 허용해서 조합할 때
print(result)