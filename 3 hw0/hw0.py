# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num): return [x for x in L if x%num != 0]


## Problem 2
def myLists(L): return [ [x for x in range(1,y+1)] for y in L]



## Problem 3
def myFunctionComposition(f, g): return {key:g[f[key]] for key in f}


## Problem 4
# Please only enter your numerical solution.

complex_addition_a = (5+3j)
complex_addition_b = 1j
complex_addition_c = (-1+0.001j)
complex_addition_d = (0.001+9j)


from GF2 import One

## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L): 
    summation = 0
    for x in L:
        summation +=x
    return summation
    
#print (mySum([1,2,3,4,5]))

## Problem 7
def myProduct(L): 
    mul = 1
    for x in L:
        mul *=x
    return mul

#print (myProduct([1,2,3,4,5]))

## Problem 8
def myMin(L): 
    less = L[0]
    for x in L:
        if x < less:
            less = x
        
    return less
#print (myMin([1,2,3,4,5]))

## Problem 9
def myConcat(L): 
    string = ''
    for x in L:
        string = string + x    
    return string
    
#print (myConcat(['he','ll','0']))


## Problem 10
def myUnion(L): 
    unionset = set()
    for x in L:
        unionset = unionset.union(x)
    return unionset    
#print (myUnion([{1,2,3},{3,4,5},{1,4,5}]))        