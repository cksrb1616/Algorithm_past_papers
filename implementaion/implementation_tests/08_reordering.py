n = input()

word = []
number = []

for i in range(len(n)):
    if n[i].isalpha():
        word.append(n[i])
    else:
        number.append(n[i])

word.sort()
sumnumber = 0

result = ''
for i in word:
    result += i
for i in number:
    sumnumber += int(i)

print(result + str(sumnumber))
#############
# forgot about the possibility of no interger




