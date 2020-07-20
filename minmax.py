#Give min and max of list using recursive function

def min_max(lst):
#if-elif-else statement based on length of list
    if len(lst) ==0:
        return 0
#if length is 1, then there is only one item in the list, and it is returned as both the min and the max
    elif len(lst) == 1:
        return [lst[0], lst[0]]   
#if length is greater than 1, then the else statment is activated:
    else:
        #midlst finds the middle point of the list for splitting the list and checking for the min and max
        midlst = len(lst) // 2
        #finds the min and max for the first half of the list of data
        half1 = min_max(lst[:midlst])
        #finds the min and max for the second half of the list of data
        half2 = min_max(lst[midlst:]) 
        # compare half1 and half2 to determine the min and max between the two sets
        if (half2[0] < half1[0]):
            half1[0] = half2[0]
        if (half2[1] > half1[1]):
            half1[1] = half2[1]
        return half1
        
data=[7,5,14,3,18,74,21]

minitem, maxitem = (min_max(data))

print("The minimum in the list is {}.".format(minitem))
print("The maximum in the list is {}.".format(maxitem))

