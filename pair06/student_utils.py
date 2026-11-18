import random
import statistics


def generate_grades(count):
  """Повертає список випадкових оцінок від 1 до 12."""
  grades = []
  for _ in range(count):
    grades.append(random.randint(1, 12))
  return grades


def average_grade(grades):
  """Повертає середній бал."""
  if not grades:
    return 0
  return statistics.mean(grades)


def get_level(average):
  """Визначає рівень навчальних досягнень за середнім балом."""
  if average >= 10:
    return "високий"
  elif average >= 7:
    return "достатній"
  elif average >= 4:
    return "середній"
  else:
    return "початковий"


if __name__ == "__main__":
  # Тестовий запуск модуля
  test_grades = generate_grades(5)
  avg = average_grade(test_grades)
  print("Тест:", test_grades, "->", round(avg, 2), "->", get_level(avg))