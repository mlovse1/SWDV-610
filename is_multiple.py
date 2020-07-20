#define function that will accept the parameters n and m to check to see if n is a factor of m
def is_multiple(n,m):
#if statement that uses the modulus operator to see if there is a remainder
    if m%n == 0:
        #if there is no remainder then it is a factor and it will equal 0, hence true
        return True
        #if there is a remainder, then it is not a factor and it will equal some other number, hence false
    else:
        return False
#test function
print(is_multiple(4,20))
print(is_multiple(10,3))

