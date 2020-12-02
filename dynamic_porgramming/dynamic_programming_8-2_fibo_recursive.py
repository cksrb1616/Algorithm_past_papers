#Using memoization
#Top_down method : 작은 문제들이 모두 해결되었을 때 큰 문제가 해결됨
#Bottom_up mehtod : 작은 문제를 하나씩 해결해 나가면 먼저 해결된 문제를 활용해 다음 문제를 차례로 해결
#Dynamic -> Bottom Up


d = [0]*100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))