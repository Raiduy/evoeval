def remove_vowels_and_count(text):
    vowels = 'aeiouAEIOU'
    removed_vowels = ''
    vowel_counts = {}
    for char in text:
        if char in vowels:
            removed_vowels += ''
            if char.lower() in vowel_counts:
                vowel_counts[char.lower()] += 1
            else:
                vowel_counts[char.lower()] = 1
        else:
            removed_vowels += char
    return (removed_vowels, vowel_counts)