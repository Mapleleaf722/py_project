i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(str(i) + '*' + str(j) + '=' + str(i * j), end=' ')
        j += 1
    print()
    i += 1
