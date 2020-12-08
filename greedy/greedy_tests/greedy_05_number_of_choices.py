# combination without duplication
# different weight should be picked up
# how many combinations would be?
# each ball has unique number

n, m = map(int,input().split())
weights = list(map(int,input().split()))

count = 0
for i in range(len(weights)):
    for j in weights[i+1:]:
        if weights[i] != j:
            count += 1
        else:
            pass
print(count)

