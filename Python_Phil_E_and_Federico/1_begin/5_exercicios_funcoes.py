"""Write a function that requires an indefinite number of arguments. What this function must do is return 
True if at any time the number zero has been entered twice consecutively.
For example:
(5,6,1,0,0,9,3,5) >>>
True
(6,0,5,1,0,3,0,1) >>>
False"""

def neighboring_zeros(*args):

    counter = 0

    for n in args:

        if counter + 1 == len(args):
            return False
        elif args[counter] == 0 and args[counter + 1] == 0:
            return True
        else:
            counter += 1

    return False


print(neighboring_zeros(0, 4, 0, 8, 1, 3, 9, 8, 0, 2, 0))