"""
Rätta eventuella fel. Vad gör koden?
x = 100  # biljettpris
y = 200  # pengar på fickan
print("Det blir " + (y-x) "kronor över.")
z = 200 - 100 / 2      
print("hälften är: " + z)   


Fel:
- Print statement saknar kommatecken, har ett överflödigt plustecken
- För att göra strängkonkatingering krävs det att man typecastar int med str()
- Variabel z försöker strängkonkatineras utan att vara en sträng
- Prioritets regler i pyhton följer matte och är från vänster till höger så vill man subrahera först 
  kan man använda () för att prioritera det först
- Otydliga variabel namn och inte använda dom ändå
"""

biljettpris = 100  
fickpengar = 200  
balans = fickpengar - biljettpris # gör en ny variabel för uträkning, denna variabel används flera gånger 
print(f"Det blir {balans} kronor över.")
halva_balansen = balans / 2 
print(f"hälften av kvarstående balans är: {halva_balansen}")
