def makemypizza(size,*toppings):
    print('Make my pizza of '+ str(size)+ 'with the below Toppings :')
    for topping in toppings:
        print(topping)


makemypizza(16,'Tomato','cheese','chicken')
makemypizza(14,'cucumber','chili','Beef',"mushroom")
makemypizza(8,'cheese')
