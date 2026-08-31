'''In the previous lesson we have seen how error handling is usually implemented in Python. For this exercise, however, 
I'll need you to do it in a slightly different way so that it can be tested: you'll need to implement it INSIDE the function. 
In the form of a comment, you will see an example resolution. Keep in mind, however, that the preferred form is the one we've 
seen in class.
For the following division() function, implement an error handler:
In the event of a type error (TypeError), the message should be printed on the screen: "Arguments must be numbers"
If a division by zero is attempted (error of type ZeroDivisionError), the message displayed should be: "Second argument must
not be zero"
In the event that an error does not occur, it should limit itself to printing the result of the quotient (division) between the
two numbers given as an argument.'''
try:
    x = int(input("Put the first number: "))
    y = int(input("Put the second number: "))
    division = x / y
    print("Result:", division)
except ValueError:
    print("Arguments must be valid integers")
except ZeroDivisionError:
    print("Second argument must not be zero")





