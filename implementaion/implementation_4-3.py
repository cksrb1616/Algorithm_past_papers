po = input()
co_po = int(ord(po[0]))-int(ord('a'))+1
ro_po = int(po[1])

co_list = ['a','b','c','d','e','f','g','h']
ro_list = [1,2,3,4,5,6,7,8]

result = 0
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

for step in steps:
    next_row = ro_po +step[0]
    next_column  = co_po + step[1]
    if next_row>=1 and next_row<=8 and next_column>=1 and next_column<=8:
        result +=1

print(result)
print(int(ord('b')))