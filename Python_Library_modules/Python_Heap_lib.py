import heapq

# Python code to demonstrate working of
# heapify(), heappush() and heappop()

# importing "heapq" to implement heap queue
li=[5,23,2,55,100,124]
heapq.heapify(li)      # COnverted Array (li) to Heap

print(li)
print("Created heap is :",end="")
print(list(li))

############# ------------------------------------------------------

# Using heappush to insert element into heap

heapq.heappush(li,10)
print("Modified heap after pushing :",end="")
print(li)

############# ------------------------------------------------------
# using heappop() to pop smallest element
heapq.heappop(li)

print ("The popped and smallest element is : ",end="")
print(li)

############# ------------------------------------------------------
# Using heappoppush

heapq.heappushpop(li,200)
print ("The poppush adds one new element and removed the smallest is : ",end="")
print(li)

############# ------------------------------------------------------
# Using heapreplace() element is first popped, then element is pushed

heapq.heapreplace(li,1)
print ("The heapreplace : ",end="")
print(li)

############# ------------------------------------------------------
# Using nlargest(n,iteratable)
print("The 3 largest numbers in list are : ",end="")
print(heapq.nlargest(3,li))


############# ------------------------------------------------------
# Using nsmallest(n,iteratable)
print("The 3 smallest numbers in list are : ",end="")
print(heapq.nsmallest(3,li))