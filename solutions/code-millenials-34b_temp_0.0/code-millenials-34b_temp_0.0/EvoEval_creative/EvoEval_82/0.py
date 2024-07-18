def zodiac_element(birthdays):
    if not birthdays:
        return None
    elements = {'Fire': ['03-21', '04-19', '07-23', '08-23', '11-23', '12-22'], 'Water': ['06-21', '07-23', '02-19', '03-20'], 'Air': ['05-21', '06-21', '09-23', '10-23', '11-22', '01-20'], 'Earth': ['04-20', '05-21', '08-22', '09-22', '10-22', '11-21']}
    result = {}
    for birthday in birthdays:
        (month, day) = birthday.split('-')
        for (element, dates) in elements.items():
            if day + '-' + month in dates:
                result[element] = result.get(element, 0) + 1
    return result