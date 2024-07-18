
def valid_date(date):
    # Check if the date string is not empty
    if not date:
        return False
    
    # Check the format of the date string
    try:
        parts = date.split('-')
        if len(parts) != 3:
            return False
        
        month, day, year = parts
        month = int(month)
        day = int(day)
        year = int(year)  # Even though we don't have a specific rule for the year, we need to ensure it's a valid integer
        
        # Check the month range
        if month < 1 or month > 12:
            return False
        
        # Define the maximum days in each month
        if month in [1, 3, 5, 7, 8, 10, 12]:
            max_days = 31
        elif month in [4, 6, 9, 11]:
            max_days = 30
        else:  # February
            max_days = 29
        
        # Check the day range
        if day < 1 or day > max_days:
            return False
        
        return True
    except ValueError:
        # If conversion to integer fails, the date is invalid
        return False
