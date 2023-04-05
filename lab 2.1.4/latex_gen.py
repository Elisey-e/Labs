#tmp = [[], [], [], [], [], [], []]
#for i in range(7):
#    st = input().split('&')
#    for j in range(1, 5):
#        tmp[i].append(st[j][1:st[j].rfind('\t')])
#for i in range(7):
#    print('\t'.join(tmp[i]))

st = input()
ma = 0
for i in range(1000):
    ma += float(st.replace(',', '.'))
    st = input()
tmp = []
ma /= 1000
while st != '!':
    st = float(st.replace(',', '.'))
    ma = ma * 0.999 + 0.001 * st
    tmp.append(ma)
    st = input()
for i in range(1000):
    tmp.append(ma)
print('\n'.join(map(lambda x: str(x).replace('.', ',')[:11], tmp)))