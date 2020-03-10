from Cimpl import *

red_image = load_image(choose_file())
green_image = load_image(choose_file())
blue_image = load_image(choose_file())

def combine(red_image: Image, green_image: Image, blue_image: Image) -> Image:
    new_image = copy(red_image)
    for x, y, (r, g, b) in new_image:
        red_colour = get_color(red_image, x, y)
        green_colour = get_color(green_image, x, y)
        blue_colour = get_color(blue_image, x, y)
        combine_colour = create_color(red_colour[0], green_colour[1], blue_colour[2])
        set_color (new_image, x, y, combine_colour)

    show(new_image)
    return new_image
