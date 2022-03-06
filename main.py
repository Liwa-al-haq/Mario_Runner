import pygame
from random import randint,choice
from sys import exit


def display_score():
    current_time = (pygame.time.get_ticks()//1000) - start_timer
    score_surface = text_font.render(f'Score:{current_time}',False,(255,255,255))
    score_rectangle = score_surface.get_rect(center = (270,40))
    screen.blit(score_surface,score_rectangle)
    return current_time

pygame.init()
screen = pygame.display.set_mode((550,280))
game_active = False
pygame.display.set_caption("Super Mario Runner")
pygame.display.set_icon(pygame.image.load('Icon/icon.jpg'))
map = pygame.image.load('map.PNG').convert_alpha()
clock = pygame.time.Clock()
bg_music = pygame.mixer.Sound('Audio/resources_music_main_theme.ogg')
game_over = pygame.mixer.Sound('Audio/resources_music_game_over.ogg')
death_music = pygame.mixer.Sound('Audio/resources_music_death.wav')
jump_music = pygame.mixer.Sound('Audio/resources_sound_small_jump.ogg')
victory_music = pygame.mixer.Sound('Audio/resources_music_stage_clear.wav')
text_font = pygame.font.Font('Fonts/Fixedsys500c.ttf',50)
player_gravity = 0
start_timer = 0
score = 0
logo = pygame.image.load('Icon/Logo-removebg-preview.png').convert_alpha()
logo_rect = logo.get_rect(center=(280,100))
current_time = (pygame.time.get_ticks() // 1000) - start_timer
player_left = 0
game_name = logo
game_name_rect = game_name.get_rect(center=(275,70))
game_message = text_font.render('Press space to start',False,(255,255,255))
game_message_rect = game_message.get_rect(center=(275,180))

#Player
player_surf = pygame.image.load('Enemies/mario_bros1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (60,250))

#Enemies
#Goomba
goomba_surf = pygame.image.load('Enemies/enemies-removebg-preview.png').convert_alpha()
goomba_rect = goomba_surf.get_rect(midbottom = (500,250))

#Music
bg_music.play(-1)

#Koopa
koopa_surf = pygame.image.load('Enemies/turtle 1.png').convert_alpha()
koopa_rect = koopa_surf.get_rect(center=(605,180))

#Timer
obstacle_rect_list =[]
#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 250:
                    player_gravity = -15
                    jump_music.play()
                if event.key == pygame.K_d :
                    player_rect.x += player_left
                    player_left = -15

        else:
            bg_music.stop()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                bg_music.play(-1)
                start_time = (pygame.time.get_ticks() // 1000)


    if game_active:
        screen.blit(map, (0, 0))
        score = display_score()
        # collison
        if player_rect.colliderect(goomba_rect):
            goomba_rect.x = 550
            game_active = False
            death_music.play()
            bg_music.stop()
            pygame.time.delay(1500)
        if score>=30:
            game_active = False
            bg_music.stop()
            victory_music.play()


        if player_rect.colliderect(koopa_rect):
            koopa_rect.x = 550
            game_active = False
            death_music.play()
            bg_music.stop()
            pygame.time.delay(2000)

        player_gravity += 1
        player_left += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 250: player_rect.bottom = 250
        screen.blit(player_surf, player_rect)
        goomba_rect.x -= 4
        koopa_rect.x -= 4
        if goomba_rect.left <= -200: goomba_rect.left = randint(550,1000)
        screen.blit(goomba_surf, goomba_rect)
        if koopa_rect.left <= -200:koopa_rect.left = randint(550,1000)
        screen.blit(koopa_surf,koopa_rect)


    else:
        screen.fill((255, 0, 0))
        screen.blit(player_surf, player_rect)
        screen.blit(game_name, game_name_rect)
        score_message = text_font.render(f'Your score: {score}', False, (255, 255, 255))
        score_message_rect = score_message.get_rect(center=(270, 230))

        if score == 0:
          screen.blit(game_message,game_message_rect)

        else:
          screen.blit(score_message, score_message_rect)
          screen.blit(game_message,game_message_rect)


    pygame.display.update()
    clock.tick(60)

