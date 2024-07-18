def remove_vowels_and_count(text):
    vowels = 'aeiouAEIOU'
    vowel_count = {v: 0 for v in vowels if v in text}
    no_vowels_text = ''
    for char in text:
        if char in vowels:
            vowel_count[char] += 1
        else:
            no_vowels_text += char
    return (no_vowels_text, vowel_count)