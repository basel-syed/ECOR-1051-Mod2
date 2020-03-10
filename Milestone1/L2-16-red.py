from Cimpl import *

def red_channel(image: Image) -> Image:

    red_channel_image = copy(image)
    for x, y, (r, g, b) in red_channel_image:
        redfill = create_color(r, 0, 0)
        set_color(red_channel_image, x, y, redfill)
    show(red_channel_image)
    return red_channel_image


def test_red(image: Image) -> bool:

    compared_image = red_channel(image)
    for x, y, (r, g, b) in compared_image:
        if not (g == 0 and b == 0):
            return False
    return True
