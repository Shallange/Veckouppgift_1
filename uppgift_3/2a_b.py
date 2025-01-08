#2a + b
def calculate_discount(cost,sale):
    discount = sale / 100 #convert percentage to decimal
    price_after_discount = discount * cost
    return price_after_discount


clothing = str(input("vad är det för typ av klädsel: "))
cost = int(input(f"Hur mycket kostar {clothing}? : "))
sale = int(input(f"Hur mycket procent är {clothing} nedsatt? (svara i heltal): "))


final_price = calculate_discount(cost,sale)

print(f"{clothing} kostar {final_price} kr med rean")
    
    