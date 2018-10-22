"""if then statements"""

# ask the user question
ans = input('Is three an odd or even number? ')

# make the characters in the ans lowercase for consistency
ans = ans.lower()

# set up the if then statement
if ans == 'even':

    # if the conditions above were met, complete this code
    print('that is incorrect')

# this is a caveat to the first if. if it is not true, then check to see if this is true
elif ans == 'odd':
    print("yes, three is an odd number")

# if none of the above statements are true, then complete this code
else:
    print('that is not an answer choice.')




# again, dont worry about this
def complicated_stuff():
    print("\n \n \n \n \n \n ")
    input("press enter to quit")
    pass

