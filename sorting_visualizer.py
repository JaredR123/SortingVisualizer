import pygame
import random
import math
import time
pygame.init()

SCREEN_WIDTH = 1280 # 1280
SCREEN_HEIGHT = 720 # 720
BUTTONS_PER_SCREEN = 6
HEADER_SIZE = SCREEN_HEIGHT / 5

button_width = SCREEN_WIDTH / BUTTONS_PER_SCREEN
button_height = HEADER_SIZE / 2

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # , pygame.FULLSCREEN

arr_access_counter = 0
time_counter = 0

# Button Images
red_button = pygame.transform.scale(pygame.image.load('assets/sv_button_red.png').convert_alpha(), (button_width, button_height))
blue_button = pygame.transform.scale(pygame.image.load('assets/sv_button_blue.png').convert_alpha(), (button_width, button_height))
brown_button = pygame.transform.scale(pygame.image.load('assets/sv_button_brown.png').convert_alpha(), (button_width, button_height))
dark_green_button = pygame.transform.scale(pygame.image.load('assets/sv_button_dark_green.png').convert_alpha(), (button_width, button_height))
gray_button = pygame.transform.scale(pygame.image.load('assets/sv_button_gray.png').convert_alpha(), (button_width, button_height))
light_blue_button = pygame.transform.scale(pygame.image.load('assets/sv_button_light_blue.png').convert_alpha(), (button_width, button_height))
light_green_button = pygame.transform.scale(pygame.image.load('assets/sv_button_light_green.png').convert_alpha(), (button_width, button_height))
maroon_button = pygame.transform.scale(pygame.image.load('assets/sv_button_maroon.png').convert_alpha(), (button_width, button_height))
orange_button = pygame.transform.scale(pygame.image.load('assets/sv_button_orange.png').convert_alpha(), (button_width, button_height))
violet_button = pygame.transform.scale(pygame.image.load('assets/sv_button_violet.png').convert_alpha(), (button_width, button_height))
yellow_button = pygame.transform.scale(pygame.image.load('assets/sv_button_yellow.png').convert_alpha(), (button_width, button_height))

# Button Pressed Images
red_button_pressed = pygame.transform.scale(pygame.image.load('assets/sv_button_red_pressed.png').convert_alpha(), (button_width, button_height))
blue_button_pressed = pygame.transform.scale(pygame.image.load('assets/sv_button_blue_pressed.png').convert_alpha(), (button_width, button_height))
brown_button_pressed = pygame.transform.scale(pygame.image.load('assets/sv_button_brown_pressed.png').convert_alpha(), (button_width, button_height))
dark_green_button_pressed = pygame.transform.scale(pygame.image.load('assets/sv_button_dark_green_pressed.png').convert_alpha(), (button_width, button_height))
gray_button_pressed = pygame.transform.scale(pygame.image.load('assets/sv_button_gray_pressed.png').convert_alpha(), (button_width, button_height))
light_blue_button_pressed = pygame.transform.scale(pygame.image.load('assets/sv_button_light_blue_pressed.png').convert_alpha(), (button_width, button_height))
light_green_button_pressed = pygame.transform.scale(pygame.image.load('assets/sv_button_light_green_pressed.png').convert_alpha(), (button_width, button_height))
maroon_button_pressed = pygame.transform.scale(pygame.image.load('assets/sv_button_maroon_pressed.png').convert_alpha(), (button_width, button_height))
orange_button_pressed = pygame.transform.scale(pygame.image.load('assets/sv_button_orange_pressed.png').convert_alpha(), (button_width, button_height))
violet_button_pressed = pygame.transform.scale(pygame.image.load('assets/sv_button_violet_pressed.png').convert_alpha(), (button_width, button_height))
yellow_button_pressed = pygame.transform.scale(pygame.image.load('assets/sv_button_yellow_pressed.png').convert_alpha(), (button_width, button_height))

class Button():
    def __init__(self, x_position, y_position, image, image_pressed, text):
        self.image = image
        self.text = text
        self.image_pressed = image_pressed
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_position, y_position)

    FONT = pygame.font.SysFont('centuryschoolbook', math.ceil(SCREEN_WIDTH / 71))
    SMALL_FONT = pygame.font.SysFont('centuryschoolbook', math.ceil(SCREEN_WIDTH / 95))
    
    def detect_click(self, image, button_arr, slider_active):
        mouse_pos = pygame.mouse.get_pos()
        button_event = False
        other_button_clicked = False
        
        for i in range(len(button_arr)):
            if button_arr[i].clicked:
                other_button_clicked = True

        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked and not other_button_clicked and not slider_active:
                self.image = self.image_pressed
                self.clicked = True
                button_event = True
            
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
                self.image = image

        if not self.rect.collidepoint(mouse_pos):
            self.image = image

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        return button_event

    def change_color(self, new_color, new_color_pressed):
        self.image = new_color
        self.image_pressed = new_color_pressed

    def change_text(self, new_text):
        self.text = new_text

