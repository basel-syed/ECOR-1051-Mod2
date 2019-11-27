"""Milestone 2 P6 Group Submission Filters

Group: L2-16

"""
from Cimpl import create_color, show, load_image, choose_file, set_color, get_color, Image, copy, get_height, get_width

def two_tone(image: Image, colour_1: str, colour_2: str) -> Image:
    """ Returns a copy of a specified image where the RGB values consist of 2 
    different colour tones based on the brightness of each pixel.
    Written by: Lachlan Alexander
    
    >>>image = load_image(choose_file())
    >>>two_tone(ORIGINAL_IMAGE, "black", "white")
    Image
    
    """
    #Colour variables with assigned RGB values.
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    lime = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    cyan = (0, 255, 255)
    magenta = (255, 0, 255)
    gray = (128, 128, 128)

    #List of strings of colours.
    colour_names = ["black", "white", "red", "lime", "blue", "yellow", "cyan",
                    "magenta", "gray"]
    #List of variables of colours.
    colour_values = [black, white, red, lime, blue, yellow, cyan, magenta, gray]
    
    #Loops that compare the values of the inputted strings to determine which
    #colour variable needs to be applied.
    for i in range(len(colour_names)):
        if colour_names[i] == colour_1:
            tone_1 = colour_values[i]
    for i in range(len(colour_names)):
        if colour_names[i] == colour_2:
            tone_2 = colour_values[i]

    toned = copy(image)
    for pixel in toned:
        x, y, (r, g, b) = pixel
        brightness = (r + g + b) // 3
        if brightness <= 127: #If the brightness is less than or equal to 127
                              #then the colour is assigned to colour_1
            colour_change_1 = create_color(tone_1[0], tone_1[1], tone_1[2])
            set_color(toned, x, y, colour_change_1)
        elif brightness >= 128: #If the brightness is greater than of equal to
                                #128 then the colour is assigned to colour_2
            colour_change_2 = create_color(tone_2[0], tone_2[1], tone_2[2])
            set_color(toned, x, y, colour_change_2)
    show(toned)
    return toned


def three_tone(image: Image, colour_1: str, colour_2: str, colour_3: str) -> Image:
    """ Returns a copy of a specified image where the RGB values consist of 3 set colour tones based on the brightness of each pixel.
    Written by: Lachlan Alexander
    
    >>>ORIGINAL_IMAGE = load_image(choose_file())
    >>>three_tone(ORIGINAL_IMAGE, "black", "white", "gray")
    Image
    
    """
    #Colour variables with assigned RGB values.
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    lime = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    cyan = (0, 255, 255)
    magenta = (255, 0, 255)
    gray = (128, 128, 128)

    #List of strings of colours.
    colour_names = ["black", "white", "red", "lime", "blue", "yellow", "cyan",
                    "magenta", "gray"]
    
    #List of variables of colours.
    colour_values = [black, white, red, lime, blue, yellow, cyan, magenta, gray]
    
    #Loops that compare the values of the inputted strings to determine which
    #colour variable needs to be applied.    
    for i in range(len(colour_names)):
        if colour_names[i] == colour_1:
            tone_1 = colour_values[i]
    for i in range(len(colour_names)):
        if colour_names[i] == colour_2:
            tone_2 = colour_values[i]
    for i in range(len(colour_names)):
        if colour_names[i] == colour_3:
            tone_3 = colour_values[i]

    toned = copy(image)
    for pixel in toned:
        x, y, (r, g, b) = pixel
        brightness = (r + g + b) // 3
        if brightness <= 84:  #If the brightness is less than or equal to 84
                              #then the colour is assigned to colour_1
            colour_change_1 = create_color(tone_1[0], tone_1[1], tone_1[2])
            set_color(toned, x, y, colour_change_1)
            
        elif brightness >= 85 and brightness <= 170:
            #If the brightness is less than or equal to 170 or greater than or 
            #equal to 85 then the colour is assigned to colour_2            
            colour_change_2 = create_color(tone_2[0], tone_2[1], tone_2[2])
            set_color(toned, x, y, colour_change_2)
            
        elif brightness >= 171: #If the brightness is less than or equal to 171
                                #then the colour is assigned to colour_3
            colour_change_3 = create_color(tone_3[0], tone_3[1], tone_3[2])
            set_color(toned, x, y, colour_change_3)
    show(toned)
    return toned


def extreme_contrast(image: Image) -> Image:
    """Returns an image with an extreme contrast filter applied
    Written By: Basel Syed
    
    >>>extreme_contrast(newImage)
    Image
    
    """
    copied_image = copy(image)  
    for x, y, (r,g,b) in copied_image:
        if r >= 128:
            r = 255
        elif r <= 127:
            r = 0
        if g >= 128:
            g = 255
        elif g <= 127:
            g = 0 
        if b >= 128:
            b = 255
        elif b <= 127:
            b = 0
        contrasted_pixel = create_color(r, g, b)
        set_color(copied_image, x, y, contrasted_pixel)
    show(copied_image)
    return copied_image
