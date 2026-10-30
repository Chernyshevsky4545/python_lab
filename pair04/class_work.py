# Приклад 1. Статистика списку оцінок
grades = [10, 8, 12, 9, 11]
print("--- Приклад 1 ---")
print("Min:", min(grades))
print("Max:", max(grades))
print("Сума:", sum(grades))
print("Середнє:", sum(grades) / len(grades))

# Приклад 2. Додавання, видалення та сортування
numbers = [5, 2, 9, 1]
numbers.append(7)
numbers.remove(2)
numbers.sort()
print("\n--- Приклад 2 ---")
print("Відсортований список:", numbers)

# Приклад 3. Фільтрація у новий список
numbers = [12, 3, 4, 7, 10, 5]
positive = []
for number in numbers:
    if number > 0:
        positive.append(number)
print("\n--- Приклад 3 ---")
print("Додатні:", positive)

# Приклад 4. Кортеж координат і розпакування
point = (15, -4)
x, y = point
print("\n--- Приклад 4 ---")
print("x:", x)
print("y:", y)

# Приклад 5. Видалення дублікатів через set
names = ["Ivan", "Anna", "Ivan", "Olha", "Anna"]
unique_names = set(names)
print("\n--- Приклад 5 ---")
print("Унікальні імена:", unique_names)

# Приклад 6. Спільні елементи двох множин
math = {"Ivan", "Anna", "Olha"}
python = {"Anna", "Maksym", "Ivan"}
print("\n--- Приклад 6 ---")
print("Спільні:", math & python)
print("Тільки math:", math - python)
print("Усі:", math | python)

# Приклад 7. Словник товарів
prices = {"bread": 35, "milk": 48}
prices["cheese"] = 120
prices["bread"] = 38
print("\n--- Приклад 7 ---")
print("Словник цін:", prices)

# Приклад 8. Перебір items()
print("\n--- Приклад 8 ---")
for product, price in prices.items():
    print(product, "-", price, "грн")

# Приклад 9. Учень - список оцінок
students = {
    "Anna": [10, 11, 12],
    "Ivan": [8, 9, 10]
}
print("\n--- Приклад 9 ---")
print("Оцінки Анни:", students["Anna"])

# Приклад 10. Середній бал кожного учня
print("\n--- Приклад 10 ---")
for name, grades_list in students.items():
    average = sum(grades_list) / len(grades_list)
    print(name, round(average, 2))

# Приклад 11. Пошук найкращого результату
students_scores = {
    "Anna": [10, 11, 12],
    "Ivan": [8, 9, 10],
    "Olha": [11, 12, 12]
}
best_name = ""
best_average = 0
for name, grades_list in students_scores.items():
    average = sum(grades_list) / len(grades_list)
    if average > best_average:
        best_average = average
        best_name = name
print("\n--- Приклад 11 ---")
print("Найкращий:", best_name, round(best_average, 2))

# Приклад 12. Вибір структури даних
grades_list = [10, 8, 12]  # list
point_tuple = (10, 20)     # tuple
subjects_set = {"Python", "HTML", "Python"}  # set
student_dict = {"name": "Ivan", "grade": 11}  # dict
print("\n--- Приклад 12 ---")
print(grades_list, point_tuple, subjects_set, student_dict)