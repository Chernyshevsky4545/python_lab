from datetime import date
import math
import random
import statistics

#1
radius = float(input("Введіть радіус круга:"))
a = float(input("Введіть перший катет:"))
b = float(input("Введіть другий катет:"))
c = int(input("Введіть кількість предметів:"))
d = int(input("Введіть місткість однієї упаковки: "))

e = math.pi * (radius**2)
f = math.sqrt(a**2 + b**2)
g = math.ceil(c / d)

print("Площа круга:", round(e, 2))
print("Гіпотенуза:", round(f, 2))
print("Потрібно упаковок:", g)

#2 
n = int(input("Введіть кількість оцінок: "))
if n > 0:
  grades = []
  for _ in range(n):
    grades.append(random.randint(1, 12))
  high_grades = 0
  for grade in grades:
    if grade >= 10:
      high_grades += 1
  print("Оцінки:", grades)
  print("Мін:", min(grades))
  print("Макс:", max(grades))
  print("Середнє:", round(statistics.mean(grades), 2))
  print("Медіана:", statistics.median(grades))
  print("Оцінок 10-12:", high_grades)
else:
  print("Помилка")

#3

year = int(input("Введіть рік: "))
month = int(input("Введіть місяць: "))
day = int(input("Введіть день: "))

a = date(year, month, day)
b = date.today()
difference = (a - b).days

if difference > 0:
  print(f"залишилося: {difference} днів")
elif difference < 0:
  print(f"Пройшло днів: {abs(difference)}")
else:
  print("Подія відбувається сьогодні!")