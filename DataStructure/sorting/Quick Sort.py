def quicksort(sequence):
    length=len(sequence)
    if length<=1:
        return sequence
    else:
        pivot=sequence.pop()

    # Choosing the last element as pivot
    greaterthan_pivot=[]
    smallerthan_pivot=[]
    for item in sequence:
        if item>pivot:
            greaterthan_pivot.append(item)
        else:
            smallerthan_pivot.append(item)
    return quicksort(smallerthan_pivot)+[pivot]+quicksort(greaterthan_pivot)


print(quicksort([-5,20,4,7,23,4,54,-100]))