class Slider():
    LIGHT_GRAY = [192, 192, 192]
    DARK_GRAY = [128, 128, 128]
    
    def __init__(self, slider_vals):
        """
        self.border.rect.topleft = (border_vals[0], border_vals[1])
        self.border.width = border_vals[2]
        self.border.height = border_vals[3]
        self.border.color = border_vals[4]
        """
        self.origin = (slider_vals[0], slider_vals[1])
        self.width = slider_vals[2]
        self.height = slider_vals[3]
        self.min_val = slider_vals[4]
        self.max_val = slider_vals[5]
        self.starting_val = slider_vals[6]
        self.color = slider_vals[7]
        self.rect = pygame.Rect(self.origin, (self.width, self.height))

    def draw_border(self, border_vals):
        border_init_x, border_init_y, border_width, border_height, border_color = border_vals
        border = pygame.Rect(border_init_x, border_init_y, border_width, border_height)
        return border, border_color

    def detect_mouse(self, color, pressed_color):
        mouse_pos_x = pygame.mouse.get_pos()[0]
        mouse_pos_y = pygame.mouse.get_pos()[1]
        x_buffer = 10
        y_buffer = 10
        slider_move = False

        if self.rect.x - x_buffer < mouse_pos_x < self.rect.x + self.width + x_buffer and self.rect.y - y_buffer < mouse_pos_y < self.rect.y + self.height + y_buffer:
            if pygame.mouse.get_pressed()[0] == 1:
                self.color = pressed_color
                slider_move = True
            
            if pygame.mouse.get_pressed()[0] == 0:
                self.color = color
        else:
            self.color = color

        return slider_move

    def move_slider(self):
        self.rect.x = pygame.mouse.get_pos()[0] - self.width / 2

        if self.rect.x > self.max_val:
            self.rect.x = self.max_val
        elif self.rect.x < self.min_val:
            self.rect.x = self.min_val

    def slider_vals(self, border_init_x, border_width, min_val, max_val, is_time_slider):
        length_of_subdivisions = border_width / (max_val - min_val)
        current_slider_pos = math.ceil(self.rect.x - border_init_x)
        current_subdivision = math.ceil(current_slider_pos / length_of_subdivisions) + min_val
        
        if self.rect.x + self.width == math.floor(border_init_x + border_width):
            current_subdivision = math.ceil((current_slider_pos + self.width) / length_of_subdivisions) + min_val

        if self.rect.x + self.width == math.floor(border_init_x + border_width) and is_time_slider:
            current_subdivision = 0
        
        return current_subdivision




class DrawingInformation():
    # Constant color values (R, G, B)
    red_header_val = 0
    green_header_val = 255
    blue_header_val = 0

    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    RED = 255, 0, 0
    GREEN = 0, 255, 0
    PURPLE = 255, 0, 255
    BLUE = 0, 0, 255
    DARK_GRAY = 128, 128, 128
    GRAY = 160, 160, 160
    LIGHT_GRAY = 192, 192, 192
    BACKGROUND_COLOR = WHITE
    HEADER_COLOR = GREEN

    GRAY_SCALE = [
        DARK_GRAY,
        GRAY,
        LIGHT_GRAY
    ]

    FONT = pygame.font.SysFont('centuryschoolbook', math.ceil(SCREEN_WIDTH / 71))
    MEDIUM_FONT = pygame.font.SysFont('centuryschoolbook', 24)
    LARGE_FONT = pygame.font.SysFont('centuryschoolbook', 28)

    SIDE_PADDING = 100
    TOP_PADDING = HEADER_SIZE + 5

    # Constructor class for drawing value bars
    def __init__(self, width, height, list):
        self.width = width
        self.height = height
        
        # self.window = screen
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(list)

    def set_list(self, list):
        self.list = list
        self.min_val = min(list)
        self.max_val = max(list)

        self.block_width = (self.width - self.SIDE_PADDING) / len(list)
        self.block_height = math.floor((self.height - self.TOP_PADDING) / (self.max_val - self.min_val))
        self.starting_x = self.SIDE_PADDING // 2

    def change_header_color(self, r, g, b):
        self.HEADER_COLOR = r, g, b

