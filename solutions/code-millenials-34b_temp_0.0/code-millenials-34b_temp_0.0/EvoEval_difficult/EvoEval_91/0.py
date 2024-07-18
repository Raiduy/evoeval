def detect_boredom(S, substrings):
    count = 0
    S = re.sub('\\s*\\([^)]*\\)\\s*|\\s*\\[[^]]*\\]\\s*|\\s*\\{[^}]*\\}\\s*|\\s*"[^"]*"\\s*', ' ', S)
    sentences = re.split('\\.\\s*|\\?\\s*|\\!\\s*', S)
    for sentence in sentences:
        if any((sentence.strip().startswith(sub) for sub in substrings)):
            count += 1
    return count