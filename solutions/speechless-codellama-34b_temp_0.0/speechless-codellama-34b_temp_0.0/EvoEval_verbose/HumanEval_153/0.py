
def Strongest_Extension(class_name, extensions):
    strongest_ext = extensions[0]
    strongest_strength = sum((1 for c in strongest_ext if c.isupper())) - sum((1 for c in strongest_ext if c.islower()))
    for ext in extensions[1:]:
        strength = sum((1 for c in ext if c.isupper())) - sum((1 for c in ext if c.islower()))
        if strength > strongest_strength:
            strongest_ext = ext
            strongest_strength = strength
    return f'{class_name}.{strongest_ext}'