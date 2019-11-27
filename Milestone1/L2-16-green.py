from Cimpl import *


def greenChannel(image: Image) -> Image:
    """Filters out the Blue and Red channels of an image, leaving the green chanel as is
    Written by: Kevin Bai
    >>> image = load_image(choose_file())         "miss_sullivan.jpg"
    >>> turnedGreenLol = greenChannel(image)
    >>> show(turnedGreenLol)
    """
    new_image = copy(image)

    # Set the intensities of blue and red to 0 in every pixel.
    for x, y, (r, g, b) in image:
        greenFilter = create_color(0, g, 0)
        set_color(new_image, x, y, greenFilter)

    return new_image


def testGreenChannel(testThisImage: Image) -> bool:
    """Return whehter every pixel in image filtered by greenChannel has blue and red values equal to 0
    Written by: Kevin Bai
    >>>image = load_image(choose_file("miss_sullivan.jpg"))
    >>> turnedGreenLol = greenChannel(image)
    >>> show(turnedGreenLol)
    >>>testGreenChannel(image)
    True
    """
    comparison = greenChannel(testThisImage)

    for x, y, (r, g, b) in comparison:
        if not (r == 0 and b == 0):
            return False
    return True
