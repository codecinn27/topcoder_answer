from datetime import datetime

# Function to parse the date string
def parse_date(date_str):
    return datetime.strptime(date_str, '%b %d %Y %I:%M%p')

# Read input dates
date1 = parse_date(input().strip())
date2 = parse_date(input().strip())

# Calculate the difference
delta = date2 - date1

# Extract days and time components
days = delta.days
seconds = delta.seconds
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

# Format the output
print(f"{days} days, {hours}:{minutes:02d}:{seconds:02d}")