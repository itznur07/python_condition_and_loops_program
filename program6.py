
#program 6: Count the total number of digits in a number

#For example, the number is 75869, so the output should be 5.

numbers = 75869

count = 0

while numbers != 0:
    numbers = numbers // 10
    count += 1
    print(count)