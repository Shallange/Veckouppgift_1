## 2 Öva på loopar och listor
```python
answer = 0
for i in range(11):
    answer += i
print("Summan av talen 1 till 10 är: " + str(answer))
```
### 1b 
*Räkna ut summan av alla tal mellan 1 och 100. (inklusive 1 och 100, rätt svar ska bli 5050)*
```python
answer = 0
for i in range(101):
    answer += i
print("Summan av talen 1 till 10 är: " + str(answer))
```
### 1c 
*Skriv om 1b så att den använder en while-loop.*
```python
answer = 0
i = 0
while i <= 100:
    answer += i
    i += 1
print("Summan av talen 1 till 10 är: " + str(answer))
```

### 2 
*Räkna ut summan av alla elementen i listan*
```python
numbers = [1, -2, 3, -2, 4, -3] 
sum = 0
for i in range(len(numbers)):
    sum += numbers[i]

print(f"total sum {sum}")
```

### 3a 
*Skapa en lista med namnen på fyra filmer. Namnen ska vara strängar. Skriv ut hela listan 2med funktionen print.*

```python
movies = ["Harry potter","film2","film3","film4"]
for movie in movies:
    print(movie)
```

### 3b 
*Lägg till "Fellowship of the ring" sist i listan.*
```python
movies.append("Fellowship of the ring")
```
### 3c 
*Lägg till "The two towers" på första platsen i listan. (index noll)*
```python
movies.insert(0,"The two towers")
```
### 3d 
*Ta reda på vilken position (index) "Fellowship of the ring" har nu.*
```python
print(movies.index("Fellowship of the ring"))
```
### 3e 
*Ta bort en annan av filmerna. Har Fellowship-filmen ändrat index?*

```python
movies.pop(1)
print(movies)
print(movies.index("Fellowship of the ring"))
```
### 3f 
*Ta reda på hur lång listan är. (len)*
```python
print(len(movies))
```
### 3g 
*Vänd listan baklänges.*
```python
movies.reverse()
```

### 3h 
*Sortera listan stigande i bokstavsordning.*
```python
movies.sort()
```
