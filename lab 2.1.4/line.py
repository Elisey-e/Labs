st = input()
tmp = []
while st != '!':
    tmp.append(st)
    st = input()
i = 0
st = input()
while st != '!':
    tmp[i] = tmp[i] + ' ' + st
    i += 1
    st = input()
for i in range(0, len(tmp), 2):
    print(tmp[i])
