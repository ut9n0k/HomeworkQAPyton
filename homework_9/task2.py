# Реализовать функцию которая возвращает дату недельной давности от текущего момента времени.
from datetime import datetime, timedelta


def date_week_before():
    today = datetime.now()
    week = timedelta(7)
    week_before = today - week
    return week_before


if __name__ == "__main__":
    print(date_week_before())
