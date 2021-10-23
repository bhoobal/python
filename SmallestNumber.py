def smallest(n):
    # check string
    #    print (type(n.split(",")))
    numtolist=n.split(",")
    #print(numtolist)
    integerlist=[]
    comparelist=[]
   
    #missingnumber = 0
    maximunnumber = 54879
    
    
    for i in range(len(numtolist)):
#        print (type(numtolist[i]))
        if (not(numtolist[i].isnumeric()) or int(numtolist[i]) > maximunnumber ):           
            print ("invalid")
            break
        else:
            integerlist.append(int(numtolist[i]))                    
            print("Sorted list -->", sorted(integerlist))
            print("Original list -->", integerlist)
            
            print("Maximum number", max(integerlist))   
            print("Smallest number", min(integerlist))   
            #create a list from smallest to biggest
            for i in range(1,max(integerlist)):
                comparelist.append(i)
            #print("to Compare", comparelist)
            #print("Length of integretlist",len(comparelist))
            #print("first item of integretlist",comparelist[1])

            missing = list(sorted(set(integerlist)-set(comparelist)))
            added = list(sorted(set(comparelist)-set(integerlist)))
            # print("Missing numbers",missing)
            #print("Maximum of missing numbers",min(missing))
            print("Minimum of missing numbers",min(added))
            print("this is on the smallest function value ",n)
def main(n):
    smallest(n)
    #print("This is in main function")

if __name__ == "__main__":    
    #n=input()
    #n="1,2,238,6,3,11,456,34,78,901,12,4,5,9,7,8,34567"
    n="1001,3,s,r,g,2,13,9,8,7"
    #n="s,r,t,y,u,u,u,7"
    #n="#,!,$"
    main(n)