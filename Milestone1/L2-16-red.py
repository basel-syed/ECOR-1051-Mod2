from Cimpl import *

def red_channel(image: Image) -> Image:
    """Return an image that has only the blue channel of an original image.
    Written by: Basel Syed

    >>> red_channel(p2-original)
    """
    red_channel_image = copy(image)
    for x, y, (r, g, b) in red_channel_image:
        redfill = create_color(r, 0, 0)
        set_color(red_channel_image, x, y, redfill)
    show(red_channel_image)
    return red_channel_image


def test_red(image: Image) -> bool:
    """Returns true all pixels in image filtered by red_channel
    Writtern by: Basel Syed

    >>>test_red("p2-original.jpg")
    True
    """
    compared_image = red_channel(image)
    for x, y, (r, g, b) in compared_image:
        if not (g == 0 and b == 0):
            return False
    return True