def draw_to_screen(drawing, algorithm_name, ascending, button_arr, slider_arr, slider_border_arr, num_arr_vals, clock_speed, sort_page, help_clicked, red_val, green_val, blue_val):
    text_buffer = 2.1
    global time_counter
    
    screen.fill(drawing.BACKGROUND_COLOR)
    if not help_clicked:
        draw_values(drawing)
    else:
        draw_help(drawing, slider_arr, slider_border_arr, red_val, green_val, blue_val)
    pygame.draw.rect(screen, drawing.HEADER_COLOR, pygame.Rect(0, 0, SCREEN_WIDTH, HEADER_SIZE))

    for i in range(len(button_arr)):
        screen.blit(button_arr[i].image, (button_arr[i].rect.x, button_arr[i].rect.y))
        button_text = button_arr[i].FONT.render(button_arr[i].text, 1, drawing.BLACK)

        if (button_text.get_width() > button_width / 1.5):
            button_text = button_arr[i].SMALL_FONT.render(button_arr[i].text, 1, drawing.BLACK)

        screen.blit(button_text, ((2 * button_arr[i].rect.x + button_width) / 2 - button_text.get_width() / 2, (2 * button_arr[i].rect.y + button_height) / 2 - button_text.get_height() / 2))

    title = drawing.LARGE_FONT.render(f"{algorithm_name}: {'Ascending Order' if ascending else 'Descending Order'}", 1, drawing.BLACK)
    text_1 = button_arr[0].FONT.render(f"# of Items to Sort: {num_arr_vals}", 1, drawing.BLACK)
    text_2 = button_arr[0].FONT.render(f"Sorting Speed: {clock_speed if clock_speed != 0 else 'N/A'} FPS", 1, drawing.BLACK)
    current_page = button_arr[0].FONT.render(f"Current Sort Page: {sort_page}/4", 1, drawing.BLACK)
    arr_accesses = drawing.FONT.render(f"Array Accesses: {arr_access_counter}", 1, drawing.BLACK)

    if (time_counter < 1.0):
        timer = drawing.FONT.render(f"Time: {time_counter * 100} milliseconds", 1, drawing.BLACK)
    else:
        timer = drawing.FONT.render(f"Time: {time_counter} seconds", 1, drawing.BLACK)

    screen.blit(title, (drawing.width / 2 - title.get_width() / 2, 5))
    screen.blit(text_1, (slider_border_arr[0][0], slider_border_arr[0][1] - text_buffer * slider_border_arr[0][3]))
    screen.blit(text_2, (slider_border_arr[1][0], slider_border_arr[1][1] - text_buffer * slider_border_arr[1][3]))
    screen.blit(current_page, (0, 0))
    screen.blit(arr_accesses, (button_width, 0))
    screen.blit(timer, (button_width * 4, 0))

    pygame.draw.rect(screen, slider_arr[0].draw_border(slider_border_arr[0])[1], slider_arr[0].draw_border(slider_border_arr[0])[0])
    pygame.draw.rect(screen, slider_arr[0].color, slider_arr[0].rect)

    pygame.draw.rect(screen, slider_arr[1].draw_border(slider_border_arr[1])[1], slider_arr[1].draw_border(slider_border_arr[1])[0])
    pygame.draw.rect(screen, slider_arr[1].color, slider_arr[1].rect)

    """
    user_options = drawing.FONT.render("R - Reset | Space - Start Sorting | A - Ascending | D - Descending", 1, drawing.BLACK)
    screen.blit(user_options, (drawing.width / 2 - user_options.get_width() / 2, 35))

    sorting_options = drawing.FONT.render("I - Insertion Sort | B - Bubble Sort", 1, drawing.BLACK)
    screen.blit(sorting_options, (drawing.width / 2 - sorting_options.get_width() / 2, 65))
    """

    pygame.display.update()

def draw_values(drawing, colors={}, clear_background=False):
    global sorted_vals
    list = drawing.list

    if clear_background:
        clear_rectangle = (drawing.SIDE_PADDING // 2, drawing.TOP_PADDING + 50, 
        drawing.width - drawing.SIDE_PADDING, drawing.height - drawing.TOP_PADDING)

        pygame.draw.rect(screen, drawing.BACKGROUND_COLOR, clear_rectangle)
    

    for i, val in enumerate(list):
        current_x = drawing.starting_x + i * drawing.block_width
        current_y = drawing.height - (val - drawing.min_val) * drawing.block_height
        current_color = drawing.GRAY_SCALE[i % 3]
        
        if i in colors:
            current_color = colors[i]
        
        pygame.draw.rect(screen, current_color, (current_x, current_y, drawing.block_width, drawing.height))

    if clear_background:
        pygame.display.update()

