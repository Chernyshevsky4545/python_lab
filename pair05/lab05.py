import math

#1
def area_circle(radius):
    return 3.14159 * radius ** 2

def area_rectangle(width, height):
    return width * height

def area_triangle(base, height):
    return 0.5 * base * height

def main():
    print("ЗАВДАННЯ 1: Площі фігур")
    print("Оберіть фігуру: 1 - круг, 2 - прямокутник, 3 - трикутник")
    choice = input("Ваш вибір (1/2/3): ")
    
    if choice == "1":
        r = float(input("Радіус: "))
        print(f"Площа круга: {area_circle(r)}")
    elif choice == "2":
        w = float(input("Ширина: "))
        h = float(input("Висота: "))
        print(f"Площа прямокутника: {area_rectangle(w, h)}")
    elif choice == "3":
        b = float(input("Основа: "))
        h = float(input("Висота: "))
        print(f"Площа трикутника: {area_triangle(b, h)}")
    else:
        print("Невірний вибір фігури.")

if __name__ == "__main__":
    main()


#2
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def digit_sum(n):
    return sum(int(digit) for digit in str(abs(n)))

def main():
    print("ЗАВДАННЯ 2: Аналіз числа")
    n = int(input("Введіть натуральне число N: "))
    prime_status = "так" if is_prime(n) else "ні"
    print(f"Просте число: {prime_status}")
    print(f"Дільники: {divisors(n)}")
    print(f"Сума цифр: {digit_sum(n)}")

if __name__ == "__main__":
    main()

#3
def average(grades):
    return sum(grades) / len(grades) if grades else 0

def minimum(grades):
    return min(grades) if grades else 0

def maximum(grades):
    return max(grades) if grades else 0

def count_above(grades, value):
    return sum(1 for grade in grades if grade > value)

def main():
    print("ЗАВДАННЯ 3: Звіт за списком оцінок")
    grades_list = [10, 8, 12, 9, 11]
    threshold = 9
    print(f"Оцінки: {grades_list}")
    print(f"Поріг: {threshold}")
    print(f"Середній бал: {average(grades_list)}")
    print(f"Мінімальна: {minimum(grades_list)}")
    print(f"Максимальна: {maximum(grades_list)}")
    print(f"Вище {threshold}: {count_above(grades_list, threshold)}")

if __name__ == "__main__":
    main()

#4

def check_length(password):
    return len(password) >= 8

def check_digit(password):
    return any(char.isdigit() for char in password)

def check_upper(password):
    return any(char.isupper() for char in password)

def check_lower(password):
    return any(char.islower() for char in password)

def check_special(password):
    return any(not char.isalnum() for char in password)

def validate_password(password):
    errors = []
    if not check_length(password):
        errors.append("мінімальна довжина менше 8 символів")
    if not check_digit(password):
        errors.append("немає цифр")
    if not check_upper(password):
        errors.append("немає великої літери")
    if not check_lower(password):
        errors.append("немає малої літери")
    if not check_special(password):
        errors.append("немає спеціального символу")
        
    is_valid = len(errors) == 0
    return is_valid, errors

def main():
    print("зАВДАННЯ 4: Перевірка пароля")
    pwd = input("Введіть пароль: ")
    is_valid, errors = validate_password(pwd)
    
    if is_valid:
        print("Пароль надійний.")
    else:
        print("Пароль не відповідає вимогам.")
        print("Не виконано:", ", ".join(errors))

if __name__ == "__main__":
    main()