def linear_sum(S,n):

    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1)+S[n-1]
    
#S = [4,3,6,2,8,9,3,2,8,5,1,7,2,8,3,7]
S=[0,1,2,3]
n =4
print(linear_sum(S,n))