#3 Kvittouträknaren
def split_the_bill(antal_personer,sum, tip=10):
    added_tip = sum * (tip/100) #How much tip is added to the total cost 
    total_kostnad = sum + added_tip #How much the total cost is including the tip 
    kostnad_per_person = total_kostnad / antal_personer # The total cost 
    return kostnad_per_person, total_kostnad

sum = 0

print("Välkommen till Kvittokompis! Avsluta genom att skriva: quit eller avsluta")
while True:
    user_input = input("Skriv in ett belopp:")
    if user_input.lower() == "quit" or user_input.lower() == "avsluta":
        break 
    try:
        belopp = float(user_input)
        sum += belopp 
    except ValueError:
        print("Det var inte ett giltigt tal, försök igen.")


antal_personer = int(input("Hur många är ni? "))
delad_nota,summa_med_tip = split_the_bill(antal_personer,sum)
print(f"Det blir {summa_med_tip} kr totalt, alltså {delad_nota} kr per person. Välkommen åter!")