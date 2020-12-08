a = [3, 1, 2]
k = 5

def solution(food_times, k):
    while k!=0:
        for i in range(len(food_times)):
            if food_times[i] == 0:
                continue
            food_times[i] -= 1
            k -= 1
    answer = [index for index, value in enumerate(food_times) if value > 0][0]+1
    return answer

solution(a,k)