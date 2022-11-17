
#Write a program to print multiplication table of a given number

#Hint
#Formula =>  r = n*i

n = int(input('Enter number: '))

for i in range(1, 10 +1, 1):
    r = n * i
    print(f'{n} * {i} = {r}')