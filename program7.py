
#Print the following pattern

n = 10
k = 10

for i in range(0, n + 1):
    for j in range(k - i, 0, -1):
        print(j, end=' ')
    print('')