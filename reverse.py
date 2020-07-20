#recursive function takes list and reverses it.
def revlist(s):
    #base case
    if len(s) == 0:
        return []
    else:
        #function calls itself, starting in the first position of the list, data at position at 0 is added on
        return revlist(s[1:]) + [s[0]] 
    
#test list to ensure function is working properly    
testList=[1,2,3,4]

print("The original list is {}.".format(testList))
#fuction called
print("The reverse of the list is {}.".format((revlist(testList))))
