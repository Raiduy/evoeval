def remove_vowels_and_count(text):
    vowels = 'aeiouAEIOU'
    count_dict = {v: 0 for v in vowels if v in text}
    new_text = ''
    for char in text:
        if char in vowels:
            count_dict[char] += 1
        else:
            new_text += char
    return (new_text, {k: v for (k, v) in count_dict.items() if v > 0})