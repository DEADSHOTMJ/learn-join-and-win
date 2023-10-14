# 3. Convert Month Name to Number of Days
months = {
    'January': 31,
    'February': '28/29',
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}

print("List of months:", ', '.join(months.keys()))
month_name = input("Input the name of Month: ")

if month_name in months:
    days = months[month_name]
    print(f"No. of days: {days} days")
else:
    print("Invalid month name.")
