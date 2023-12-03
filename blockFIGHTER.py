# Import necessary modules
import pygame # for game engine
import sys # for quitting the game
import time
import random

# Initialize game engine
pygame.init()


# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])

# Set title and icon
pygame.display.set_caption("BLOCK Fight") # sets the title of the game window
#icon = pygame.image.load('icon.png') # loads the game icon
#pygame.display.set_icon(icon) # sets the game icon




# Set up game loop
running = True # variable to control the game loop

# Set up level tracking variable
current_level = 1


# Set up player and enemy stick figures
player_x = 100
player_y = 500
player_width = 100
player_height = 100
player_punching = False
player_health = 100 # initialize player health to 100

enemy_x = 600
enemy_y = 500
enemy_width = 100
enemy_height = 100
enemy_health = 100 # initialize enemy health to 100

# Set up timer for enemy movement
last_move_time = time.time()
move_delay = 10 # delay of 1 second between enemy moves

# Set the minimum distance between the player and enemy
min_distance = 50
move_units = 30

# Set up font for displaying health
font = pygame.font.Font(None, 30) # create a font object

# Set up font for displaying story
star_wars_font = pygame.font.Font(None, 30) # create a font object
# Set the maximum width for the text
max_width = 500

    # Set up story lines
story_lines = [
    "A long time ago in a galaxy far, far away...",
    "Two blocks hated each other.",
    "Beat the heck outta this other block",
    "Before it beats you.",
    "There is no end.",
    "Just beat this block as many times as you can.",
    "Give up at supper time."
]

# Display intro story
for line in story_lines:
    
     # Clear screen
    screen.fill((0, 0, 0))
    # Wrap text to the specified width
    # Wrap text to the specified width
    wrapped_text = "" # initialize wrapped text as an empty string
    words = line.split(" ") # split text into words
    current_line = "" # initialize current line as an empty string
    for word in words:
        # Check if adding the current word to the current line would exceed the maximum width
        if star_wars_font.size(current_line + " " + word)[0] > max_width:
            # If adding the word would exceed the maximum width, add a line break to the wrapped text
            wrapped_text += current_line + "\n"
            current_line = word # reset the current line to the current word
        else:
            # If adding the word would not exceed the maximum width, add the word to the current line
            current_line += " " + word
    # Add the last line of text to the wrapped text
    wrapped_text += current_line

    # Create text label for current story line
    story_label = star_wars_font.render(wrapped_text, 1, (255, 255, 255))

   # Draw current story line on screen
    screen.blit(story_label, (screen_width / 2 - max_width / 2, screen_height / 2))

    # Update screen
    pygame.display.flip()

    # Add delay to slow down story pacing
    time.sleep(2)

