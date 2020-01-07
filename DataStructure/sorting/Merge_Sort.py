def mergesort(mylist):
    length=len(mylist)
    if length>1:
        middle=length//2
        left_list=mylist[:middle]
        right_list=mylist[middle:]
        mergesort(left_list)
        mergesort(right_list)



        return merge(mylist,left_list,right_list)


def merge(mylist,left_list,right_list):

    i=0  # left list index
    j=0  # Right list index
    k=0  # Index of the Result list
    while i<len(left_list)and j<len(right_list):
        if left_list[i]<right_list[j]:
            mylist[k]=left_list[i]
            i=i+1
            k=k+1
        else:
            mylist[k]=right_list[j]
            j+=1
            k+=1
    while i<len(left_list):
        mylist[k] = left_list[i]
        i = i + 1
        k = k + 1
    while j<len(right_list):
        mylist[k] = right_list[j]
        j += 1
        k += 1
    return mylist




print(mergesort([23,12,55,232,45,66,2,54]))