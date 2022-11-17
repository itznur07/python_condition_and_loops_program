
#Program 3: Calculate the sum of all numbers from 1 to a given number

# Expected Output:
# User Enter a Number 10 
# Sum is = 55

#For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

numbers = int(input('Enter number:  ')) # Take a number from user
s = 0 #Declear a variable

                                                       
for number in range(1, numbers + 1, 1) :
    s = s + number
print('\n')
print(f'You Enter: {numbers}')
print(f'sum is: {s}')
    
