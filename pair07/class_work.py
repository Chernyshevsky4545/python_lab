# Приклад 1
import numbers


with open("hello.txt", "w", encoding="utf-8") as file:
    file.write("Привіт, Python!\n")

# Приклад 2
with open("log.txt", "w", encoding="utf-8") as file:
    file.write("Перший запуск\n")

with open("log.txt", "a", encoding="utf-8") as file:
    file.write("Новий запис\n")

# Приклад 3
with open("hello.txt", "r", encoding="utf-8") as file:
    text = file.read()
    print(text)

# Приклад 4
with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()
    print(text)
    print("Символів:", len(text))

# Приклад 5
with open("text.txt", "r", encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        print(f"{number}: {line.strip()}")

# Приклад 6
with open("text.txt", "r", encoding="utf-8") as file:
    for line in file:
        clean_line = line.strip()
        print(clean_line)

# Приклад 7
numbers = []
with open("numbers.txt", "r", encoding="utf-8") as file:
    for line in file:
        numbers.append(int(line.strip()))
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))

# Приклад 8
with open("students.txt", "r", encoding="utf-8") as file:
    for line in file:
        if line.strip():
            name, score = line.strip().split(";")
            print(name.strip(), int(score.strip()))

# Приклад 9
sample_line = "Anna; Python; 11"
name, subject, grade = sample_line.split(";")
print("Учень:", name.strip())
print("Предмет:", subject.strip())
print("Оцінка:", int(grade.strip()))

# Приклад 10
selected = []
with open("students.txt", "r", encoding="utf-8") as file:
    for line in file:
        if line.strip():
            name, score = line.strip().split(";")
            score_val = int(score.strip())
            if score_val > 80:
                selected.append([name.strip(), score_val])
print("Відібрані (>80):", selected)

# Приклад 11
students_demo = [
    ["Anna", 91],
    ["Ivan", 84],
    ["Olha", 97],
]
students_demo.sort(key=lambda student: student[1], reverse=True)
for student in students_demo:
    print(student[0], student[1])

# Приклад 12
sorted_demo = [
    ["Olha", 97],
    ["Anna", 91],
    ["Ivan", 84],
]
with open("result_demo.txt", "w", encoding="utf-8") as file:
    for name, score in sorted_demo:
        print(f"{name}; {score}", file=file)
print("Звіт result_demo.txt створено.")