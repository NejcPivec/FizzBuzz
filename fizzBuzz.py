
# narediš zanko čez 100 elementov 1- 100
for x  in range(1, 101):
    if x % 3 == 0 and x % 5 == 0: # najprej morš definerat ta pogoj, ker python začčne iz vrha in ga drugače spregleda
        print("FizzBuzz")
    elif x % 5 == 0:
        print("Fuzz")
    elif x % 3 == 0:
        print("Fizz")
    else:
        print (x) # če ni 3, 5 ali 15 samo zapiše število 