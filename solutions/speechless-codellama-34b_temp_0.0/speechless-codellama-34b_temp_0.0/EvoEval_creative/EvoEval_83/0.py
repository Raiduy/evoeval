def reverse_vowels(s):
    vowels = 'aeiouAEIOU'
    vowel_list = [c for c in s if c in vowels]
    vowel_list.reverse()
    result = ''
    vowel_index = 0
    for c in s:
        if c in vowels:
            result += vowel_list[vowel_index]
            vowel_index += 1
        else:
            result += c
    return result