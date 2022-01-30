import pygame  # игровая библиотека
from random import randrange  # бибилиотека рандомных чисел
import sys  # библиотека потоковава


lastMove = ''
dis_width = 600
dis_height = 400
imeg = pygame.image.load('trava.png')  # загрузказка фона
game_over = pygame.image.load('game.jpg')   # загрузказка фона

pygame.init()
screen = pygame.display.set_mode((dis_width, dis_height))  # Создаем экран
pygame.display.set_caption('Snake')  # Название
clock = pygame.time.Clock()

running = True
# Размер змеи
snake_block = 10
snake_speed = 15  # Скорость змеи

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
number = pygame.font.SysFont("comicsansms", 10)


def terminate():  # Экстреный выход из програмы
    pygame.quit()
    sys.exit()


def number_dr(x, y, n):
    value = number.render(str(n), True, 'red')
    screen.blit(value, [x, y-2])


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, 'blue')
    screen.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, 'black', [x[0], x[1], snake_block, snake_block])


def message():
    msg, color = "Повторить игру - C, закончить игру - Q", 'red'
    global screen
    global running
    global game_over
    run = True
    while run:
        screen.blit(game_over, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    terminate()
                if event.key == pygame.K_c:
                    running = True
                    gameLoop()
        mesg = font_style.render(msg, True, color)
        screen.blit(mesg, [dis_width / 6, dis_height / 3])
        pygame.display.flip()
    pygame.quit()


def gameLoop():
    global lastMove
    global running
    global imeg
    x1 = dis_width / 2
    y1 = dis_height / 2
    coun = 1
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    n1 = randrange(1, 50, 5)
    n2 = randrange(51, 99, 5)
    n3 = n1 + n2
    n4 = randrange(1, 50, 5)
    n5 = randrange(51, 99, 5)
    n6 = randrange(1, 50, 5)
    prov = True
    prov2 = True
    while prov:
        if n4 != n5 and n4 != n6 or n5 != n4 and n5 != n6:
            prov = False

        elif n3 != n4 or n3 != n5 or n3 != n6:
            prov = False

        else:
            n4 = randrange(1, 50, 5)
            n5 = randrange(51, 99, 5)
            n6 = randrange(1, 50, 5)

    foodx1 = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody1 = round(randrange(50, dis_height - snake_block) / 10.0) * 10.0
    foodx2 = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody2 = round(randrange(50, dis_height - snake_block) / 10.0) * 10.0
    foodx3 = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody3 = round(randrange(50, dis_height - snake_block) / 10.0) * 10.0
    foodx4 = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody4 = round(randrange(50, dis_height - snake_block) / 10.0) * 10.0
    foodx5 = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody5 = round(randrange(50, dis_height - snake_block) / 10.0) * 10.0
    foodx6 = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody6 = round(randrange(50, dis_height - snake_block) / 10.0) * 10.0

    while prov2:
        if foodx1 != foodx2 and foodx1 != foodx3 and foodx1 != foodx4 and foodx1 != foodx5 and foodx1 != foodx6:
            prov2 = False
        else:
            foodx1 = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody1 = round(randrange(50, dis_height - snake_block) / 10.0) * 10.0
            foodx2 = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody2 = round(randrange(50, dis_height - snake_block) / 10.0) * 10.0
            foodx3 = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody3 = round(randrange(50, dis_height - snake_block) / 10.0) * 10.0
            foodx4 = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody4 = round(randrange(50, dis_height - snake_block) / 10.0) * 10.0
            foodx5 = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody5 = round(randrange(50, dis_height - snake_block) / 10.0) * 10.0
            foodx6 = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody6 = round(randrange(50, dis_height - snake_block) / 10.0) * 10.0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                terminate()

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

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            running = False
            message()

        x1 += x1_change
        y1 += y1_change
        screen.blit(imeg, (0, 0))
        pygame.draw.rect(screen, 'purple', [foodx1, foody1, snake_block, snake_block])
        pygame.draw.rect(screen, 'purple', [foodx2, foody2, snake_block, snake_block])
        pygame.draw.rect(screen, 'blue', [foodx3, foody3, snake_block, snake_block])
        pygame.draw.rect(screen, 'blue', [foodx4, foody4, snake_block, snake_block])
        pygame.draw.rect(screen, 'blue', [foodx5, foody5, snake_block, snake_block])
        pygame.draw.rect(screen, 'blue', [foodx6, foody6, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                message()

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        number_dr(foodx1, foody1, n1)
        number_dr(foodx2, foody2, n2)
        number_dr(foodx3, foody3, n3)
        number_dr(foodx4, foody4, n4)
        number_dr(foodx5, foody5, n5)
        number_dr(foodx6, foody6, n6)
        if x1 == foodx1 and y1 == foody1:
            if coun == 1 or coun == 2:
                foodx1 = -60
                foody1 = -60
                coun += 1

        elif x1 == foodx2 and y1 == foody2:
            if coun == 1 or coun == 2:
                foodx2 = -60
                foody2 = -60
                coun += 1

        elif x1 == foodx3 and y1 == foody3:
            if coun == 3:
                print('f')
                n1 = randrange(1, 50, 5)
                n2 = randrange(51, 100, 5)
                n3 = n1 + n2
                foodx1 = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody1 = round(randrange(0, dis_height - snake_block) / 10.0) * 10.0
                foodx2 = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody2 = round(randrange(0, dis_height - snake_block) / 10.0) * 10.0
                foodx3 = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody3 = round(randrange(0, dis_height - snake_block) / 10.0) * 10.0
                foodx4 = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody4 = round(randrange(50, dis_height - snake_block) / 10.0) * 10.0
                foodx5 = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody5 = round(randrange(50, dis_height - snake_block) / 10.0) * 10.0
                foodx6 = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody6 = round(randrange(50, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1
                coun -= 2
            else:
                message()
        elif x1 == foodx4 and y1 == foody4 or x1 == foodx5 and y1 == foody5 or x1 == foodx6 and y1 == foody6:
            message()

        Your_score(Length_of_snake - 1)
        pygame.display.update()
        clock.tick(snake_speed)
    pygame.quit()


if __name__ == '__main__':
    gameLoop()