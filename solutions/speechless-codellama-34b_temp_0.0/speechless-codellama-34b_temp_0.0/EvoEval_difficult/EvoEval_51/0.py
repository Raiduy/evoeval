def remove_vowels_and_count(text):
    vowels = 'aeiouAEIOU'
    vowel_count = {}
    new_text = ''
    for char in text:
        if char not in vowels:
            new_text += char
        elif char in vowels:
            if char in vowel_count:
                vowel_count[char] += 1
            else:
                vowel_count[char] = 1
    return (new_text, vowel_count)