""" Learnings
multiple variable declaration and assignment """

def main():
   # n = input() # std input
    n = "23 1 -367" # string
    print(type(n)) # type of a object
    list2=list(map(int,list((str(n)).split()))) # 1. Split, convert to list, int type list    
    print(list2, "Type is --", type(list2))
    result = product(list2) # function with argument and return tuple
    pr, su, flag = result
    print("return from function--",result, pr, su, flag, "Difference--",pr-su)

def product(numlist):
    index = 0
    j, sum = None, None # multiple variable assignment
    for i in numlist:  # list iteration
        if index == 0:
            j, sum = i, i
            index +=1
            #print("first--",j,"Index --", index)
        else:
            j = j * i
            sum = sum + i
            index +=1
        print(i, "Index--", index)
    print("Product--", j, "Sum is--", sum)
    return j, sum, bool(j-sum > 0) # return bool 

# Main function
if __name__== '__main__':
    main()
