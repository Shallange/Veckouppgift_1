#4 Temperaturomvandling
def convert_to_celsius(F):
    C = (F - 32) / 1.8
    return C

def convert_to_fahrenheit(C):
    F = 1.8 * C + 32
    return F

def what_to_wear_celc(temperature):
    if temperature <= 10:
        print("Det är ganska kallt och du borde ta på dig vinterkläder!") 
    elif temperature >= 20:
        print("Du borde packa badkläder, det är varmt ute")

def print_format_temp(temperature):
    return f"{temperature:.1f}"


temperature_type_input = input("Vill du ange graderna i Farhenheit eller celcius(f/c)?: ").lower()


if temperature_type_input == "f":
    fahrenheit_input = float(input("Skriv in en temperatur i farenheit: "))
    celcius = convert_to_celsius(fahrenheit_input)
    print(f"Det blir {print_format_temp(celcius)} grader celcius.")
    what_to_wear_celc(celcius)
elif temperature_type_input == "c":
    celcius_input = float(input("Skriv in en temperatur i celcius: "))
    fahrenheit = convert_to_fahrenheit(celcius_input)
    print(f"Det blir {print_format_temp(fahrenheit)} grader Fahrenheit.")
    what_to_wear_celc(celcius_input)
else:
    print("Ogiltigt val! Ange 'f' för Fahrenheit eller 'c' för Celsius.")