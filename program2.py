
#Program 2: Print the following pattern using Nested loop

row = 10 

for i in range(1, row + 1, 1): # <-- range(start, stop, step)
    for j in range(1, i + 1 ):  # <- Child loop
        print(j, end=' ')
    print('') #empty line after each rowor Emtey


