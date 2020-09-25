#Bubble Sort

lst=eval(input('Enter list')) #Reading unsorted list from user
n=len(lst)
for i in range(n): 
    for j in range(n-(i+1)):
        if lst[j]>lst[j+1]: #Checking if the number greater than the number succeeding it
            lst[j],lst[j+1]=lst[j+1],lst[j]
print(lst)
    
