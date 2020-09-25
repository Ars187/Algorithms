#Selection sort

lst=eval(input('Enter list'))
for i in range(len(lst)): 
    x=i #
    for j in range(i+1,len(lst)): 
        if lst[x]>lst[j]: 
            x=j        
    lst[i],lst[x]=lst[x], lst[i] # Swap found minimum element with the first element         
print(lst)
