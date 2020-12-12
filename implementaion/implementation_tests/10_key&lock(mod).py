# still not perfect

def rotate_a_mtrix(a):
    n = len(a) # 행 갯수
    m = len(a[0]) # 열 갯수
    result =[[0]*n for _ in range(m)] # 결과값 저장용 리스트
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
        return result
def check(new_lcok):
    lock_length = len(new_lcok)//3
    for i in range(lock_length,lock_length*2):
        for j in range(lock_length,lock_length*2):
            if new_lcok[i][j] != 1:
                return False
    return True

def solution(key,lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0]*(n*3) for _ in range(n*3)]

    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    for rotation in range(4):
        key = rotate_a_mtrix(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False