def remove_vowels_and_count(text):
    vowels = 'aeiouAEIOU'
    removed_text = ''
    vowel_count = {}
    for char in text:
        if char in vowels:
            vowel_count[char] = vowel_count.get(char, 0) + 1
        else:
            removed_text += char
    return (removed_text, vowel_count)