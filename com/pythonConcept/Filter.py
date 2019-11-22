from functools import reduce

nums=[2,5,6,7,9,10,12,8,11]


######## Using Filter()

evens=list(filter(lambda n:n%2==0,nums))
odds=list(filter(lambda n:n%2!=0,nums))


print("Even numbers :",evens)
print("Odd numbers :",odds)


######## Using Map()

doubletheeven=list(map(lambda n:n*2,evens))

print("Double the Even numbers :",doubletheeven)

######### Using reduce()

#Note : reduce will not be available in default . We need to import it separately

SumTotal=reduce(lambda a,b:a+b,doubletheeven)

print("Total sum of all Doubled Even numbers are ", SumTotal)