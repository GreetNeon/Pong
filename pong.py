import pygame, sys, random

def ball_animation():
    global ball_speed_x, ball_speed_y, p_score, op_score

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= 500:
        ball_speed_y *= -1
    if ball.left <= 0:
        ball_restart()
        p_score += 1
    if ball.right >= 800:
        ball_restart()
        op_score += 1
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= 500:
        player.bottom = 500

def opponent_ai():
    if ball.x <= 300: #and ball_speed_x < 0:
        if opponent.top < ball.y:
            opponent.top += opponent_speed
        if opponent.top > ball.y:
            opponent.top -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= 500:
        opponent.bottom = 500



def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (400, 250)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

ball = pygame.Rect(800/2 - 15, 500/2 - 15, 30, 30)
player = pygame.Rect(800 - 20, 500/2 - 70, 10, 140)
opponent = pygame.Rect(10, 500/2 - 70, 10, 140)

light_grey = (200, 200, 200)
bg_color = pygame.Color('grey12')

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

p_score = 0
op_score = 0
game_font = pygame.font.Font(None, 100)



while 1==1:
    p_score_surface = game_font.render(str(p_score), True, (255, 255, 255))
    op_score_surface = game_font.render(str(op_score), True, (255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed +=7
            if event.key == pygame.K_UP:
                player_speed -=7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -=7
            if event.key == pygame.K_UP:
                player_speed +=7

    ball_animation()
    player_animation()
    opponent_ai()
    

    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (400, 0), (400, 500))
    screen.blit(p_score_surface, (400 + 15, 0))
    screen.blit(op_score_surface, (400 - 50, 0))

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_w:
        #         boards.b1.y -= 10
        #     elif event.key == pygame.K_s:
        #         boards.b1.y += 10
        #     elif event.key == pygame.K_UP:
        #         boards.b2.y -= 10
        #     elif event.key == pygame.K_DOWN:
        #         boards.b2.y += 10


    clock.tick(60)
    print(clock.get_fps())
    pygame.display.update()

        