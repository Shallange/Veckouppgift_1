"""
Det är ca 470km mellan stockholm och göteborg. Skriv ett programm som räknar ut hur lång tid det tar att köra från
Stockholm till Göteborg. Du behlver fråga användaren hur fort man ska köra, i km/h

formeln för uträkning av tid är ->
time = distance ÷ speed

"""
distance = 470 #km
speed = int(input("Hur fort planerar du att köra? (km/h): "))

def distance_calc(speed, distance):
    time = distance / speed
    return time 

print(f"Det kommer att ta dig {distance_calc(speed, distance)} timmar")
