from datetime import datetime

def validate_row(row: dict):
    try:
        datetime.strptime(row["Дата"], "%d.%m.%Y")
    except ValueError:
        raise ValueError("Invalid date format, expected DD.MM.YYYY")

    if not row["Номер группы"].strip():
        raise ValueError("Empty group number")

    if not row["ФИО"].strip():
        raise ValueError("Empty full name")

    grade = int(row["Оценка"])
    if grade < 2 or grade > 5:
        raise ValueError("Grade must be between 2 and 5")
