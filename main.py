





# connect the main python file with all the secondary files
from photo import photo
from split import split
from merge import merge
from merge import execute
from detect import detect, give
from tables import tables



# The Libraries we are going to use
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)


pygame_icon= pygame.image.load('data/icon.png')
pygame.display.set_icon(pygame_icon)


# func variable changes according to which action is selected
func = 0
# Start variable helps inside the ruuning loop
start = True


file = ""
times = 0
flag_tables = True


# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('PDF editor')

# Load images
image_files = ['data/photo1.png', 'data/photo2.png', 'data/photo3.png', 'data/photo4.png', 'data/photo5.png']
images = [pygame.image.load(image).convert_alpha() for image in image_files]

# Set image positions (arranging them horizontally)
image_positions = [
    (50, 300),
    (200, 300),
    (350, 300),
    (500, 300),
    (650, 300)
]

# Variable to change based on the image clicked
clicked_image_index = -1


# call_text function is used when we want to display text in pygame's screen
def call_text(tx,wdt):
    screen.fill(WHITE)
    font = pygame.font.Font(None, 36)
    text = font.render(tx, True, (0, 0, 0))
    screen.blit(text, (SCREEN_WIDTH // 2 - wdt, 200))

# call_text_lines use is the same with the previous function, but it is used if only a specific action is completed(you can see it below)
def call_text_lines(tx):
    font = pygame.font.Font(None, 28)
    text = font.render(tx, True, (0, 0, 0))
    screen.blit(text, (SCREEN_WIDTH // 50 , 250))




# this function checks wether any of the given iamges is selected(image = action)
def check_image_click(pos):
    global clicked_image_index
    for idx, (image, img_pos) in enumerate(zip(images, image_positions)):
        rect = pygame.Rect(img_pos[0], img_pos[1], image.get_width(), image.get_height())
        if rect.collidepoint(pos):
            clicked_image_index = idx + 1  # Image index starts at 1
            #print(f"Image {clicked_image_index} clicked!")

# Main game loop



running = True
while running:
    screen.fill(WHITE)

    # Draw the images
    if start:
        call_text("Select an action:",100)
        for image, pos in zip(images, image_positions):
            screen.blit(image, pos)
    # This if is checking whether an action has ended(start = false). In this case the right text is displayed
    if not start:
        if func == 1:
            call_text("PDF is created!",100)
        if func == 2:
            call_text("PDF files are created",120)
        if func == 3:
            call_text("Files successfully merged(directory of the program)",310)
        if func == 4:
            call_text("This word was detected " + str(times) + " times inside the PDF file", 300)
            if times > 0:
                call_text_lines("Find the exact lines the word was detected inside lines.txt(directory of the program)")
        if func == 5:
            if flag_tables == True:
                call_text("No tables found!",100)
            else:
                call_text("Tables are extracted inside tables.txt(directory of the program)",370)
        pygame.display.update()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and start:  # Left click
            mouse_pos = pygame.mouse.get_pos()
            check_image_click(mouse_pos)




    # Case one(image 1)
    if clicked_image_index == 1:
        func = 1
        call_text("Select an Image", 100)
        pygame.display.flip()
        photo()
        clicked_image_index =-1
        start = False



    # Case two(image 2)
    if clicked_image_index == 2:
        func = 2
        call_text("Select a PDF file",90)
        pygame.display.flip()
        split()
        clicked_image_index = -1
        start = False

    # Case 3(image 3)
    if clicked_image_index == 3:
        func = 3
        width, height = 800, 600
        screen = pygame.display.set_mode((width, height))


        # Define colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

        # Set up fonts
        font = pygame.font.Font(None, 48)
        small_font = pygame.font.Font(None, 36)

        # Instructions and variables
        input_text = ''
        instruction_text = "How many files do you want to merge ?:"


        running = True
        enter_pressed = False
        while running:
            screen.fill(WHITE)

            # Display the instruction text
            instruction_surface = small_font.render(instruction_text, True, BLACK)
            screen.blit(instruction_surface, (20, 20))

            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

                # Print the pressed keys on the screen
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # If enter is pressed
                        enter_pressed = True
                    elif event.key == pygame.K_BACKSPACE:  # To handle backspace
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode  # Append the character typed

            # Render the input text
            input_surface = font.render(input_text, True, BLACK)
            screen.blit(input_surface, (20, 100))


            if enter_pressed:
                if input_text.isdigit():
                    files_list = []
                    screen.fill(WHITE)  # Clear screen
                    message = input_text
                    surface = font.render(message, True, BLACK)
                    screen.blit(surface, (20, height // 2))
                    # Handle file inputs
                    for i in range(int(input_text)):
                        screen.fill(WHITE)
                        message = 'Give file ' +  str(i + 1)
                        surface = font.render(message, True, BLACK)
                        screen.blit(surface, (300, 200))
                        pygame.display.flip()
                        print(i)
                        files_list.append(merge(i))
                    execute(files_list)
                    clicked_image_index = -1
                    input_text =""
                    start = False
                    break

                else:
                    clicked_image_index = -1


            pygame.display.flip()



    # Case four(image 4)
    if clicked_image_index == 4:
        call_text("Select a PDF file", 90)
        pygame.display.flip()
        func = 4
        file = give()
        width, height = 800, 600
        screen = pygame.display.set_mode((width, height))
        message = ""
        # Define colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

        # Set up fonts
        font = pygame.font.Font(None, 48)
        small_font = pygame.font.Font(None, 36)

        # Instructions and variables
        input_text = ''
        instruction_text = "Give the word you want to search for?:"

        # Main loop
        running = True
        enter_pressed = False
        while running:
            screen.fill(WHITE)

            # Display the instruction text
            instruction_surface = small_font.render(instruction_text, True, BLACK)
            screen.blit(instruction_surface, (20, 20))

            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

                # Print the pressed keys on the screen
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # If enter is pressed
                        enter_pressed = True
                    elif event.key == pygame.K_BACKSPACE:  # To handle backspace
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode  # Append the character typed

            # Render the input text
            input_surface = font.render(input_text, True, BLACK)
            screen.blit(input_surface, (20, 100))


            if enter_pressed:
                if not input_text.isdigit():
                    files_list = []
                    screen.fill(WHITE)  # Clear screen
                    message = input_text
                    surface = font.render(message, True, BLACK)
                    screen.blit(surface, (20, height // 2))
                    break
            pygame.display.flip()

        # Conduct the word search
        times = detect(file, message)
        print(times)
        clicked_image_index = -1
        start = False




    # Case five(image 5)
    if clicked_image_index == 5:
        func = 5
        call_text("Select a PDF file", 90)
        pygame.display.flip()
        flag_tables = tables()
        clicked_image_index = -1
        start = False








    # Update display
    pygame.display.flip()
# Clean up Pygame
pygame.quit()











