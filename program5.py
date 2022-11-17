#Display numbers from a list using loop

#the number must be divisible by five
#If the number is greater than 150, then skip it and move to the next number
#If the number is greater than 500, then stop the loop

#Expected output: 75 150 145

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers :
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0 :
        print(i)
