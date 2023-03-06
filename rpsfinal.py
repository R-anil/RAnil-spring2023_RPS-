# File created by: Ryan Anil
# edited for github
 
# import libraries
# used to delay code
from time import sleep
# generate a random result from computer
from random import randint 
# a comprehensive game library for use with python
import pygame as pg
# to manage files and folders in terms of directories
import os
# this stores where we are currently working in the game folder
game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings
WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors
# tuples are immutable - cannot change once created
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

choices = ["rock", "paper", "scissors"]

def draw_text(text, size, color, x, y):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

# cpu chooses randomly...
def cpu_randchoice():
    choice = choices[randint(0,2)]
    print("computer randomly decides..." + choice)
    return choice

pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock, Paper, Scissors...")
clock = pg.time.Clock()

rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
rock_image_rect = rock_image.get_rect()
cpu_rock_image_rect = rock_image.get_rect()

paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
paper_image_rect = paper_image.get_rect()
cpu_paper_image_rect = paper_image.get_rect()

scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
scissors_image_rect = scissors_image.get_rect()
cpu_scissors_image_rect = scissors_image.get_rect()

start_screen = True

player_choice = ""
cpu_choice = ""
running = True

while running:
    clock.tick(FPS)
    # get user input
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # ########## input ###########
        # HCI - human computer interaction...
        # keyboard, mouse, controller, vr headset
        # keys = pg.key.get_pressed()
        # if keys[pg.K_SPACE]:
        #     print("start game!!!")
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                print("game on!!!!")
                start_screen = False
        
        if event.type == pg.MOUSEBUTTONUP:
            # displays coordinates where you click
            print(pg.mouse.get_pos()[0])
            print(pg.mouse.get_pos()[1])
            # stores mouse position
            mouse_coords = pg.mouse.get_pos()
            # if pg.mouse.get_pos()[0] <= my_image_rect.width and pg.mouse.get_pos()[1] < my_image_rect.height:
            #print("i clicked the rock")
            print(rock_image_rect.collidepoint(mouse_coords))
            if rock_image_rect.collidepoint(mouse_coords):
                print("you clicked on rock..")
                player_choice = "rock"
                cpu_choice = cpu_randchoice()
                # call a function that gets the cpu choice
            elif paper_image_rect.collidepoint(mouse_coords):
                print("you clicked on paper...")
                player_choice = "paper"
                cpu_choice = cpu_randchoice()
       
            elif scissors_image_rect.collidepoint(mouse_coords):
                print("you clicked on scissors...")
                player_choice = "scissors"
                cpu_choice = cpu_randchoice()                      
            else:
                print("you didn't click on anything...")
    

    ############ draw ###################
    screen.fill(BLACK)

    # waits for player to hit space bar
    if start_screen:
        draw_text("Press space to play rock paper scissors", 22, WHITE, WIDTH/2, HEIGHT/10)
        rock_image_rect.x = 2000
        paper_image_rect.x = 2000
        scissors_image_rect.x = 2000

    # allows player to choose rock paper or scissors
    if not start_screen and player_choice == "":
        rock_image_rect.x = 50
        paper_image_rect.x = 350
        scissors_image_rect.x = 550
        screen.blit(scissors_image, scissors_image_rect)
        screen.blit(paper_image, paper_image_rect)
        screen.blit(rock_image, rock_image_rect)

    # checks to see what the outcome of the contest was
    if player_choice == "rock":
        if cpu_choice == "rock":
            cpu_rock_image_rect.x = 500
            screen.blit(rock_image, rock_image_rect)
            screen.blit(rock_image, cpu_rock_image_rect)
            draw_text("You Tied!!!", 40, RED, WIDTH/2, HEIGHT/10)
        if cpu_choice == "paper":
            cpu_paper_image_rect.x = 500
            screen.blit(rock_image,rock_image_rect)
            screen.blit(paper_image_rect, cpu_paper_image_rect)
            draw_text("You Lost!!!", 40, RED, WIDTH/2, HEIGHT/10)
        if cpu_choice == "scissors":
            cpu_scissors_image_rect.x = 500
            screen.blit(rock_image,rock_image_rect)
            screen.blit(scissors_image_rect, cpu_scissors_image_rect)
            draw_text("You Won!!!", 40, RED, WIDTH/2, HEIGHT/10)
    if player_choice == "paper":
        if cpu_choice == "paper":
            cpu_paper_image_rect.x = 500
            screen.blit(paper_image, paper_image_rect)
            screen.blit(paper_image, cpu_paper_image_rect)
            draw_text("You Tied!!!", 40, RED, WIDTH/2, HEIGHT/10)
        if cpu_choice == "rock":
            cpu_rock_image_rect.x = 500
            screen.blit(paper_image, paper_image_rect)
            screen.blit(rock_image, cpu_rock_image_rect)
            draw_text("You Won!!!", 40, RED, WIDTH/2, HEIGHT/10)
        if cpu_choice == "scissors":
            cpu_scissors_image_rect.x = 500
            screen.blit(paper_image, paper_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            draw_text("You Lost!!!", 40, RED, WIDTH/2, HEIGHT/10)
    if player_choice == "scissors":
        if cpu_choice == "paper":
            cpu_paper_image_rect.x = 500
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(paper_image, cpu_paper_image_rect)
            draw_text("You Won!!!", 40, RED, WIDTH/2, HEIGHT/10)
        if cpu_choice == "rock":
            cpu_rock_image_rect.x = 500
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(rock_image, cpu_rock_image_rect)
            draw_text("You Lost!!!", 40, RED, WIDTH/2, HEIGHT/10)
        if cpu_choice == "scissors":
            cpu_scissors_image_rect.x = 500
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            draw_text("You Tied!!!", 40, RED, WIDTH/2, HEIGHT/10)
    pg.display.flip()

pg.quit()