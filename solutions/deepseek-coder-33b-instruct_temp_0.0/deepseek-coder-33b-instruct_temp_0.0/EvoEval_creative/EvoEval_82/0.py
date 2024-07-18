def zodiac_element(birthdays):
    if not birthdays:
        return None
    elements = {'Fire': 0, 'Water': 0, 'Air': 0, 'Earth': 0}
    zodiac_signs = {'Aries': 'Fire', 'Taurus': 'Earth', 'Gemini': 'Air', 'Cancer': 'Water', 'Leo': 'Fire', 'Virgo': 'Earth', 'Libra': 'Air', 'Scorpio': 'Water', 'Sagittarius': 'Fire', 'Capricorn': 'Earth', 'Aquarius': 'Air', 'Pisces': 'Water'}
    for birthday in birthdays:
        date = datetime.strptime(birthday, '%Y-%m-%d')
        month = date.month
        day = date.day
        if month == 3 and day >= 21 or (month == 4 and day <= 19):
            elements[zodiac_signs['Aries']] += 1
        elif month == 4 and day >= 20 or (month == 5 and day <= 20):
            elements[zodiac_signs['Taurus']] += 1
        elif month == 5 and day >= 21 or (month == 6 and day <= 20):
            elements[zodiac_signs['Gemini']] += 1
        elif month == 6 and day >= 21 or (month == 7 and day <= 22):
            elements[zodiac_signs['Cancer']] += 1
        elif month == 7 and day >= 23 or (month == 8 and day <= 22):
            elements[zodiac_signs['Leo']] += 1
        elif month == 8 and day >= 23 or (month == 9 and day <= 22):
            elements[zodiac_signs['Virgo']] += 1
        elif month == 9 and day >= 23 or (month == 10 and day <= 22):
            elements[zodiac_signs['Libra']] += 1
        elif month == 10 and day >= 23 or (month == 11 and day <= 21):
            elements[zodiac_signs['Scorpio']] += 1
        elif month == 11 and day >= 22 or (month == 12 and day <= 21):
            elements[zodiac_signs['Sagittarius']] += 1
        elif month == 12 and day >= 22 or (month == 1 and day <= 19):
            elements[zodiac_signs['Capricorn']] += 1
        elif month == 1 and day >= 20 or (month == 2 and day <= 18):
            elements[zodiac_signs['Aquarius']] += 1
        elif month == 2 and day >= 19 or (month == 3 and day <= 20):
            elements[zodiac_signs['Pisces']] += 1
    return {k: v for (k, v) in elements.items() if v > 0}