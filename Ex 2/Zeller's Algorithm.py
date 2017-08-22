import sys

print("This program calculates the day of the week for any date.")

DAYS = ("Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December")
DAYS_IN_MONTH = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def get_date():
    str_date = input("Enter date (MM/DD/YYYY): ")
    parts = str_date.split('/')
    length = len(parts)
    if length != 3:
        print()
        raise ValueError("Invalid format for date.")
    for i in range(length):
        parts[i] = parts[i].strip()
        if len(parts[i]) == 0 or not parts[i].isdigit():
            print()
            raise ValueError("Invalid format for date.")
    return (int(parts[0]), int(parts[1]), int(parts[2]))


def is_date_valid(month, day, year):
    if month < 1 or month > 12 or day < 1 or year < 0:
        return False
    days_in_month = DAYS_IN_MONTH[month - 1]
    if month != 2:
        return day <= days_in_month
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        days_in_month += 1
    return day <= days_in_month


def date_as_string(month, day, year):
    return MONTHS[month - 1] + " " + str(day) + ", " + str(year)


def day_of_week(month, day, year):
    if month == 1 or month == 2:
        month += 12
        year -= 1
    J = year // 100
    K = year % 100
    m = month
    q = day
    h = int((q + 26 * (m + 1) // 10 + K + (K // 4) + (J // 4) - (2 * J)) % 7)
    return DAYS[h]


def main():
    try:
        (month, day, year) = get_date()
        is_date_valid(month, day, year)
    except ValueError as error:
        print("ERROR:", error)
        sys.exit(1)
    if not is_date_valid(month, day, year):
        print()
        print(str(month) + "/" + str(day) + "/" + str(year) + " is an invalid date.")
        sys.exit(1)
    else:
        weekday = day_of_week(month, day, year)
        x = date_as_string(month, day, year)
        print()
        print(str(x) + " is a " + str(weekday + "."))


if __name__ == "__main__":
    main()