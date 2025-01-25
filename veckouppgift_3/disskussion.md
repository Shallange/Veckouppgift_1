### Grupp 2 power ninjas

#### 1. 
*Vad skrivs ut?*

```python
limit = 15 
index = 5 

while index <= limit:
    print(index)
    index = index + 2
```
*Output*
```bash
5
7 
9 
11 
13 
15
```
#### 2. 
*Vad skrivs ut?*
- I for  i in range() så hanteras inkrementeringen redan och till skillnad från while loop så behövs inte ```i = i + 1```

```python
for i in range(10):
    if i == 5:
        print("")
    else:
        print(i)
   # i = i + 1 
```
#### 3.
0+1+2+3+4+5 = 15
- Summan blir 15
```python
counter = 0
for i in range(6):
    counter += i
print(counter)
```
*Output*
```bash 
15
```
#### 4.
- Värdet av x i slutet av while loopen kommer vara = 145 
*inget printas ut*
```python
x = 0 
y = 1

while y < 10:
    if y % 2 == 0:
        x -= y 
    else:
        x += y * y 
    y += 1
```

#### 5.
*Kan du göra om koden så att den skriver ut"time" i stället?*

- Här är det bara att flytta start värdet och slut värdet för slice från ``message[3:7]`` till ``message[4:8]``
```python
message = "its_time_to_get_coding"
print(message[4:8])
```
*output*
``time``
#### 6.
*Kan du flytta linjen ett steg åt höger?*
```python
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y + 1:   #<------  Löses genom att lägga till "+ 1"
            s += "#"
        else:
            s += "."
    print(s)
```
*output*
```
.#......
..#.....
...#....
....#...
.....#..
......#.
```
