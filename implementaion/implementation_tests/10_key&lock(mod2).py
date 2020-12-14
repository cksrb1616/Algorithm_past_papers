def can_be_unlocked(key, lock, r, c, goal):

    start_row = max(0, r)
    end_row = min(r + len(key), len(lock))
    start_col = max(0, c)
    end_col = min(c + len(key[0]), len(lock))
    cnt = 0

    for row in range(start_row, end_row):
        for col in range(start_col, end_col):

            if lock[row][col] + key[row - r][col - c] != 1:
                return False

            if key[row-r][col-c]:
                cnt += 1

    return cnt == goal


def match_lock(key, lock, goal) -> bool:

    for row in range(-(len(key)-1), len(lock)):
        for col in range(-(len(key[0]) - 1), len(lock[0])):
            if can_be_unlocked(key, lock, row, col, goal):
                return True

    return False


def rotate_key(key) -> list:
    N = len(key)
    ret = [[0]*N for _ in range(N)]

    for row in range(N):
        for col in range(N):
            ret[col][N-1-row] = key[row][col]

    return ret


def solution(key, lock):
    goal = 0
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                goal += 1

    for i in range(4):
        if match_lock(key, lock, goal):
            return True
        key = rotate_key(key)

    return False
