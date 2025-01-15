#Gör så att programmet svarar i minuter istället

distance = 470 #km
speed = int(input("Hur fort planerar du att köra? (km/h): "))

def distance_calc(speed, distance):
    time = (distance / speed) * 60 
    return time 

print(f"Det kommer att ta dig {round(distance_calc(speed, distance),3)} minuter")
