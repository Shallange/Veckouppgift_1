"""3b (svårare) Ändra programmet så att det kan tala om vilket datum det är om 7 dagar.
"""

from datetime import date, timedelta

today = date.today() 
t1_one_week = timedelta(days=7) #ett time delta objekt som man kan specifera exempelvis timmar
future_date = today + t1_one_week # lägger på dessa 7 dagar på dagens datum 

print(f"the date in one week is: {future_date}")