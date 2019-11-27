from Cimpl import *

def blue_channel(file: Image) -> Image:
    """Returns an image containing only the blue channel of an original image.
    Written by: Lachlan Alexander

    >>>blue_channel(file)
    blue_channel_image

    """
    image = load_image(file)
    blue_channel_image = copy(image)
    for pixel in blue_channel_image:
        x, y, (r, g, b) = pixel
        blue_fill = create_color(0, 0, b)
        set_color(blue_channel_image, x, y, blue_fill)
    show(blue_channel_image)
    return blue_channel_image


def check_blue(file: Image) -> bool:
    """ Returns a true value if the value produced is equal to the expected
    amount, if the values are not the same then the function returns false.
    Written by: Lachlan Alexander

    >>>check_blue("p2-original.jpg")
    True
    """

    image = blue_channel(file)

    for x, y, (r, g, b) in image:
        if not ((r == 0) and (g == 0)):
            return False
    return True