def grayscale(image: Image) -> Image:
    """Return a grayscale copy of image.
    Written by ECOR 1051 professors
    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    grayscale_image = copy(image)
    """Returns gray image"""
    for x, y, (r, g, b) in grayscale_image:

        brightness = (r + g + b) // 3
        gray = create_color(brightness, brightness, brightness)
        set_color(grayscale_image, x, y, gray)

    return grayscale_image

def sepia(image: Image) -> Image:
    """ Written by Eryn Ho. Returns an increaed the value and decreased the blue
    value for an image by a certain factor.
    >>>sepia(original_image)
    <Cimpl.Image object at 0x000002004BA6B5C8>
    """
    new_image = grayscale(image)
    for x, y, (r, g, b) in new_image:
        colours = get_color(new_image, x, y)
        if (g < 63):
            r = r * 1.1
            g = g
            b = b * 0.9
        elif (g <= 191):
            r = r * 1.15
            g = g
            b = b * 0.85
        else:
            r = r * 1.08
            g = g
            b = b * 0.93
        new_colour = create_color(r, g, b)
        set_color(new_image, x, y, new_colour) 
               
    show(new_image)    
    return new_image
def posterize(original_image: Image) -> Image:
    """ Writen by Eryn Ho. Creates new image with colours readjusted to fit into certain ranges
    >>>posterize(original_image)
    <Cimpl.Image object at 0x0000027BD844B0C8>
    """
    posterized_image = copy(original_image)
    for x, y, (r, g, b) in posterized_image:
        colours = get_color(original_image, x, y)
        red_component = _adjust_component(colours[0])
        green_component = _adjust_component(colours[1])
        blue_component = _adjust_component(colours[2])
        new_colour = create_color(red_component, green_component, blue_component)
        set_color(posterized_image, x, y, new_colour)
    show(posterized_image)
    return posterized_image


def _adjust_component(colour: int) -> int:
    """Returns new colour value for a set range of colour values."""
    if(colour < 64):
        colour = 31
    elif(colour < 128):
        colour = 95
    elif(colour < 192):
        colour = 159
    else:
        colour = 223
    return colour


def detect_edges(image: Image, threshold: float) ->Image:
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    image_copied = copy(image)
    for y in range(0, get_height(image_copied) - 1):
        for x in range(0, get_width(image_copied)):
            r, g, b = get_color(image_copied, x, y)
            r2, g2, b2 = get_color(image_copied, x, y + 1)
            if abs((r + g + b) // 3 - (r2 + g2 + b2) // 3) > threshold:
                set_color(image_copied, x, y, black)
            else:
                set_color(image_copied, x, y, white)
    show(image_copied)
    return image_copied


def flip_vertical(imge: Image) -> Image:
    """ Writen by Eryn Ho. Returns original image flipped along the vertical axis.
    >>>flip_vertical(original_image)
    <Cimpl.Image object at 0x000001C9737A6E08>
    """
    vertical_flip = copy(imge)
    for x, y, (r, g, b) in imge:
        new_colour = create_color(r, g, b)
        set_color(vertical_flip, -x, y, new_colour)
    show(vertical_flip)
    return vertical_flip


def flip_horizontal(image: Image) -> Image:
    """Returns a copy of an image that whose pixels have been flipped in the 
    horizontal direction.
    
    Written by: Lachlan Alexander
    Based on code from L2_16_P5_vertical written by: Eryn Ho
    
    >>> ORIGINAL = load_image(choose_file())
    >>> flip_horizontal(ORIGINAL)
    Image
    
    """

    new_image = copy(image)

    for x in range(get_width(new_image)):
        for y in range(get_height(new_image)):
            current_colour = get_color(image, x, y)
            set_color(new_image, x, -y, current_colour)
            #Switches the colour with the colour of the pixel in the oposite x 
            #coordinate.
    show(new_image)
    return new_image

def detect_edges_better(image: Image, threshold: float) -> Image:
    """Returns a black and white copy of an image, where the pixels are black if
    they have high contrast with the pixels to their right and below, if they 
    have low contrast then the pixel is white.
    By: Lachlan Alexander
    Based on code from L2_16_P5_edge written by: Basel Syed
    
    >>> ORIGINAL_IMAGE = load_image(choose_file())
    >>> detect_edges_better(ORIGINAL_IMAGE, 3)
    Image
    
    """

    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    
    new_image = copy(image)

    for y in range(get_height(new_image) - 1):
        for x in range(get_width(new_image) - 1):
            
            #Get the colour and brightness of the current point.
            colour_point = get_color(new_image, x, y)
            brightness_point = (colour_point[0] + colour_point[1] + colour_point[2]) / 3
            
            #Get the colour and brightness of the point below the current point.
            colour_below = get_color(new_image, x, y + 1)
            brightness_below = (colour_below[0] + colour_below[1] + colour_below[2]) / 3

            #Get the colour and brightness of the point to the right of the current point.
            colour_beside = get_color(new_image, x + 1, y)
            brightness_beside = (colour_beside[0] + colour_beside[1] + colour_beside[2]) / 3

            if abs(brightness_point - brightness_below) > threshold or abs(brightness_point - brightness_beside) > threshold:
                set_color(new_image, x, y, black)
                #If the brightness of the image compared to the pixels around it
                #is low then change the colour to black.

            else:
                set_color(new_image, x, y, white)
                #If the brightness of the image compared to the pixels around it
                #is high then change the colour to white.                

    show(new_image)
    return new_image