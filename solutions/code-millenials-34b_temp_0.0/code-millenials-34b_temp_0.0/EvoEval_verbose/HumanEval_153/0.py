
def Strongest_Extension(class_name, extensions):
    strongest_ext = extensions[0]
    strongest_strength = sum([1 if c.isupper() else -1 for c in extensions[0]])
    for ext in extensions[1:]:
        strength = sum([1 if c.isupper() else -1 for c in ext])
        if strength > strongest_strength:
            strongest_ext = ext
            strongest_strength = strength
    return f'{class_name}.{strongest_ext}'