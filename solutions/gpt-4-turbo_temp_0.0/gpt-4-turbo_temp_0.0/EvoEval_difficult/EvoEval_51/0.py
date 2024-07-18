def remove_vowels_and_count(text):
    vowels = 'aeiouAEIOU'
    vowel_count = {}
    no_vowels_text = []
    for char in text:
        if char in vowels:
            if char in vowel_count:
                vowel_count[char] += 1
            else:
                vowel_count[char] = 1
        else:
            no_vowels_text.append(char)
    no_vowels_text = ''.join(no_vowels_text)
    return (no_vowels_text, vowel_count)