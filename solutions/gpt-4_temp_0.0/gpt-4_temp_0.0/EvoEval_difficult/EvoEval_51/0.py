def remove_vowels_and_count(text):
    vowels = 'aeiouAEIOU'
    vowel_count = {vowel: text.count(vowel) for vowel in vowels if vowel in text}
    no_vowels_text = ''.join([char for char in text if char not in vowels])
    return (no_vowels_text, vowel_count)