from collections import deque

def solution(n, weak, dist):
    dist.sort(reverse=True)
    q = deque([weak])
    visited = set()
    visited.add(tuple(weak))
    for i in range(len(dist)):
        d = dist[i]
        for _ in range(len(q)):
            current = q.popleft()
            for p in current:
                l = p
                r = (p + d) % n
                if l < r:
                    temp = tuple(filter(lambda x: x < l or x > r, current))
                else:
                    temp = tuple(filter(lambda x: x < l and x > r, current))
                if len(temp) == 0:
                    return (i + 1)
                elif temp not in visited: # 방문한 거리 조합들이 q에 기입되고 visited에 기입됨
                    visited.add(temp)
                    q.append(list(temp))
    return -1

# 제일 긴 디스턴스로 이동 했을 때 방문 불가능한 weak 조합들을 q에 기입
# 그 다음 디스턴스 이동 가능한 사람으로 그 조합들을 방문하다 len(temp) = 0 즉, 모두 방문하면, i +1 값 즉 동원된 사람 수를 리턴