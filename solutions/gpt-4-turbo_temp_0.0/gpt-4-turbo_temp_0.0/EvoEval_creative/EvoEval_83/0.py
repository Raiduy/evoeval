def reverse_vowels(s):
    vowels = 'aeiouAEIOU'
    reversed_vowels = [char for char in s if char in vowels][::-1]
    s_list = list(s)
    reversed_vowels_index = 0
    for i in range(len(s_list)):
        if s_list[i] in vowels:
            s_list[i] = reversed_vowels[reversed_vowels_index]
            reversed_vowels_index += 1
    return ''.join(s_list)