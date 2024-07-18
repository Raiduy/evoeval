def zodiac_element(birthdays):
    if not birthdays:
        return None
    zodiacs = [(('03-21', '04-19'), 'Fire'), (('04-20', '05-20'), 'Earth'), (('05-21', '06-20'), 'Air'), (('06-21', '07-22'), 'Water'), (('07-23', '08-22'), 'Fire'), (('08-23', '09-22'), 'Earth'), (('09-23', '10-22'), 'Air'), (('10-23', '11-21'), 'Water'), (('11-22', '12-21'), 'Fire'), (('12-22', '01-19'), 'Earth'), (('01-20', '02-18'), 'Air'), (('02-19', '03-20'), 'Water')]
    elements_count = {}
    for birthday in birthdays:
        (_, month, day) = birthday.split('-')
        birthday_md = f'{month}-{day}'
        for (zodiac_range, element) in zodiacs:
            (start, end) = zodiac_range
            if start > end:
                if birthday_md >= start or birthday_md <= end:
                    elements_count[element] = elements_count.get(element, 0) + 1
                    break
            elif start <= birthday_md <= end:
                elements_count[element] = elements_count.get(element, 0) + 1
                break
    return elements_count