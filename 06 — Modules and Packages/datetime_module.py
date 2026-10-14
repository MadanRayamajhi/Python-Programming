
# Python Datetime Module

from datetime import datetime, date, time, timedelta

# Current date and time
now = datetime.now()
print("Current date and time:", now)

# Current date
today = date.today()
print("Today's date:", today)

# Create a specific date
birthday = date(2004, 5, 15)
print("Birthday:", birthday)

# Create a specific time
meeting_time = time(10, 30, 0)
print("Meeting time:", meeting_time)

# Format date and time
formatted_date = now.strftime("%d-%m-%Y")
print("Formatted date:", formatted_date)

formatted_time = now.strftime("%I:%M %p")
print("Formatted time:", formatted_time)

# Add days to a date
future_date = today + timedelta(days=7)
print("Date after 7 days:", future_date)

# Calculate the difference between dates
start_date = date(2026, 1, 1)
end_date = date(2026, 12, 31)

difference = end_date - start_date
print("Days between dates:", difference.days)
