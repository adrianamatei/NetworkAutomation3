def is_year_leap(year):
    # An bisect: divizibil cu 4 și (nu cu 100 sau da cu 400)
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    # Verificare date valide
    if month < 1 or month > 12 or year < 1:
        return None

    # Zilele standard ale lunilor
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Ajustăm februarie dacă anul e bisect
    if is_year_leap(year):
        month_lengths[1] = 29

    return month_lengths[month - 1]

def day_of_year(year, month, day):
    # Verificăm dacă data e validă
    if days_in_month(year, month) is None or day < 1 or day > days_in_month(year, month):
        return None

    # Inițializăm un contor pentru numărul total de zile
    total_days = 0

    # Adunăm zilele din lunile anterioare
    for m in range(1, month):
        total_days += days_in_month(year, m)

    # Adăugăm zilele din luna curentă
    total_days += day

    return total_days

print(day_of_year(2000, 12, 27))
