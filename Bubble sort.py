#Bubble Sort

lst=eval(input('Enter list'))
n=len(lst)
for i in range(n):
    for j in range(n-(i+1)):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print(lst)
    
