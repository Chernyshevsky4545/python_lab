#1
numbers = [12, 3, 4, 14, -12, 5, 10, 16, -4]
positive = []
negative = []
a = []
b = []
for num in numbers:
    if num > 0:
        positive.append(num)
    if num < 0:
        negative.append(num)
    if num % 2 == 0:
        a.append(num)
    if num % 3 == 0:
        b.append(num)

min_val = min(numbers)
max_val = max(numbers)
total_sum = sum(numbers)
average_val = total_sum / len(numbers)
print("Початковий список:", numbers)
print("Додатні:", positive)
print("Від'ємні:", negative)
print("Парні:", a)
print("Кратні 3:", b)
print("Min:", min_val, "; Max:", max_val, "; Sum:", total_sum, "; Average:", round(average_val, 2))
print("-" * 50)
#2

group1 = {'Anna', 'Ivan', 'Olha'}
group2 = {'Ivan', 'Maksym', 'Olha'}
a = group1 & group2
only_group1 = group1 - group2
only_group2 = group2 - group1
un = group1 | group2
print("Group 1:", group1)
print("Group 2:", group2)
print("Спільні:", ", ".join(a))
print("Тільки group1:", ", ".join(only_group1))
print("Тільки group2:", ", ".join(only_group2))
print("Усі:", ", ".join(un))
print("-" * 50)

#3

catalog = {
    "bread": 35,
    "milk": 48,
    "cheese": 120,
    "tea": 75,
    "butter": 85
}
catalog["coffee"] = 110  
catalog["bread"] = 38    
search_item = "milk"
price = catalog.get(search_item, "Товар не знайдено")
print("Пошук товару", search_item, ":", price, "грн")
min_price, max_price = 40, 100
print("Ціновий діапазон:", min_price, "..", max_price, "грн")
for product, price_val in catalog.items():
    if min_price <= price_val <= max_price:
        print(product, "-", price_val, "грн")
print("-" * 50)

#4

group_info = ('10-IT', '2026/2027')
journal = {
    "Anna": [10, 11, 12, 9, 10],
    "Ivan": [8, 9, 10, 11, 9]
}
def add_student(name, grades_list):
    if len(grades_list) == 5 and all(1 <= g <= 12 for g in grades_list):
        journal[name] = grades_list
    else:
        print("Помилка додавання", name, ": оцінок має бути рівно 5 у діапазоні від 1 до 12.")
print(group_info[0], "-", group_info[1])
best_student = ""
g = -1

for name, grades_list in journal.items():
    avg = sum(grades_list) / len(grades_list)
    print(name, "-", round(avg, 1))
    if avg > g:
        g = avg
        best_student = name
print("Найкращий результат:", best_student, "-", round(g, 1))