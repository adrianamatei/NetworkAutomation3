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


# Teste
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
