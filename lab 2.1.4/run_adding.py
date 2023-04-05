st = input()
tmp = []
i = 0
while st != '!':
    tmp.append(str(i) + ' ' + st)
    i += 1
    st = input()
print('\n'.join(tmp))
