a='2,7,11,15'.split(',')
y = 9
for i in range(len(a)):
    if i < len(a)-1:
        if int(a[i]) + int(a[i+1]) == y:
            print('[',i,',',i+1,']')
        else:
            exit
