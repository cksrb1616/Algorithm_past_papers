n=1260 #거스름돈
count = 0

coin_type = [500,100,50,10]

for coin in coin_type:
    count += n//coin
    n %= coin

print(count)

###########################
#큰수의문제
n, m, k = map(int, input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]
maxsum = 0

while True:
    for i in range(k):
        if m == 0:
            break
        maxsum += first
        m -= 1
    if m == 0:
        break
    maxsum += second
    m -= 15
print(maxsum)

#################################

count = int(m/(k+1))*k
count += m%(k+1)

result = 0
result += (count)*first
result += (m-count)*second
print(result, count)

