def fix_to_grid(position, dimensions):
    return (position // dimensions) * dimensions


def combined_lists(a, b):
    return tuple(a) + tuple(b)
