array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1
    #O(N)
for i in range(len(count)): #O(K)
    for j in range(count[i]):#O(N)
        print(i, end =' ') #O(N+K)