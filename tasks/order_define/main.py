import random

if __name__ == "__main__":
    students = ["Белошапкин", "Катричко", "Криворучко",
                "Минкашев", "Порсев Д.", "Порсев Е.",
                "Романов", "Уткин","Ходько",
                "Чхеидзе", "Щукин", "Вильданов 😎"]
    random.shuffle(students)
    for index, student in enumerate(students):
        print(f"{index} -> {student}")
