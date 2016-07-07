"""
python 3.4.2
Ron Callahan

put a timeer on the screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
 
import pygame
import time
from time import sleep
from gpiozero import MotionSensor
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

bright_red = (255,0,0)
bright_green = (0,255,0)

# Motion sensor GPIO
player1_score = MotionSensor(4)
player2_score = MotionSensor(6)
 
pygame.init()
pygame.mixer.init()
sounda = pygame.mixer.Sound("end_game_buzzer.wav")
 
# Set the height and width of the screen
size = [800, 480]
screen = pygame.display.set_mode(size, pygame.NOFRAME)
 
#pygame.display.set_caption("SOHO HOCKEY")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

display_font = pygame.font.Font("SourceSansPro-Bold.ttf",  60) 
display_message = pygame.font.Font("SourceSansPro-Regular.ttf",  40) 
font = pygame.font.Font("Digital.ttf",  160)
font_small = pygame.font.Font("Digital.ttf",  100)

 
frame_count = 0
frame_rate = 30
start_time = 10

p1_score = 0
p2_score = 0



StartScreen = pygame.image.load("StartScreen.png")
splash = pygame.image.load("splash.png")
background = pygame.image.load("scoreboard.png")
background_end = pygame.image.load("EndGame.png")

backgroundRect = background.get_rect()

size = (width, height) = background.get_size()
screen = pygame.display.set_mode(size)

"""
# place start and quit buttons
pygame.draw.rect(StartScreen, GREEN,(400,330,130,55))
pygame.draw.rect(StartScreen, RED,(600,330,120,55))

"""
# start screen function #############################################
def game_intro():

    intro = True

    while intro:
        welcomeMessage = "tap screen to start"
        screen.blit(StartScreen, backgroundRect)
        text = display_message.render(str(welcomeMessage), True, RED)
        screen.blit(text, [400, 320])
        mousePress = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if mousePress[0] == 1:
                    intro = False
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
 
            else:
                pygame.display.update()
                clock.tick(15)
                pygame.display.flip()

game_intro()

# end start screen function #############################################



# start enter names function ############################################


player_1Message = "enter player one name"
player_2Message = "enter player two name"


"""
end_it=False 
while (end_it==False):
    screen.blit(splash, backgroundRect)
    text = display_message.render(str(player_1Message), True, RED)
    screen.blit(text, [30, 50])

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            end_it=True
    pygame.display.flip()
"""


# get player names and mak ALL CAPS
p1_name = input("Enter Player1 name: ")
p2_name = input("Enter Player2 name: ")

p1_name_up = p1_name.upper()
p2_name_up = p2_name.upper()


# end enter names function ############################################


 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop



    # Set the screen background
    screen.fill(BLACK)
    screen.blit(background, backgroundRect)
    
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT


 
        
    # --- Timer going up ---
    # Calculate total seconds
    total_seconds = frame_count // frame_rate
 
    # Divide by 60 to get total minutes
    minutes = total_seconds // 60
 
    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60
 
    # Use python string formatting to format in leading zeros
    #output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
 

 
    # --- Timer going down ---
    # --- Timer going up ---
    # Calculate total seconds
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0
 
    # Divide by 60 to get total minutes
    minutes = total_seconds // 60
 
    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60
 
    # Use python string formatting to format in leading zeros
    output_string = "{0:02}:{1:02}".format(minutes, seconds)
    
    p1_string = p1_score
    p2_string = p2_score

    # Blit names to the screen
    text = display_font.render(str(p1_name_up), True, WHITE)
    screen.blit(text, [30, 50])

    text = display_font.render(str(p2_name_up), True, WHITE)
    screen.blit(text, [600, 50])

    
    # Blit scores to the screen
    text = font_small.render(str(p1_string), True, RED)
    screen.blit(text, [50, 120])

    text = font_small.render(str(p2_string), True, RED)
    screen.blit(text, [630, 120])
 
    # Blit to the screen
    text = font.render(output_string, True, RED)
    screen.blit(text, [228, 78])

    #check if time has run out
    if total_seconds == 0 :
        # Use python string formatting to format in leading zeros
        output_string = "GAME OVER"
        tie_string = "OVER TIME!!"
        time.sleep(2)

        # Blit to the screen
        text = font_small.render(output_string, True, RED)
        screen.blit(text, [150, 240])
        sounda.play()
        sleep(5)
        screen.fill(WHITE)
        screen.blit(background_end, backgroundRect)
        if p2_score > p1_score:
                    text = font_small.render(p2_name, True, RED)
                    screen.blit(text, [150, 240])
        if p1_score > p2_score:
                    text = font_small.render(p1_name, True, RED)
                    screen.blit(text, [150, 240])
        if p1_score == p2_score:
                    text = font_small.render(tie_string, True, RED)
                    screen.blit(text, [150, 240])                

    # motion sensor output
    if player1_score.motion_detected:
        print("Player 1 scores!")
        p1_score += 1
        print ("player 1:", p1_score)
        print ("player 2:", p2_score)
        time.sleep(2)
    if player2_score.motion_detected:
        print("Player 2 scores!")
        p2_score += 1
        print ("player 1:", p1_score)
        print ("player 2:", p2_score)
        time.sleep(2)


    
      # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    frame_count += 1
 
    # Limit frames per second
    clock.tick(frame_rate)


 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()




# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()

            
            
