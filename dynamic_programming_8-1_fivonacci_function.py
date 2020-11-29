#Optimal Substructure : One big question can be divided into small questions and colleition of small answers can be a
# big one
#Overlappint Subproblem : repeatitive same samll questions are waiting to be solved.

def fibo(x):
    if x ==1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))