def draw_help(drawing, slider_arr, slider_border_arr, red_val, green_val, blue_val):
    padding = 42
    text_buffer = 50
    value_buffer = 30
    
    header = drawing.LARGE_FONT.render("Keyboard Shortcuts", 1, drawing.BLACK)
    text0 = drawing.FONT.render("Press f to toggle full screen mode.", 1, drawing.BLACK)
    text1 = drawing.FONT.render("Press a to switch to ascending order or d to switch to descending order.", 1, drawing.BLACK)
    text2 = drawing.FONT.render("Press r to reset the list to be sorted.", 1, drawing.BLACK)
    text3 = drawing.FONT.render("Press the spacebar to run the most recently selected sort.", 1, drawing.BLACK)
    text4 = drawing.FONT.render("Press the grave key or 0-9 to change the color of the buttons.", 1, drawing.BLACK)
    text5 = drawing.FONT.render("Press q to reset the header background's color.", 1, drawing.BLACK)
    text6 = drawing.LARGE_FONT.render("Header Color", 1, drawing.BLACK)
    text7 = drawing.FONT.render(f"Red Value: {red_val}", 1, drawing.BLACK)
    text8 = drawing.FONT.render(f"Green Value: {green_val}", 1, drawing.BLACK)
    text9 = drawing.FONT.render(f"Blue Value: {blue_val}", 1, drawing.BLACK)
    # text5 = drawing.FONT.render("Press p or o to respectively increase or decrease the amount of red in the header background.", 1, drawing.BLACK)
    # text6 = drawing.FONT.render("Press l or k to respectively increase or decrease the amount of green in the header background.", 1, drawing.BLACK)
    # text7 = drawing.FONT.render("Press m or n to respectively increase or decrease the amount of blue in the header background.", 1, drawing.BLACK)

    screen.blit(header, (SCREEN_WIDTH / 2 - header.get_width() / 2, HEADER_SIZE + padding))
    screen.blit(text0, (SCREEN_WIDTH / 2 - text0.get_width() / 2, HEADER_SIZE + 2 * padding))
    screen.blit(text1, (SCREEN_WIDTH / 2 - text1.get_width() / 2, HEADER_SIZE + 3 * padding))
    screen.blit(text2, (SCREEN_WIDTH / 2 - text2.get_width() / 2, HEADER_SIZE + 4 * padding))
    screen.blit(text3, (SCREEN_WIDTH / 2 - text3.get_width() / 2, HEADER_SIZE + 5 * padding))
    screen.blit(text4, (SCREEN_WIDTH / 2 - text4.get_width() / 2, HEADER_SIZE + 6 * padding))
    screen.blit(text5, (SCREEN_WIDTH / 2 - text5.get_width() / 2, HEADER_SIZE + 7 * padding))
    screen.blit(text6, (SCREEN_WIDTH / 2 - text6.get_width() / 2, HEADER_SIZE + 9 * padding - text_buffer))
    screen.blit(text7, (SCREEN_WIDTH / 2 - text7.get_width() / 2, slider_border_arr[2][1] - value_buffer))
    screen.blit(text8, (SCREEN_WIDTH / 2 - text8.get_width() / 2, slider_border_arr[3][1] - value_buffer))
    screen.blit(text9, (SCREEN_WIDTH / 2 - text9.get_width() / 2, slider_border_arr[4][1] - value_buffer))

    pygame.draw.rect(screen, slider_arr[2].draw_border(slider_border_arr[2])[1], slider_arr[2].draw_border(slider_border_arr[2])[0])
    pygame.draw.rect(screen, slider_arr[2].color, slider_arr[2].rect)
    
    pygame.draw.rect(screen, slider_arr[3].draw_border(slider_border_arr[3])[1], slider_arr[3].draw_border(slider_border_arr[3])[0])
    pygame.draw.rect(screen, slider_arr[3].color, slider_arr[3].rect)

    pygame.draw.rect(screen, slider_arr[4].draw_border(slider_border_arr[4])[1], slider_arr[4].draw_border(slider_border_arr[4])[0])
    pygame.draw.rect(screen, slider_arr[4].color, slider_arr[4].rect)

    # pygame.draw.rect(screen, slider.draw_border(slider_border_arr)[1], slider.draw_border(slider_border_arr)[0])
    # pygame.draw.rect(screen, slider.color, slider.rect)


def reset_list(num_vals, min_val, max_val):
    list = []

    for _ in range(num_vals):
        val = random.randint(min_val, max_val)
        list.append(val)

    return list


