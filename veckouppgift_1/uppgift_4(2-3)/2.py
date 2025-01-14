"""
2 Skriv ett program som räknar ut längden på hypotenusan i en rätvinklig triangel. Användaren behöver skriva in längden på de två kortare sidorna.
Tips 1: fråga en AI om formeln Pythagoras sats. Men var noga med att inte fråga efter kod som löser uppgiften!
Tips 2: räkna ut roten med math.sqrt().

Som testdata kan du använda triangeln med sidorna 3, 4 och 5:

hypotenusa² = katet² + katet²
a²+b²=c²
"""
import math as m

def calc_pythagoras(a ,b):
    c = m.sqrt((a**2) + (b**2)) #Roten ur summan av a² b² ger c   
    return c

print(calc_pythagoras(3,4)) 