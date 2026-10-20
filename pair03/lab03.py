#1
text = input("Введіть текст: ")

a = "аеєиіїоуюяaeiou"
b = 0
c = 0
d = 0
e = 0

for char in text:
    if char.isalpha():
        b += 1
    if char.isdigit():
        c += 1
    if char.isspace():
        d += 1
    if char.lower() in a:
        e += 1

f = len(text.split())

print("Символів:", len(text))
print("Літер:", b)
print("Цифр:", c)
print("Пробілів:", d)
print("Голосних:", e)
print("Слів:", f)
print()

#2

pib = input("Введіть ПІБ: ")
words = pib.strip().split()

if len(words) == 3:
    surname = words[0].capitalize()
    name = words[1][0].upper()
    p = words[2][0].upper()
    print(surname, name + "." + p + ".")
else:
    print("Помилка:потрібно ввести три слова.")
print()

#3

str1 = input("Перший рядок: ")
str2 = input("Другий рядок: ")

norm1 = str1.lower().replace(" ", "")
norm2 = str2.lower().replace(" ", "")

if sorted(norm1) == sorted(norm2):
    print("Рядки є анаграмами. (", str1, "та", str2, ")")
else:
    print("Рядки не є анаграмами. (", str1, "та", str2, ")")
print()

#4

sentence = input("Введіть речення:")
a = sentence.split()
if a:
    longest = a[0]
    shortest = a[0]
    
    for w in a:
        if len(w) > len(longest):
            longest = w
        if len(w) < len(shortest):
            shortest = w
    unique = []
    for w in a:
        w_lower = w.lower()
        if w_lower not in unique:
            unique.append(w_lower)

    print("Найдовші:", longest)
    print("Найкоротші:", shortest)
    print("Унікальних слів:", len(unique))
    old_word = input("Слово для заміни:")
    new_word = input("Нове слово:")
    result_sentence = sentence.replace(old_word, new_word)
    print("Після заміни:", result_sentence)
else:
    print("Речення порожнє")