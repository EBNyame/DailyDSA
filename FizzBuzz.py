number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31];

for num in number:
#so for the first two lines of code, you can see that we have to loop through if
#we have a number divisible by 3 and also divisible by 5 then we print fizzBuzz, 
# Dont you think it's a long way? Dont you think we can simplify it by finding a common factor for both 3 and 5? 
    
#........................................................................
    # if num % 3 == 0 and num % 5 == 0:
    #     print(f"{num} fizzBuzz")
#.......................................

#The common factor for both 3 and 5 is 15, so let's make some changes;
    if num % 15 == 0:
        print(f"{num} fizzBuzz")

    elif num % 3 == 0:
        print(f"{num} fizz")

    elif num % 5 == 0:
        print(f"{num} buzz")


# ............enjoy coding..........




#.........................testing...............................................