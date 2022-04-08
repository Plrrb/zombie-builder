def fix_to_grid(position, dimensions):
    return (position // dimensions) * dimensions


def combine_lists(a, b):
    for item in b:
        a.append(item)

    return a
