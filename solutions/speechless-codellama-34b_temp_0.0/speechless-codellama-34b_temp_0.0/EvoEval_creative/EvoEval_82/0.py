def zodiac_element(birthdays):
    if not birthdays:
        return None
    zodiac_signs = {'Aries': 'Fire', 'Taurus': 'Earth', 'Gemini': 'Air', 'Cancer': 'Water', 'Leo': 'Fire', 'Virgo': 'Earth', 'Libra': 'Air', 'Scorpio': 'Water', 'Sagittarius': 'Fire', 'Capricorn': 'Earth', 'Aquarius': 'Air', 'Pisces': 'Water'}
    element_count = {'Fire': 0, 'Water': 0, 'Air': 0, 'Earth': 0}
    for birthday in birthdays:
        month = int(birthday.split('-')[1])
        day = int(birthday.split('-')[2])
        if month == 3 and day >= 21 or (month == 4 and day <= 19):
            element_count[zodiac_signs['Aries']] += 1
        elif month == 4 and day >= 20 or (month == 5 and day <= 20):
            element_count[zodiac_signs['Taurus']] += 1
        elif month == 5 and day >= 21 or (month == 6 and day <= 20):
            element_count[zodiac_signs['Gemini']] += 1
        elif month == 6 and day >= 21 or (month == 7 and day <= 22):
            element_count[zodiac_signs['Cancer']] += 1
        elif month == 7 and day >= 23 or (month == 8 and day <= 22):
            element_count[zodiac_signs['Leo']] += 1