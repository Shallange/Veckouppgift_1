#1c (svårare) Nu ska programmet svara i hela timmar och minuter.
distance = 470 #km
speed = int(input("Hur fort planerar du att köra? (km/h): "))

def distance_calc(speed, distance):
    time_total_min = (distance / speed) * 60 # totala antalet minuter 
    time_min = int(time_total_min % 60) #antal minuter som blir över(minuter under 60) typecastingen gör så att de visas i heltal
    time_hour = int(time_total_min // 60) # heltals division -> resulterar i heltal 

    return time_min, time_hour #returnerar antalet timmar och minuter 

time_min, time_hour = distance_calc(speed, distance) # lägger in dessa returnerade värden i varibler ordningen är den samma som ordningen i funktionen returer

print(f"Det kommer att ta dig {time_hour} timmar och {time_min} minuter att köra")