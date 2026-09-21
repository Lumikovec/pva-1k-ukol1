import random

cislo = random.randint(1, 100)
print("Hádej číslo mezi 1 a 100.")

while True:
    guess = int(input("Zadej svůj tip:"))

    if guess < cislo: 
        print("Větší!")
    elif guess > cislo:
        print ("Měnší!")
    elif guess == cislo:
        print ("Správně!")
        break
    else: 
        print ("Chyba")