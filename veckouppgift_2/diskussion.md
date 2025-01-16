### 1- Diskutera i grupp
- Vad är syftet med koden?
- Testkör koden med några olika värden.
- Finns det några direkta fel i koden? (fel som gör att programmet kraschar)
- Finns det logiska fel? (programmet gör något annat än det är tänkt)
- Diskutera möjliga lösningar på felen ni hittat.
- Diskutera möjliga förbättringar på koden.


``` python
is_member = False
level1 = 100
level2 = 300
discount = 0

price = input("Välkommen, köp något dyrt: ")
price = float(price)

if price > level1:
    print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
    discount = discount + 10

if price >= level2:
    print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
    discount = discount + 25

final_price = price * (100 - discount) / 100
print("Efter rabatter blir priset.... " + final_price)

```

### 1: Syftet med koden: 
Syftet med koden är att beräkna en rabatt baserat på priset användaren betalar och om användaren är medlem. Rabatten delas upp i olika nivåer:
- **Nivå 1:** 10% rabatt för pris över 100 kr.
- **Nivå 2:** 25% rabatt för pris över 300 kr.

### Finns det några direkta fel i koden? (fel som gör att programmet kraschar)  
Ja, hittade följande direkta fel:

- **Felaktig konkatenering av sträng och float:**  
  I den ursprungliga koden användes konkatenering mellan en sträng och ett flyttal, vilket orsakade ett fel vid utskrift av `final_price`.

  **Ursprunglig kod:**  
  ```python
  print("Efter rabatter blir priset.... " + final_price)
  ```
**Lösning:** Använd `f-string` eller konvertera `final_price` till en sträng med `str()`:
  ```python
  print(f"Efter rabatter blir priset: {final_price}")
  ```

### 4: Logiska fel
#### 1. Båda rabattnivåerna appliceras
- Om priset är över 300 kr, tillämpas både nivå 1 och nivå 2, vilket ger felaktiga resultat.  
**Lösning:** Använd `if-elif-else` för att säkerställa att endast en rabattnivå används.


#### 2. Medlemskapet påverkar inte logiken i originalkoden
- Variabeln `is_member` används inte för att styra om rabatter kan tillämpas.  
**Lösning:** Lägg till logik som kontrollerar medlemskap innan rabatten beräknas.

#### 3. Ingen feedback för icke-medlemmar
- Om användaren inte är medlem, saknas information om varför ingen rabatt ges.  
**Lösning:** Lägg till tydligt meddelande som förklarar att rabatter endast gäller för medlemmar.

#### 4. Onödig komplexitet i rabattberäkning
- Rabatt läggs till med `discount = discount + 10`, vilket kan förenklas till `discount = 10`.  
**Lösning:** Gör koden enklare genom att direkt tilldela värden till variabeln.



----
### Möjliga förbättringar
``` python 
def calculate_discount(price, is_member):
    """
    Beräknar rabatten baserat på pris och om användaren är medlem.

    parametrar:
    - price(float):priset på varan
    - is_member (bool): ander om användaren är medlem

    Reuturnerar:
    - discount (int): rabatt i procent (0, 10 eller 25)
    """
    discount_level_1 = 100
    discount_level_2 = 300
    discount = 0

    if is_member:
        if price < discount_level_1:
            left_to_advance = discount_level_1 - price
            print(f"Du behöver {left_to_advance} kr till för att komma upp till nivå 1 rabatten")
        elif price > discount_level_1 and price < level_2:    
            print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
            discount = 10
        elif price >= discount_level_2:
            print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
            discount = 25
    else:
        print("Du är tyvärr inte medlem och kan inte ta del av medlemsrabatterna vid ditt köp")
        
    return discount

#default värde för medlemskap är False
is_member = False

price = input("Välkommen, köp något dyrt: ")
price = float(price)
#Fråga om användaren är medlem och konvertera svar till lowercase
is_member_input = input("Medlem? (ja/nej): ").lower()

#Om input är ja då ändras is_member till True
if is_member_input == "ja":
    is_member = True

discount = calculate_discount(price, is_member)

#Om rabatt finns, beräkna och skriv ut slutpriset
if discount > 0:
    final_price = price * (100 - discount) / 100
    print(f"Efter rabatter blir priset: {final_price}")
else:
    #Om det inte en rabatt tillämpades, skriv att priset är oförändrad
    print(f"Priset är fortfarande: {price} (ingen rabatt tillämpades) ")
```