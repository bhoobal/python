def shoppinglist(slist):    
    slist=slist.split(",")
    budget = 10000
    # convert to integer list
 #   intlist =[]
    count=0
    balance = budget
    for x in range(len(list(slist))):
#        intlist.append(int(slist[x]))
        if int(slist[x])>=budget:
            count += 1
            balance -= int(slist[x])
            break
        else:
            balance = balance - int(slist[x])
            if balance <=0:
                break
            count += 1          
    
    print("Balance is -->",balance)
    print("Count is -->",count)


if __name__=="__main__":
    # shopping=input()
    #shopping = "10000,100,30,30,100,50,100"
    shopping = "9850,100,30,30,100,50,100"
    #shopping = "9250,100,30,30,100,50,100"
    if not shopping:
        print("list is empty")        
    shoppinglist(shopping)