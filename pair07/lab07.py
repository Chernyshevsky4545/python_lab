#1
with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()

lines = text.splitlines()
words = text.split()

longest_num = 0
longest_len = 0
longest_line = ""

for i in range(len(lines)):
    line = lines[i]
    if len(line) > longest_len:
        longest_len = len(line)
        longest_num = i + 1
        longest_line = line

print("Рядків:", len(lines))
print("Слів:", len(words))
print("Символів:", len(text))
print(f"Найдовший рядок: №{longest_num}, символів: {longest_len}")
print("Текст:", longest_line)

#2
fragment = input("Введіть фрагмент: ").strip().lower()
found = False

for i in range(len(lines)):
    if fragment != "" and fragment in lines[i].lower():
        print(f"{i + 1}: {lines[i]}")
        found = True

if not found:
    print("Збігів не знайдено.")


#3
good_students = []

with open("students.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if line == "":
            continue
        name, score_text = line.split(";")
        score = int(score_text.strip())
        if score > 80:
            good_students.append([name.strip(), score])
for i in range(len(good_students)):
    for j in range(i + 1, len(good_students)):
        if good_students[j][1] > good_students[i][1]:
            good_students[i], good_students[j] = good_students[j], good_students[i]

with open("result.txt", "w", encoding="utf-8") as file:
    for name, score in good_students:
        file.write(f"{name};{score}\n")
        
#4
def get_grades(filename):
    q = {}
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(";")
            if len(parts) != 3:
                continue
            name = parts[0].strip()
            grade = int(parts[2].strip())
            if name not in q:
                q[name] = []
            q[name].append(grade)
    return q


def make_report(q, out_file):
    a = []
    for name in q:
        grades = q[name]
        b = sum(grades) / len(grades)
        a.append([name, len(grades), b])
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[j][2] > a[i][2]:
                a[i], a[j] = a[j], a[i]

    with open(out_file, "w", encoding="utf-8") as file:
        if len(a) == 0:
            file.write("Немає даних для звіту.\n")
            return

        for name, count, b in a:
            file.write(f"{name} - оцінок: {count}\n")
            file.write(f"середній: {b:.2f}\n")

        best_b = a[0][2]
        best_names = []
        for name, count, avg in a:
            if abs(avg - best_b) < 1e-9:
                best_names.append(name)

        file.write(f"Найкращий результат: {' та '.join(best_names)} {best_b:.2f}\n")
grades_dict = get_grades("grades.csv")
make_report(grades_dict, "report.txt")