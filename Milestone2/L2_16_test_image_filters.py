
from Cimpl import create_color, show, load_image, choose_file, set_color, get_color, Image, copy, get_height, get_width, create_image
from L2_16_image_filters import two_tone, three_tone, extreme_contrast, grayscale, sepia, posterize, _adjust_component, detect_edges, flip_vertical, flip_horizontal, detect_edges_better

def check_equal(description: str, outcome, expected) -> None:
  
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:
        print("{0} FAILED: expected ({1}) has type {2}, "
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '),
                     outcome, str(outcome_type).strip('<class> ')))
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
    else:
        print("{0} PASSED".format(description))
    print("------")


def test_extreme() -> None:

    original = create_image(3, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(128, 127, 128))
    set_color(original, 2, 0, create_color(255, 255, 255))

    expected = create_image(3, 1)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(146, 127, 118))
    set_color(expected, 2, 0, create_color(255, 255, 237))

    filtered = sepia(original)

    for x, y, col in filtered:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


def two_tone_test(pretested_image: Image) -> bool:

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    lime = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    cyan = (0, 255, 255)
    magenta = (255, 0, 255)
    gray = (128, 128, 128)
    color_names = ["black", "white", "red", "lime", "blue", "yellow", "cyan", "magenta", "gray"]
    color_values = [black, white, red, lime, blue, yellow, cyan, magenta, gray]
    print(color_names)
    first_tone = input("Please choose a color from one of the colors listed above ")
    second_tone = input("Please choose another color from the colors listed above ")
    
    for i in range(len(color_names)):
        if color_names[i] == first_tone:
            tone_1 = color_values[i]
    for i in range(len(color_names)):
        if color_names[i] == second_tone:
            tone_2 = color_values[i]    
    tested_image = two_tone(pretested_image, first_tone, second_tone)
    for x, y, (r, g, b) in tested_image:
        if (r, g, b) == tone_1 or (r, g, b) == tone_2:
            return True
        else:
            return False
        
        
def three_tone_test(pretested_image : Image) -> bool:
 
    
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    lime = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    cyan = (0, 255, 255)
    magenta = (255, 0, 255)
    gray = (128, 128, 128)
    color_names = ["black", "white", "red", "lime", "blue", "yellow", "cyan", "magenta", "gray"]
    color_values = [black, white, red, lime, blue, yellow, cyan, magenta, gray]
    print(color_names)
    first_tone = input("Please choose a color from one of the colors listed above ")
    second_tone = input("Please choose another color from the colors listed above ")
    third_tone = input("Please choose another color from the colors listed above ")
    for i in range(len(color_names)):
        if color_names[i] == first_tone:
            tone_1= color_values[i]
    for i in range(len(color_names)):
        if color_names[i] == second_tone:
            tone_2 = color_values[i]
    for i in range(len(color_names)):
        if color_names[i] == third_tone:
            tone_3 = color_values[i]    
    tested_image = three_tone(pretested_image, first_tone, second_tone, third_tone)
    for x, y, (r, g, b) in tested_image:
        if (r, g, b) == tone_1 or (r, g, b) == tone_2 or (r, g, b) == tone_3:
            return True
        else:
            return False
        
        
def test_sepia(image: Image) -> bool:
 
    sepia_image = sepia(image)
    errors = 0 
    
    for x, y, (r, g, b) in sepia_image:
        
        if r == int(g * 1.1) and b == int(g * 0.9):
            errors += 0 
            
        elif r == int(g * 1.15) and b == int(g * 0.85):
            errors += 0 
            
        elif r == int(g * 1.08) and b == int(g * 0.93):
            errors += 0 
            
        elif g >= 237 and r == 255 and b == int(g * 0.93):
            errors += 0
 
        else:
            errors += 1
    if errors == 0:
        return True
    else:
        return False
    
    
def posterize_test() -> bool:
 
    tested_image = posterize(original_image)
    for x, y, (r, g, b) in tested_image:
        if r == 31 or r == 95 or r == 159 or r == 223:
            if g == 31 or g == 95 or g == 159 or g == 223:
                if b == 31 or b == 95 or b == 159 or b == 223:
                    return True
        else:
            return False
        
        
def test_edge(image: Image, threshold: float) -> bool:


    errors = 0
   
    new_image = detect_edges(image, threshold)

    for x in range(get_width(image)):
        for y in range(get_height(image) - 1):
            
            
            colour_below = get_color(image, x, y + 1)
            colour_normal = get_color(image, x, y)
            current_colour = get_color(new_image, x, y)

            brightness = abs((colour_normal[0] + colour_normal[1] + colour_normal[2]) // 3
                             - (colour_below[0] + colour_below[1] + colour_below[2]) // 3)
           
            if brightness > threshold and current_colour[0] == 0 and current_colour[1] == 0 and current_colour[2] == 0:
                errors += 0
            elif brightness <= threshold and current_colour[0] == 255 and current_colour[1] == 255 and current_colour[2] == 255:
                errors += 0
            else:
                errors += 1

    if errors == 0:
        return True
    else:
        return False
    
    
def detect_edges_better_test(image: Image, threshold: float) -> bool:
   
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    error_counter = 0
    tested_image = detect_edges_better(image, threshold)
    for y in range(get_height(new_image) - 1):
        for x in range(get_width(new_image) - 1):

            colour_point = get_color(image, x, y)
            brightness_point = (colour_point[0] + colour_point[1] + colour_point[2]) / 3

            colour_below = get_color(image, x, y + 1)
            brightness_below = (colour_below[0] + colour_below[1] + colour_below[2]) / 3

            colour_beside = get_color(image, x + 1, y)
            brightness_beside = (colour_beside[0] + colour_beside[1] + colour_beside[2]) / 3  
            tested_color = get_color(tested_image, x, y)
            if (abs(brightness_point - brightness_below) > threshold or abs(brightness_point - brightness_beside) > threshold) and (tested_color[0] == 0 and tested_color[1] == 0 and tested_color[2] == 0):
                error_counter +=0
            elif (abs(brightness_point - brightness_below) < threshold or abs(brightness_point - brightness_beside) < threshold) and (tested_color[0] == 255 and tested_color[1] == 255 and tested_color[2] == 255):
                error_counter += 0
            else:
                error_counter+=1
    if error_counter > 0:
        return True
    else:
        return False
    
    
def flip_vertical_test(image: Image) -> bool:
   
    count = 0
    flipped_image =flip_vertical(image)
    image_width = get_height(image)
    for x, y, (r, g, b) in flipped_image:
        if not((image_width-1-x) != x):
            count += 1
    if count == 0:
        return True
    else:
        return False
    
def test_horizontal() -> None:
 
    
    original = create_image(3, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(128, 127, 128))
    set_color(original, 2, 0,  create_color(255, 255, 255))
    
    expected = create_image(3, 1)
    set_color(expected, 0, 0,  create_color(255, 255, 255))
    set_color(expected, 1, 0,  create_color(127, 128, 127))
    set_color(expected, 2, 0,  create_color(0, 0, 0))
    
    horizontal_flip = horizontal(original)
    
    for x, y, col in horizontal_flip:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))
