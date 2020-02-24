year = int(input("Enter a year: "))

if year<1582:
   print("Not within the Gregorian calendar period")
elif year>1582:
    if (year%4)==0:
        if (year%100)==0:
            if(year%400)!=0:
             print("Common Year")
        if (year%100)==0:
           if(year%400)==0:
             print("Leap Year")
        if (year%100)!=0:
            print("Leap Year")
    else :
        print("Common Year")