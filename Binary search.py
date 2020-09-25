#Binary search

def binsearch(lst,item,beg,end):
    if end>=beg:
        mid=(beg+end)//2
        if lst[mid]==item: #If element is present at the middle itself 
            return(mid)
        elif lst[mid]>item: #If element is smaller than mid, then it can only be present in left subarray
            return(binsearch(lst,item,beg,mid-1))
        #Else the element can only be present in right subarray 
        else:
            return(binsearch(lst,item,mid+1,end))
    else:
        return(-1)

lst=eval(input('Enter list'))
lst.sort()
print(lst)
item=int(input('Enter no to be searched'))
beg=0
end=len(lst)-1
print(binsearch(lst,item,beg,end))
