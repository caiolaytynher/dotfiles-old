def listify(color_name: str, gradient_color: str = "") -> list[str]:
    """
    Converts a color into a valid qtile color list format.
    '#FFFFFF' -> ['#FFFFFF', '#FFFFFF']
    """
    if gradient_color:
        return [color_name, gradient_color]

    return [color_name] * 2