while running:
    for event in pygame.event.get(): # checks for events (e.g. quitting the game)
        if event.type == pygame.QUIT: # if the event is to quit the game
            running = False # stop the game loop
        elif event.type == pygame.KEYDOWN: # if the event is a key press
            if event.key == pygame.K_SPACE: # if the key is the space bar
                player_punching = not player_punching # toggle the player punching animation

                # Check if enemy is within range of player's punch
                if (player_x + player_width / 2) > enemy_x and (player_x + player_width / 2) < (enemy_x + enemy_width):
                    # Punch enemy
                    enemy_health -= 10 # subtract 10 from enemy health

            elif event.key == pygame.K_LEFT: # if the key is the left arrow key
                player_x -= move_units # move the player 10 pixels to the left
            elif event.key == pygame.K_RIGHT: # if the key is the right arrow key
                player_x += move_units # move the player 10 pixels to the right
            elif event.key == pygame.K_UP: # if the key is the up arrow key
                player_y -= move_units # move the player 10 pixels up
            elif event.key == pygame.K_DOWN: # if the key is the down arrow key
                player_y += move_units # move the player 10 pixels down
            elif event.key == pygame.K_r: # if the key is the "r" key
                player_x = 100 # reset the player's x position to 100
                player_y = 500 # reset the player's y position to 500
            #Freeze enemy code
            elif event.key == pygame.K_F:
                enemy_freeze_start_time = time.time() # start the enemy freeze timer
                while time.time() - enemy_freeze_start_time < 3:
                    # Do not update the enemy's position while it is frozen
                    continue
   
   

   
    
    # Clear screen
    screen.fill((0, 0, 0)) # fill the screen with black

    #add drawings after the clear screen






    # Create text label for current level
    level_label = font.render("Level " + str(current_level), 1, (255, 255, 255))

    # Draw current level label on screen
    screen.blit(level_label, (screen_width / 2 - 50, 20))

    # Create text labels for minimum distance and move delay
    min_distance_label = font.render("Min Distance: " + str(min_distance), 1, (255, 255, 255))
    move_delay_label = font.render("Move Delay: " + str(move_delay), 1, (255, 255, 255))
    move_units_label = font.render("Move Units: " + str(move_units), 1, (255, 255, 255))


    # Draw minimum distance and move delay labels on screen
    screen.blit(min_distance_label, (screen_width - 200, 20))
    screen.blit(move_delay_label, (screen_width - 200, 40))
    screen.blit(move_units_label, (screen_width - 200, 60))

    # Draw stick figures
    pygame.draw.rect(screen, (255, 255, 255), (player_x, player_y, player_width, player_height)) # Player
    pygame.draw.rect(screen, (255, 255, 255), (enemy_x, enemy_y, enemy_width, enemy_height)) # Enemy

    # Draw health bars
    player_health_label = font.render(str(player_health), 1, (255, 255, 255)) # create text label for player health
    screen.blit(player_health_label, (player_x, player_y - 20)) # draw player health label

    enemy_health_label = font.render(str(enemy_health), 1, (255, 255, 255)) # create text label for enemy health
    screen.blit(enemy_health_label, (enemy_x, enemy_y - 20)) # draw enemy health label


    # Update player position
    if player_punching:
        player_width = 200 # double the width of the player stick figure to show the punching animation
        # Update display
        pygame.display.flip() # update the display to show the new frame
    else:
        player_width = 100
        # Update display
        pygame.display.flip() # update the display to show the new frame

    #MOVE THE ENEMY RANDOMLY AROUND THE SCREEN
    # Generate a random x and y coordinate
   # x = random.randint(0, screen_width)
    #y = random.randint(0, screen_height)

    # Check if player is off the screen
    if player_x < 0:
        player_x = 0 # set player's x coordinate to 0
    elif player_x > screen_width - player_width:
        player_x = screen_width - player_width # set player's x coordinate to the right edge of the screen
    
#start
    # Generate a random x coordinate that is outside the minimum distance from the player's x position
    if player_x < min_distance:
        # Player is within min_distance of the left edge of the screen
        x = random.randint(min_distance, screen_width)
    elif player_x > screen_width - min_distance:
        # Player is within min_distance of the right edge of the screen
        x = random.randint(0, screen_width - min_distance)
    else:
        # Player is within min_distance of neither edge of the screen
        x = random.randint(0, player_x - min_distance) if random.random() < 0.5 else random.randint(player_x + min_distance, screen_width)

    # Generate a random y coordinate that is outside the minimum distance from the player's y position
    if player_y < min_distance:
        # Player is within min_distance of the top edge of the screen
        y = random.randint(min_distance, screen_height)
    elif player_y > screen_height - min_distance:
        # Player is within min_distance of the bottom edge of the screen
        y = random.randint(0, screen_height - min_distance)
    else:
        # Player is within min_distance of neither edge of the screen
        y = random.randint(0, player_y - min_distance) if random.random() < 0.5 else random.randint(player_y + min_distance, screen_height)

#end

    
    # Set the enemy's position to the random coordinates
     # Check if it's time to move the enemy
    if time.time() - last_move_time >= move_delay:
    
        enemy_x = x
        enemy_y = y
    # Add a delay to slow down the enemy's movement
    #time.sleep(5)

        # Update the screen
        # Update display
        pygame.display.flip() # update the display to show the new frame
        last_move_time = time.time()
        #END MOVE THE ENEMY RANDOMLY AROUND THE SCREEN

    if enemy_health <= 0:
    # Create victory message
        victory_message = font.render("Victory!", 1, (255, 255, 255))
        # Draw victory message on screen
        screen.blit(victory_message, (screen_width / 2 - 50, screen_height / 2 - 50))
         # Update display
        pygame.display.flip() # update the display to show the new frame
        # Wait for 3 seconds
        time.sleep(3)

        
        # Reset the player's position
        player_x = 100
        player_y = 500
    
    # Progress to the next level
        current_level += 1
        # Reset the enemy's health
        enemy_health = 100
        #make game harder
        min_distance = min_distance + 20
        move_delay = move_delay -.5
        if move_units < 300:
    # Do something if move_units is less than or equal to 300
            move_units = move_units + 10
        elif move_units > 300:
    # Do something if move_units is greater than 300
            continue
    # Update display
    pygame.display.flip() # update the display to show the new frame


# Quit game
pygame.quit() # quit the pygame engine
sys.exit() # exit the program
