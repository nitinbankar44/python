'''Logic 
A prime number is a whole number greater than 1 whose only factors are 1 and itself.
A factor is a whole number that can be divided evenly into another number.
The first few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29.
Numbers that have more than two factors are called composite numbers.
'''


# Program to check if a number is prime or not

num = 1

# define a flag variable
flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")