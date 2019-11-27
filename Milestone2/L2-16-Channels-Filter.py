from Cimpl import *
def blue_channel(file: Image)-> Image:
    """Returns an image containing only the blue channel of an original image.
    Written by: Lachlan Alexander
    Based off code written by ECOR 1051 professors at Carleton University 
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

def check_blue(file: Image)-> bool:
    """ Returns a true value if the value produced is equal to the expected 
    amount, if the values are not the same then the function returns false.
    Written by: Lachlan Alexander
    
    >>>check_blue("p2-original.jpg")
    True
    """
    
    image = blue_channel(file)
    
    for x, y, (r, g, b) in image:
        if not((r ==0) and (g==0)):
            return False
    return True
def red_channel(image : Image) -> Image:
    """Return an image that has only the blue channel of an original image.
    Written by: Basel Syed
    Based off of code written by ECOR 1051 professors at Carleton University
    >>> red_channel(p2-original)
    """
    red_channel_image = copy(image)
    for x, y, (r,g,b) in red_channel_image:
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
    for x, y, (r,g,b) in compared_image:
        if not( g == 0 and b == 0):
            return False
    return True

def greenChannel(image: Image) -> Image:
    
    """Filters out the Blue and Red channels of an image, leaving the green chanel as is
    Written by: Kevin Bai
    Based on code from ECOR 1051 professors at Carleton University
    >>> image = load_image(choose_file())
    >>> turnedGreenLol = greenChannel(image)
    >>> show(turnedGreenLol)
    """
    new_image = copy(image)
    
    # Set the intensities of blue and red to 0 in every pixel.
    for x, y, (r, g, b) in image:
        greenFilter = create_color(0 ,g ,0)
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
        if not(r==0 and b==0):
            return False
    return True
def combine(red_image: Image, green_image: Image, blue_image: Image) -> Image:
    """ Writen by Eryn Ho. Combines three images and creates a 
    >>>combine(red_image, green_image, blue_image:)
    True
    """    
    new_image = copy(red_image)
    for x, y, (r, g, b) in new_image:
        red_colour = get_color(red_image, x, y)
        green_colour = get_color(green_image, x, y)
        blue_colour = get_color(blue_image, x, y)
        combine_colour = create_color(red_colour[0], green_colour[1], blue_colour[2])
        set_color (new_image, x, y, combine_colour)
    show( new_image )
    return new_image 

