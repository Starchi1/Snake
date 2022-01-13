import pygame
import random
import sys


lastMove = ''
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

pygame.init()
screen = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

running = True
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def terminate():  # Экстреный выход из програмы
    pygame.quit()
    sys.exit()


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    screen.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    global lastMove
    global running
    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                if event.key == pygame.K_c:
                    gameLoop()

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if lastMove != 'right':
                        x1_change = -snake_block
                        y1_change = 0
                        lastMove = 'left'
                elif event.key == pygame.K_RIGHT:
                    if lastMove != 'left':
                        x1_change = snake_block
                        y1_change = 0
                        lastMove = 'right'
                elif event.key == pygame.K_UP:
                    if lastMove != 'down':
                        y1_change = -snake_block
                        x1_change = 0
                        lastMove = 'up'
                elif event.key == pygame.K_DOWN:
                    if lastMove != 'up':
                        y1_change = snake_block
                        x1_change = 0
                        lastMove = 'down'

        screen.fill(blue)
        message("You Lost! Press C-Play Again or Q-Quit", red)
        Your_score(Length_of_snake - 1)
        pygame.display.update()

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            terminate()
        x1 += x1_change
        y1 += y1_change
        screen.fill(blue)
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                terminate()

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()


gameLoop()