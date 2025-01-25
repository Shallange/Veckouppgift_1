#5 Gissa talet
import random
secret = random.randint(1, 100)
number_of_guesses = 0

print("Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är?")

while True:
    try:
        user_guess = (int(input("Gissa nummret: ")))
        number_of_guesses += 1#För att hålla koll på antalet gissningar
        if user_guess < secret:
            print("Nej, det är för lågt!")
        elif user_guess > secret:
            print("Nej, det är för högt!")
        else:
            print(f"Det är rätt!! Du gjorde det på {number_of_guesses} gissningar.")
            break #När man gissar rätt och bara när man gissar rätt så avslutas while loopen

        if abs(user_guess - secret) <= 5 and user_guess!= secret:# om gissningen är +-5 hemliga numret, ska de visas
            print("Nu börjar det brännas!")
    except ValueError:
        print("Ange heltal, 1-100 försök igen:")


