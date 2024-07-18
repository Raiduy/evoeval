def zodiac_element(birthdays):
    if not birthdays:
        return None
    elements = {'Fire': 0, 'Water': 0, 'Air': 0, 'Earth': 0}
    for birthday in birthdays:
        month = int(birthday[5:7])
        day = int(birthday[8:10])
        if month == 3 and day >= 21 or (month == 4 and day <= 19):
            elements['Fire'] += 1
        elif month == 4 and day >= 20 or (month == 5 and day <= 20):
            elements['Earth'] += 1
        elif month == 5 and day >= 21 or (month == 6 and day <= 20):
            elements['Air'] += 1
        elif month == 6 and day >= 21 or (month == 7 and day <= 22):
            elements['Water'] += 1
        elif month == 7 and day >= 23 or (month == 8 and day <= 22):
            elements['Fire'] += 1
        elif month == 8 and day >= 23 or (month == 9 and day <= 22):
            elements['Earth'] += 1
        elif month == 9 and day >= 23 or (month == 10 and day <= 22):
            elements['Air'] += 1
        elif month == 10 and day >= 23 or (month == 11 and day <= 21):
            elements['Water'] += 1
        elif month == 11 and day >= 22 or (month == 12 and day <= 21):
            elements['Fire'] += 1
        elif month == 12 and day >= 22 or (month == 1 and day <= 19):
            elements['Earth'] += 1
        elif month == 1 and day >= 20 or (month == 2 and day <= 18):
            elements['Air'] += 1
        elif month == 2 and day >= 19 or (month == 3 and day <= 20):
            elements['Water'] += 1
    return {k: v for (k, v) in elements.items() if v > 0}