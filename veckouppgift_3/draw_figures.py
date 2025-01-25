#Skriv kod så att den skriver ut figurerna a-j en i taget.

figures = ["a","b","c","d"]

for figure in figures:
    print("-------------------------------------------")
    if figure == "a":
        for y in range(1, 7):#6 st rader lodrätt
            s = ""
            for x in range(1, 9):#varje rad skriver 8 tecken
                if x == 1:
                    s += "#"
                elif y == 3:
                    s += "#"
                else:
                    s += "."
            print(s)
    if figure == "b":
        for y in range(1, 7):
            s = ""
            for x in range(1, 9):
                if x == y:
                    s += "#"
                elif y == 3:
                    s += "#"
                else:
                    s += "."
            print(s)
    if figure == "c":
        for y in range(1, 7):
            s = ""
            for x in range(1, 9):
                if x == 3 and x == 4 and x == 5:
                    s += "#"
                elif y == 3:
                    s += "#"
                else:
                    s += "."
            print(s)
    if figure == "d":
        for y in range(1, 7):
            s = ""
            for x in range(1, 9):
                if x == 3:
                    s += "#"
                elif y == 3:
                    s += "#"
                else:
                    s += "."
            print(s)

