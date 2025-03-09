import random

num = random.randint(1, 10)
adivinar = int(input("Adivina el numero del 1 al 10: "))
if num == adivinar:
    print("Has ganado")
else:   
    print("Has perdido, el numero era: ", num)
