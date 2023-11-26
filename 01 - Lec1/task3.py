"""
Print the calendar of a given month and year
"""
import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))

print(f"Calender for the year {year}: {calendar.month(year,month)}")