# The infamous Fizz/Buzz Question
# Found here https://blog.codinghorror.com/why-cant-programmers-program/

#This programming question states the following:

# Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the number and 
# for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".

for value in range(0,101):
    if (value % 5 == 0 and value % 3 == 0):
        print('FizzBuzz')
    elif value % 3 == 0:
        print('Fizz')
    elif value % 5 == 0:
        print('Buzz')
# Only take out these '#' if you want it to print out the number for ones that
# are none of the above!
#    else:
#        print(value)
