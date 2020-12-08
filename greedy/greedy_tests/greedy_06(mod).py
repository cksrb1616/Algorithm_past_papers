import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1)) # similar to enumerate() but make a heapq of (value, index) and sort based on value
    sum_value = 0 # Time spent to eat
    previous = 0 # Time spent for previous food
    length = len(food_times) # Number of dish left

    while sum_value + ((q[0][0]-previous)*length) <=k:
        now = heapq.heappop(q)[0]
        sum_value += (now-previous) * length
        length -= 1
        previous = now
    result = sorted(q, key=lambda x: x[1])
    return result[(k-sum_value)%length][1]