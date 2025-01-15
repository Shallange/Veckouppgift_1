#3 Sportresultat
#Funktion för att skriva ut resultatet
def print_score(tot_score,liv_score,winner, margin=0):
    if winner == "Oavgjort":
        result = f"""
        Matchen är över, nu ska vi räkna ut resultatet!
        Hur många mål gjorde Tottenham? {tot_score}
        Hur många mål gjorde Liverpool? {liv_score}
        Det blev oavgjort!
        """
    else:
        result = f"""
        Matchen är över, nu ska vi räkna ut resultatet!
        Hur många mål gjorde Tottenham? {tot_score}
        Hur många mål gjorde Liverpool? {liv_score}
        {winner} vann med {margin} mål!
        """
    return result

#Fråga om resultat
tottenham_score = int(input("Hur många mål gjorde Tottenham?: "))
liverpool_score = int(input("Hur många mål gjorde Liverpool?: "))


if tottenham_score > liverpool_score:
    margin = tottenham_score - liverpool_score
    print(print_score(tottenham_score,liverpool_score,"Tottenham", margin))
elif tottenham_score < liverpool_score:
    margin = liverpool_score - tottenham_score
    print(print_score(tottenham_score,liverpool_score,"Liverpool", margin))
else:
    print(print_score(tottenham_score,liverpool_score,"Oavgjort"))

