#Merge sort

def mergeSort(lst):
    if len(lst)>1:
        mid=len(lst)//2
        left=lst[:mid]
        right=lst[mid:]
        mergeSort(left)
        mergeSort(right)
        
        # Two iterators for the two halves
        i=0
        j=0
        
        # Iterator for the main list
        a=0
        
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                lst[a]=left[i]
                # Move the iterator forward
                i+=1
            else:
                lst[a]=right[j]
                j+=1
            # Move to the next value
            a+=1

        # For all the remaining values
        while i<len(left):
            lst[a]=left[i]
            i+=1
            a+=1

        while j<len(right):
            lst[a]=right[j]
            j+=1
            a+=1

lst=eval(input())
mergeSort(lst)
print(lst)
