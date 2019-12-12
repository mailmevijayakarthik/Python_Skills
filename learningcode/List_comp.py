

Temps=[234,232,124,-345,532]
new_temp=[temp/10  if temp>0 else 0 for temp in Temps]
print(new_temp)

mylist=[89,34,2323,'a string','no data',500]

new_list=[item if isinstance(item,int) else 0 for item in mylist]
print(new_list)