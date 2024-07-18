def zodiac_element(birthdays):
    if not birthdays:
        return None
    zodiac_elements = {'Aries': 'Fire', 'Taurus': 'Earth', 'Gemini': 'Air', 'Cancer': 'Water', 'Leo': 'Fire', 'Virgo': 'Earth', 'Libra': 'Air', 'Scorpio': 'Water', 'Sagittarius': 'Fire', 'Capricorn': 'Earth', 'Aquarius': 'Air', 'Pisces': 'Water'}
    zodiac_dates = {'Aries': (3, 21), 'Taurus': (4, 20), 'Gemini': (5, 21), 'Cancer': (6, 21), 'Leo': (7, 23), 'Virgo': (8, 23), 'Libra': (9, 23), 'Scorpio': (10, 23), 'Sagittarius': (11, 22), 'Capricorn': (12, 22), 'Aquarius': (1, 20), 'Pisces': (2, 19)}
    element_counts = defaultdict(int)
    for birthday in birthdays:
        date = datetime.strptime(birthday, '%Y-%m-%d')
        for (zodiac, (month, day)) in zodiac_dates.items():
            if (date.month, date.day) >= (month, day):
                element = zodiac_elements[zodiac]
                element_counts[element] += 1
                break
    return dict(element_counts)