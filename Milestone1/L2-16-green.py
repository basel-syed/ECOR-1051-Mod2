from Cimpl import *


def greenChannel(image: Image) -> Image:

    new_image = copy(image)

    for x, y, (r, g, b) in image:
        greenFilter = create_color(0, g, 0)
        set_color(new_image, x, y, greenFilter)

    return new_image


def testGreenChannel(testThisImage: Image) -> bool:
    comparison = greenChannel(testThisImage)

    for x, y, (r, g, b) in comparison:
        if not (r == 0 and b == 0):
            return False
    return True