def main():
    running = True
    fullscreen = False
    clock = pygame.time.Clock()
    clock_time = 0
    clock_min_speed = 10
    clock_max_speed = 600
    is_time_slider = False

    num_vals = 5
    min_val = 0
    max_val = 500
    min_items = 5
    max_items = 500

    red_val = 0
    green_val = 255
    blue_val = 0
    color_val_arr = [red_val, green_val, blue_val]

    list = reset_list(num_vals, min_val, max_val)
    drawing = DrawingInformation(SCREEN_WIDTH, SCREEN_HEIGHT, list)
    
    sorting = False
    ascending = True
    help_clicked = False

    sort_selected = False
    sorting_algorithm = bubble_sort
    algorithm_name = "Bubble Sort"
    algorithm_generator = None

    init_pos_y = 28
    button_spacing_x = 1.8
    add_horizontal = button_width + button_spacing_x
    vertical_increase_factor = 1.3
    add_vertical = button_height / vertical_increase_factor

    current_button_color = light_blue_button
    current_button_pressed_color = light_blue_button_pressed

    button_1 = Button(0, init_pos_y, current_button_color, current_button_pressed_color, "Bubble Sort")
    button_2 = Button(button_1.rect.x + add_horizontal, init_pos_y, current_button_color, current_button_pressed_color, "Selection Sort")
    button_3 = Button(button_2.rect.x + add_horizontal, init_pos_y, current_button_color, current_button_pressed_color, "Insertion Sort")
    button_4 = Button(button_3.rect.x + add_horizontal, init_pos_y, current_button_color, current_button_pressed_color, "More Sorts")
    button_5 = Button(button_4.rect.x + add_horizontal, init_pos_y, current_button_color, current_button_pressed_color, "Reset")
    button_6 = Button(0, button_1.rect.y + add_vertical, current_button_color, current_button_pressed_color, "Merge Sort")
    button_7 = Button(button_1.rect.x + add_horizontal, button_1.rect.y + add_vertical, current_button_color, current_button_pressed_color, "Quick Sort")
    button_8 = Button(button_2.rect.x + add_horizontal, button_1.rect.y + add_vertical, current_button_color, current_button_pressed_color, "Heap Sort")
    button_9 = Button(button_3.rect.x + add_horizontal, button_1.rect.y + add_vertical, current_button_color, current_button_pressed_color, "Descending Order")
    button_10 = Button(button_4.rect.x + add_horizontal, button_1.rect.y + add_vertical, current_button_color, current_button_pressed_color, "Help")
    
    options_arr = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_10]

    sort_page = 1

    button_padding_x = 10
    button_padding_y = 27

    border_width = button_width
    border_height = 15
    border_color = drawing.GRAY

    border_init_x = button_5.rect.x + add_horizontal - button_padding_x
    border_init_y = init_pos_y + button_padding_y

    border_init_x_2 = button_10.rect.x + add_horizontal - button_padding_x
    border_init_y_2 = button_1.rect.y + add_vertical + button_padding_y

    red_border_init_x = SCREEN_WIDTH / 2 - border_width / 2
    red_border_init_y = math.floor(SCREEN_HEIGHT * 0.75)

    green_border_init_x = red_border_init_x
    green_border_init_y = red_border_init_y + add_vertical

    blue_border_init_x = red_border_init_x
    blue_border_init_y = green_border_init_y + add_vertical
    
    slider_width = 10
    slider_height = border_height * 2
    slider_color = drawing.LIGHT_GRAY
    slider_offset_y = slider_height / 4

    slider_x = border_init_x
    slider_y = border_init_y - slider_offset_y
    slider_min_val = border_init_x
    slider_max_val = border_init_x + border_width - slider_width
    slider_starting_val = 30

    slider_x_2 = border_init_x_2
    slider_y_2 = border_init_y_2 - slider_offset_y
    slider_min_val = border_init_x_2
    slider_max_val = border_init_x_2 + border_width - slider_width
    slider_starting_val_2 = 60

    red_slider_x = red_border_init_x
    red_slider_y = red_border_init_y - slider_offset_y
    red_slider_min_val = red_border_init_x
    red_slider_max_val = red_border_init_x + border_width - slider_width
    red_slider_start_val = 0
    
    green_slider_x = green_border_init_x + border_width - slider_width
    green_slider_y = green_border_init_y - slider_offset_y
    green_slider_min_val = green_border_init_x
    green_slider_max_val = green_border_init_x + border_width - slider_width
    green_slider_start_val = 0

    blue_slider_x = blue_border_init_x
    blue_slider_y = blue_border_init_y - slider_offset_y
    blue_slider_min_val = blue_border_init_x
    blue_slider_max_val = blue_border_init_x + border_width - slider_width
    blue_slider_start_val = 0

    border_vals = [border_init_x, border_init_y, border_width, border_height, border_color]
    border_vals_2 = [border_init_x_2, border_init_y_2, border_width, border_height, border_color]
    slider_vals = [slider_x, slider_y, slider_width, slider_height, slider_min_val, slider_max_val, slider_starting_val, slider_color]
    slider_vals_2 = [slider_x_2, slider_y_2, slider_width, slider_height, slider_min_val, slider_max_val, slider_starting_val_2, slider_color]
    red_border_vals = [red_border_init_x, red_border_init_y, border_width, border_height, border_color]
    red_slider_vals = [red_slider_x, red_slider_y, slider_width, slider_height, red_slider_min_val, red_slider_max_val, red_slider_start_val, slider_color]
    green_border_vals = [green_border_init_x, green_border_init_y, border_width, border_height, border_color]
    green_slider_vals = [green_slider_x, green_slider_y, slider_width, slider_height, green_slider_min_val, green_slider_max_val, green_slider_start_val, slider_color]
    blue_border_vals = [blue_border_init_x, blue_border_init_y, border_width, border_height, border_color]
    blue_slider_vals = [blue_slider_x, blue_slider_y, slider_width, slider_height, blue_slider_min_val, blue_slider_max_val, blue_slider_start_val, slider_color]
    
    slider = Slider(slider_vals)
    time_slider = Slider(slider_vals_2)
    red_slider = Slider(red_slider_vals)
    green_slider = Slider(green_slider_vals)
    blue_slider = Slider(blue_slider_vals)

    slider_arr = [slider, time_slider, red_slider, green_slider, blue_slider]
    slider_border_arr = [border_vals, border_vals_2, red_border_vals, green_border_vals, blue_border_vals]

    slider_active = False

    def reset_button_colors(button_arr, new_color, new_color_pressed):
        for i in range(len(button_arr)):
            button_arr[i].change_color(new_color, new_color_pressed)

    def button_clicks(algorithm, algo_name, algo_generator, sorting, sort_page, ascending, help_clicked, button_arr, slider_active):
        clicked_sort = False

        button_clicked_1 = button_1.detect_click(current_button_color, button_arr, slider_active)
        button_clicked_2 = button_2.detect_click(current_button_color, button_arr, slider_active)
        button_clicked_3 = button_3.detect_click(current_button_color, button_arr, slider_active)
        button_clicked_5 = button_5.detect_click(current_button_color, button_arr, slider_active)
        button_clicked_6 = button_6.detect_click(current_button_color, button_arr, slider_active)
        button_clicked_7 = button_7.detect_click(current_button_color, button_arr, slider_active)
        button_clicked_8 = button_8.detect_click(current_button_color, button_arr, slider_active)
        button_clicked_9 = button_9.detect_click(current_button_color, button_arr, slider_active)
        button_clicked_10 = button_10.detect_click(current_button_color, button_arr, slider_active)

        if button_clicked_1 and not help_clicked:
            clicked_sort = True
            reset_access_counter()
            reset_time_counter()

            if sort_page == 1:
                algorithm = bubble_sort
                algo_name = "Bubble Sort"
            elif sort_page == 2:
                algorithm = counting_sort
                algo_name = "Counting Sort"
            elif sort_page == 3:
                algorithm = pigeonhole_sort
                algo_name = "Pigeonhole Sort"
            elif sort_page == 4:
                algorithm = cube_sort
                algo_name = "Cube Sort"

        if button_clicked_2 and not help_clicked:
            clicked_sort = True
            reset_access_counter()
            reset_time_counter()
            
            if sort_page == 1:
                algorithm = selection_sort
                algo_name = "Selection Sort"
            elif sort_page == 2:
                algorithm = radix_sort
                algo_name = "Radix Sort"
            elif sort_page == 3:
                algorithm = cycle_sort
                algo_name = "Cycle Sort"
            elif sort_page == 4:
                algorithm = brick_sort
                algo_name = "Brick Sort"

        if button_clicked_3 and not help_clicked:
            clicked_sort = True
            reset_access_counter()
            reset_time_counter()
            
            if sort_page == 1:
                algorithm = insertion_sort
                algo_name = "Insertion Sort"
            elif sort_page == 2:
                algorithm = bucket_sort
                algo_name = "Bucket Sort"
            elif sort_page == 3:
                algorithm = cocktail_sort
                algo_name = "Cocktail Sort"
            elif sort_page == 4:
                algorithm = stooge_sort
                algo_name = "Stooge Sort"

        if button_clicked_5:
            reset_access_counter()
            reset_time_counter()
            list = reset_list(num_vals, min_val, max_val)
            drawing.set_list(list)
            sorting = False

        if button_clicked_6 and not help_clicked:
            clicked_sort = True
            reset_access_counter()
            reset_time_counter()
            
            if sort_page == 1:
                algorithm = merge_sort
                algo_name = "Merge Sort"
            elif sort_page == 2:
                algorithm = shell_sort
                algo_name = "Shell Sort"
            elif sort_page == 3:
                algorithm = strand_sort
                algo_name = "Strand Sort"
            elif sort_page == 4:
                algorithm = slow_sort
                algo_name = "Slow Sort"

        if button_clicked_7 and not help_clicked:
            clicked_sort = True
            reset_access_counter()
            reset_time_counter()
            
            if sort_page == 1:
                algorithm = quick_sort
                algo_name = "Quick Sort"
            elif sort_page == 2:
                algorithm = tim_sort
                algo_name = "Tim Sort"
            elif sort_page == 3:
                algorithm = bitonic_sort
                algo_name = "Bitonic Sort"
            elif sort_page == 4:
                algorithm = tree_sort
                algo_name = "Tree Sort"

        if button_clicked_8 and not help_clicked:
            clicked_sort = True
            reset_access_counter()
            reset_time_counter()
            
            if sort_page == 1:
                algorithm = heap_sort
                algo_name = "Heap Sort"
            elif sort_page == 2:
                algorithm = comb_sort
                algo_name = "Comb Sort"
            elif sort_page == 3:
                algorithm = gnome_sort
                algo_name = "Gnome Sort"
            elif sort_page == 4:
                algorithm = bogo_sort
                algo_name = "Bogo Sort"

        if button_clicked_9:
            ascending = not ascending

            if (ascending):
                button_9.change_text("Descending Order")
            else:
                button_9.change_text("Ascending Order")

        if button_clicked_10:
            help_clicked = not help_clicked

            if not help_clicked:
                reset_access_counter()
                reset_time_counter()
                list = reset_list(num_vals, min_val, max_val)
                drawing.set_list(list)
                
            sorting = False

        return algorithm, algo_name, algo_generator, sorting, ascending, help_clicked, clicked_sort

    def more_sorts(sort_page, button_arr, slider_active):
        button_clicked_4 = button_4.detect_click(current_button_color, button_arr, slider_active)
        if button_clicked_4:
            if sort_page == 1:
                button_1.change_text("Counting Sort")
                button_2.change_text("Radix Sort")
                button_3.change_text("Bucket Sort")
                button_6.change_text("Shell Sort")
                button_7.change_text("Tim Sort")
                button_8.change_text("Comb Sort")
                sort_page += 1
            elif sort_page == 2:
                button_1.change_text("Pigeonhole Sort")
                button_2.change_text("Cycle Sort")
                button_3.change_text("Cocktail Sort")
                button_6.change_text("Strand Sort")
                button_7.change_text("Bitonic Sort")
                button_8.change_text("Gnome Sort")
                sort_page += 1
            elif sort_page == 3:
                button_1.change_text("Cube Sort")
                button_2.change_text("Brick Sort")
                button_3.change_text("Stooge Sort")
                button_6.change_text("Slow Sort")
                button_7.change_text("Tree Sort")
                button_8.change_text("Bogo Sort")
                sort_page += 1
            elif sort_page == 4:
                button_1.change_text("Bubble Sort")
                button_2.change_text("Selection Sort")
                button_3.change_text("Insertion Sort")
                button_6.change_text("Merge Sort")
                button_7.change_text("Quick Sort")
                button_8.change_text("Heap Sort")
                sort_page = 1
        return sort_page

    def run_sort(algo_generator, sorting):
        sorting = True
        algo_generator = sorting_algorithm(drawing, ascending)
        return algo_generator, sorting

    while running:
        clock.tick(clock_time)
        sorting_algorithm, algorithm_name, algorithm_generator, sorting, ascending, help_clicked, sort_selected = button_clicks(
            sorting_algorithm, algorithm_name, algorithm_generator, sorting, sort_page, ascending, help_clicked, options_arr, slider_active)
        sort_page = more_sorts(sort_page, options_arr, slider_active)
        
        slider_can_move = slider.detect_mouse(slider.LIGHT_GRAY, slider.DARK_GRAY)
        time_slider_can_move = time_slider.detect_mouse(time_slider.LIGHT_GRAY, time_slider.DARK_GRAY)
        red_slider_can_move = red_slider.detect_mouse(red_slider.LIGHT_GRAY, red_slider.DARK_GRAY)
        green_slider_can_move = green_slider.detect_mouse(green_slider.LIGHT_GRAY, green_slider.DARK_GRAY)
        blue_slider_can_move = blue_slider.detect_mouse(blue_slider.LIGHT_GRAY, blue_slider.DARK_GRAY)
        slider_active = slider_can_move or time_slider_can_move or red_slider_can_move or green_slider_can_move or blue_slider_can_move

        drawing.HEADER_COLOR = red_val, green_val, blue_val

        if slider_can_move:
            is_time_slider = False
            num_vals = slider.slider_vals(border_init_x, border_width, min_items, max_items, is_time_slider)
            list = reset_list(num_vals, min_val, max_val)
            drawing.set_list(list)
            clock.tick(35)

        if time_slider_can_move:
            is_time_slider = True
            clock_time = time_slider.slider_vals(border_init_x_2, border_width, clock_min_speed, clock_max_speed, is_time_slider)
            clock.tick(35)

        if red_slider_can_move:
            is_time_slider = False
            red_val = red_slider.slider_vals(red_border_init_x, border_width, 0, 255, is_time_slider)

        if green_slider_can_move:
            is_time_slider = False
            green_val = green_slider.slider_vals(green_border_init_x, border_width, 0, 255, is_time_slider)

        if blue_slider_can_move:
            is_time_slider = False
            blue_val = blue_slider.slider_vals(blue_border_init_x, border_width, 0, 255, is_time_slider)

        if sorting:
            try:
                next(algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            if slider_can_move:
                slider.move_slider()
            
            if time_slider_can_move:
                time_slider.move_slider()

            if red_slider_can_move:
                red_slider.move_slider()
            
            if green_slider_can_move:
                green_slider.move_slider()

            if blue_slider_can_move:
                blue_slider.move_slider()

            draw_to_screen(drawing, algorithm_name, ascending, options_arr, slider_arr, slider_border_arr, num_vals, clock_time, sort_page, help_clicked, red_val, green_val, blue_val)

        if sort_selected:
            algorithm_generator, sorting = run_sort(algorithm_generator, sorting)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                reset_access_counter()
                reset_time_counter()
                list = reset_list(num_vals, min_val, max_val)
                drawing.set_list(list)
                sorting = False

            elif event.key == pygame.K_SPACE and not sorting and not help_clicked:
                sorting = True
                algorithm_generator = sorting_algorithm(drawing, ascending)

            elif event.key == pygame.K_a and not sorting:
                ascending = True
                button_9.change_text("Descending Order")

            elif event.key == pygame.K_d and not sorting:
                ascending = False
                button_9.change_text("Ascending Order")

            elif event.key == pygame.K_1:
                current_button_color = red_button
                current_button_pressed_color = red_button_pressed
                reset_button_colors(options_arr, current_button_color, current_button_pressed_color)

            elif event.key == pygame.K_2:
                current_button_color = blue_button
                current_button_pressed_color = blue_button_pressed
                reset_button_colors(options_arr, current_button_color, current_button_pressed_color)

            elif event.key == pygame.K_3:
                current_button_color = brown_button
                current_button_pressed_color = brown_button_pressed
                reset_button_colors(options_arr, current_button_color, current_button_pressed_color)
            elif event.key == pygame.K_4:
                current_button_color = dark_green_button
                current_button_pressed_color = dark_green_button_pressed
                reset_button_colors(options_arr, current_button_color, current_button_pressed_color)

            elif event.key == pygame.K_5:
                current_button_color = gray_button
                current_button_pressed_color = gray_button_pressed
                reset_button_colors(options_arr, current_button_color, current_button_pressed_color)

            elif event.key == pygame.K_6:
                current_button_color = light_green_button
                current_button_pressed_color = light_green_button_pressed
                reset_button_colors(options_arr, current_button_color, current_button_pressed_color)

            elif event.key == pygame.K_7:
                current_button_color = maroon_button
                current_button_pressed_color = maroon_button_pressed
                reset_button_colors(options_arr, current_button_color, current_button_pressed_color)

            elif event.key == pygame.K_8:
                current_button_color = orange_button
                current_button_pressed_color = orange_button_pressed
                reset_button_colors(options_arr, current_button_color, current_button_pressed_color)

            elif event.key == pygame.K_9:
                current_button_color = violet_button
                current_button_pressed_color = violet_button_pressed
                reset_button_colors(options_arr, current_button_color, current_button_pressed_color)

            elif event.key == pygame.K_0:
                current_button_color = yellow_button
                current_button_pressed_color = yellow_button_pressed
                reset_button_colors(options_arr, current_button_color, current_button_pressed_color)

            elif event.key == pygame.K_BACKQUOTE:
                current_button_color = light_blue_button
                current_button_pressed_color = light_blue_button_pressed
                reset_button_colors(options_arr, current_button_color, current_button_pressed_color)
            elif event.key == pygame.K_f:
                if not fullscreen:
                    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
                    fullscreen = True
                else:
                    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                    fullscreen = False
            elif event.key == pygame.K_q:
                red_val = drawing.red_header_val
                green_val = drawing.green_header_val
                blue_val = drawing.blue_header_val
            """
            elif slider.get_mouse_x(slider.LIGHT_GRAY, slider.DARK_GRAY) > slider_mouse_x or event.key == pygame.K_RIGHT:
                moving_left = False
                slider.move_slider(slider_movement, moving_left)
            elif slider.get_mouse_x(slider.LIGHT_GRAY, slider.DARK_GRAY) < slider_mouse_x or event.key == pygame.K_LEFT:
                moving_left = True
                slider.move_slider(slider_movement, moving_left)
            """
    
    pygame.quit()

def array_accesses():
    global arr_access_counter
    arr_access_counter += 1

def reset_access_counter():
    global arr_access_counter
    arr_access_counter = 0

def reset_time_counter():
    global time_counter
    time_counter = 0

def bubble_sort(drawing, ascending):
    start = time.time()
    array = drawing.list
    sort_length = len(array) - 1

    for i in range(sort_length):
        # The largest value not already sorted will be sorted by the end of the next iteration of
        # i, so after i iterations we need to sort through i less values, thus "sort_length - i"
        for j in range(0, sort_length - i): 
            if (array[j] > array[j + 1] and ascending or array[j] < array[j + 1] and not ascending):
                array[j], array[j + 1] = array[j + 1], array[j]
                draw_values(drawing, {j: drawing.GREEN, j + 1: drawing.RED}, True)
                array_accesses()
                yield True
    
    end = time.time()

    global time_counter
    time_counter = float("{:.5f}".format(end - start))
    return array

def selection_sort(drawing, ascending):
    start = time.time()
    array = drawing.list
    
    for i in range(len(array)):
        min_position = i

        for j in range(i, len(array)):
            if (array[min_position] > array[j] and ascending or array[min_position] < array[j] and not ascending):
                min_position = j
            array_accesses()
        
        array[i], array[min_position] = array[min_position], array[i]
        draw_values(drawing, {i: drawing.GREEN, min_position: drawing.RED}, True)
        yield True

    end = time.time()

    global time_counter
    time_counter = float("{:.5f}".format(end - start))
    return array

def insertion_sort():
    test = "do later"

def merge_sort():
    test = "do later"

def quick_sort():
    test = "do later"

def heap_sort():
    test = "do later"

def counting_sort():
    test = "do later"

def radix_sort():
    test = "do later"

def bucket_sort():
    test = "do later"

def shell_sort():
    test = "do later"

def tim_sort():
    test = "do later"

def comb_sort():
    test = "do later"

def pigeonhole_sort():
    test = "do later"

def cycle_sort():
    test = "do later"

def cocktail_sort():
    test = "do later"

def strand_sort():
    test = "do later"

def bitonic_sort():
    test = "do later"

def gnome_sort():
    test = "do later"

def cube_sort():
    test = "do later"

def brick_sort():
    test = "do later"

def stooge_sort():
    test = "do later"

def slow_sort():
    test = "do later"

def tree_sort():
    test = "do later"

def bogo_sort():
    test = "do later"

if __name__ == "__main__":
    main()