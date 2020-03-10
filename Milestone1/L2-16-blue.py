from Cimpl import *

def blue_channel(file: Image) -> Image:
   
    image = load_image(file)
    blue_channel_image = copy(image)
    for pixel in blue_channel_image:
        x, y, (r, g, b) = pixel
        blue_fill = create_color(0, 0, b)
        set_color(blue_channel_image, x, y, blue_fill)
    show(blue_channel_image)
    return blue_channel_image


def check_blue(file: Image) -> bool:
    
    image = blue_channel(file)

    for x, y, (r, g, b) in image:
        if not ((r == 0) and (g == 0)):
            return False
    return True
