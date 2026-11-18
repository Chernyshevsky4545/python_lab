from datetime import date, datetime
import math
import random
import statistics
import tkinter as tk

# #9 (Функції власного модуля розміщуємо вище, перед їх викликом)
def square(number):
  return number**2


def is_even(number):
  return number % 2 == 0


def average(numbers):
  return sum(numbers) / len(numbers)


# 1
a = 6
b = 8
hypotenuse = math.sqrt(a**2 + b**2)
radius = 5
circle_area = math.pi * radius**2
print("Гіпотенуза:", hypotenuse)
print("Площа круга:", round(circle_area, 2))

# 2
c = 25
d = 6
print("Повних упаковок:", math.floor(c / d))
print("Упаковок потрібно:", math.ceil(c / d))

# 3
numbers = []
for i in range(10):
  numbers.append(random.randint(1, 100))
print(numbers)

# 4
students = ["Anna", "Ivan", "Olha", "Maksym"]
selected = random.choice(students)
print("Обрано:", selected)

# 5
questions = [1, 2, 3, 4, 5]
random.shuffle(questions)
print("Новий порядок:", questions)

# 6
grades_list = [10, 8, 12, 9, 11, 10]
print("Середнє:", statistics.mean(grades_list))
print("Медіана:", statistics.median(grades_list))

# 7
print("Дата:", date.today())
print("Дата і час:", datetime.now())

# 8
date1 = date(2026, 10, 1)
date2 = date(2026, 12, 31)
difference = date2 - date1
print("Днів:", difference.days)

# 10 
nums = [4, 8, 10, 12]
print(square(5))
print(is_even(8))
print(average(nums))

# 11
print(math.sqrt(100))
from math import sqrt  
print(sqrt(100))

# 14
grades = []
for i in range(20):
  grades.append(random.randint(1, 12))

print("Оцінки:", grades)
print("Min:", min(grades))
print("Max:", max(grades))
print("Середнє:", round(statistics.mean(grades), 2))
print("Медіана:", statistics.median(grades))

high = 0
for grade in grades:
  if grade >= 10:
    high += 1
print("Оцінок 10-12:", high)


# 15 
def generate_report():
  value = count_entry.get().strip()
  if not value.isdecimal():
    result.configure(text="Введіть ціле число від 1 до 100")
    return

  count = int(value)
  if count < 1 or count > 100:
    result.configure(text="Кількість має бути від 1 до 100")
    return

  g_list = []
  for i in range(count):
    g_list.append(random.randint(1, 12))

  avg = statistics.mean(g_list)
  med = statistics.median(g_list)

  text = "Оцінки: " + str(g_list)
  text += "\nСереднє: " + str(round(avg, 2))
  text += "\nМедіана: " + str(med)
  result.configure(text=text)


window = tk.Tk()
window.title("Генератор оцінок")
window.geometry("500x350")

tk.Label(window, text="Кількість оцінок (1-100):").pack(pady=5)
count_entry = tk.Entry(window)
count_entry.pack(pady=5)

tk.Button(window, text="Згенерувати", command=generate_report).pack(pady=10)
result = tk.Label(window, text="", wraplength=460, justify="left")
result.pack(pady=10)

window.mainloop()