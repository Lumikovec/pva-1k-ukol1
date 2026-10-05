import random

while True:
    cislo = random.randint(1, 100)
    print("Hádej číslo mezi 1 a 100.")

    count = 0

    while True:
        try:
            guess = int(input("Zadej svůj tip:"))
        except ValueError:
            print("Toto není platné číslo!")
            continue

        if guess < 1 or guess > 100:
            print("Číslo mimo rozsah!")
            continue

        count = count + 1
        print("Pokusy: " + str(count))

        if guess < cislo: 
            print("Větší!")
        elif guess > cislo:
            print ("Měnší!")
        elif guess == cislo:
            print ("Správně!")
            break
        else: 
            print("Chyba")

    again = input("Chceš hrát znovu? ano/ne: ")

    if again != "ano":
        print("Díky za hru, poslední kolo už zapínat nebudu, hra byla dobrá, zábava decent pro první tři hry, ale nevim jestli je úplně worth hrát 5 minut pro další hru. A ještě ten kód trošku vážně?")
        break