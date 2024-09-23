
def Strongest_Extension(class_name, extensions):
    strongest_extension = extensions[0]
    max_strength = sum(1 if c.isupper() else -1 for c in extensions[0])

    for extension in extensions[1:]:
        strength = sum(1 if c.isupper() else -1 for c in extension)
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f'{class_name}.{strongest_extension}'
