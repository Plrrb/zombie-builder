def fix_to_grid(position, dimensions):
    return (position // dimensions) * dimensions


def combined_lists(a: iter, b: iter):
    a = list(a)
    b = list(b)

    for item in b:
        a.append(item)

    return a
