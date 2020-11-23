left =0
right = 9
while(left<= right):
    left += 2
    right -= 1
    if left>right:
        print('if' + str(left)+str(right))
    else:
        print('else'+ str(left)+str(right))