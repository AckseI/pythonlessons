"""
Написать функцию, которая принимает объект datetime и возвращает True, если год полученного значение високосный.
"""

from datetime import date


def leap_year_is(year):
    return year.year % 4 == 0 and year.year % 100 != 0


year = date(2000, 9, 26)
print(leap_year_is(year))
