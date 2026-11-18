import tkinter as tk
import student_utils


def create_report():
  value = count_entry.get().strip()

  # Перевірка коректності введення (ціле число від 1 до 20)
  if not value.isdecimal():
    report_text.delete("1.0", tk.END)
    report_text.insert(tk.END, "Помилка: введіть ціле число від 1 до 20.")
    return

  count = int(value)
  if count < 1 or count > 20:
    report_text.delete("1.0", tk.END)
    report_text.insert(tk.END, "Помилка: кількість оцінок має бути від 1 до 20.")
    return

  students = ["Anna", "Ivan", "Olha"]
  report_lines = []

  for student in students:
    grades = student_utils.generate_grades(count)
    avg = round(student_utils.average_grade(grades), 2)
    level = student_utils.get_level(avg)

    line = f"{student}: {grades} -> {avg} -> {level}"
    report_lines.append(line)

  full_report = "\n".join(report_lines)

  # Вивід у консоль (згідно з умовою)
  print("--- Звіт ---")
  print(full_report)

  # Оновлення текстового поля у вікні Tkinter
  report_text.delete("1.0", tk.END)
  report_text.insert(tk.END, full_report)


# Налаштування головного вікна
window = tk.Tk()
window.title("Статистика учнів")
window.geometry("500x320")

tk.Label(window, text="Введіть кількість оцінок для кожного учня (1-20):").pack(
    pady=5
)

count_entry = tk.Entry(window, width=20)
count_entry.pack(pady=5)

tk.Button(window, text="Сформувати звіт", command=create_report).pack(pady=10)

report_text = tk.Text(window, width=58, height=10)
report_text.pack(pady=10)

window.mainloop()