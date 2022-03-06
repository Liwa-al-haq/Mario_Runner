import pygame
import random
from sys import exit
def display_score():
    current_time = (pygame.time.get_ticks()//1000) - start_timer
    score_surface = text_font.render(f'Score:{current_time}',False,(255,255,255))
    score_rectangle = score_surface.get_rect(center = (270,40))
    screen.blit(score_surface,score_rectangle)
    return current_time
def player_animation():
    global player_surface,player_index

    if player_rectangle.bottom < 250:
        player_surface = player_jump
    elif player_rectangle.colliderect(goomba_rect):
        player_surface = player_death
    elif player_rectangle.colliderect(koopa_rect):
        player_surface = player_death
    else:
        player_index += 0.1
        if player_index >= len(player_walk):player_index = 0
        player_surface = player_walk[int(player_index)]

def fps():
    fp=str(int(clock.get_fps()))
    sc=text_font.render(f'FPS: {fp}',False,(255,255,255))
    sc_rect=sc.get_rect(topleft=(100,100))
    map.blit(sc,sc_rect)

pygame.init()
screen = pygame.display.set_mode((550,280))
game_active = False
pygame.display.set_caption("Super Mario Runner")
pygame.display.set_icon(pygame.image.load('Icon/icon.jpg'))

map = pygame.image.load('level_1 (1).png').convert_alpha()
map_rect=map.get_rect(topleft=(0,0))
clock = pygame.time.Clock()
#Music
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
player_change = 0
#fireball_left=0
map_change=0
game_name = logo
game_name_rect = game_name.get_rect(center=(275,70))
game_message = text_font.render('Press space to start',False,(255,255,255))
game_message_rect = game_message.get_rect(center=(275,180))

#SCORE TEXT

score_message = text_font.render(f'Your score: {score}', False, (255, 255, 255))
score_message_rect = score_message.get_rect(center=(270, 230))
game_win=text_font.render("     Victory",False,(255,255,255))
game_win_rect=game_win.get_rect(center=(200,200))
#game_fps=text_font.render(f'FPS: {fps}',False,(255,255,255))
#game_fps_rect=game_fps.get_rect(center=(100,100))

l=input("Enter your name: ")
score_msg=text_font.render(f'Hello:{l}',False,(255,255,255))
score_msg_rect=score_msg.get_rect(center=(270,230))
#Player
'''player_surf = pygame.image.load('Enemies/mario_bros1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (60,250))
'''
player_walk_1 = pygame.image.load('Enemies/mario_bros1.png').convert_alpha()
player_walk_2 = pygame.image.load('Enemies/mario_bros_walk_2-removebg-preview.png').convert_alpha()
player_walk = [player_walk_1,player_walk_2]
player_index = 0
player_jump =  pygame.image.load('Enemies/jump-removebg-preview.png').convert_alpha()
player_death = pygame.image.load('Enemies/mario_bros-removebg-preview.png')
player_surface = player_walk[player_index]
player_rectangle = player_surface.get_rect(midbottom = (60,250))

#Enemies
#Goomba
goomba_surf = pygame.image.load('Enemies/enemies-removebg-preview.png').convert_alpha()
goomba_rect = goomba_surf.get_rect(midbottom = (500,250))

#Fireball
#fireball_surf=pygame.image.load('Enemies/enemies-removebg-preview (1).png').convert_alpha()
#fireball_rect=fireball_surf.get_rect(midbottom=(80,250))
#Music
bg_music.play(-1)

#Koopa
koopa_surf = pygame.image.load('Enemies/turtle 1.png').convert_alpha()
koopa_rect = koopa_surf.get_rect(center=(605,180))
#sc_rect_change=0
#Timer
#obstacle_rect_list =[]
#Timer
#obstacle_timer = pygame.USEREVENT + 1
#pygame.time.set_timer(obstacle_timer,1500)

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            fps()
            if event.type == pygame.KEYDOWN:
                map_change = -2
                if event.key == pygame.K_SPACE and player_rectangle.bottom >= 250:
                    player_gravity = -15
                    jump_music.play()
                if event.key == pygame.K_a:
                    #player_change = -4
                    map_change= 2
                if event.key == pygame.K_d:
                    #player_change = 4
                    map_change = -2
                    #sc_rect_change=-2
                #if event.key == pygame.K_w:
                    #fireball_rect.x +=-3
                    #fireball_left = -3
                    #if fireball_rect.bottom>=250:fireball_rect.bottom==250
                    #screen.blit(fireball_surf, fireball_rect)

        else:
            bg_music.stop()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                bg_music.play(-1)
                start_timer = (pygame.time.get_ticks() // 1000)

    if game_active:
        score = display_score()
        player_animation()
        #fps=fps()
        #screen.blit(game_fps,game_fps_rect)
        #map.blit(score_message,score_message_rect)
        map.blit(score_msg, score_msg_rect)
        #screen.blit(game_fps,game_fps_rect)
        # collison
        if player_rectangle.colliderect(goomba_rect):
            goomba_rect.x = 550
            map_rect.x=0
            game_active = False
            a=random.randrange(0,2)
            if a == 0:
                death_music.play()
            else:
                game_over.play()
            bg_music.stop()
            pygame.time.delay(1500)
        if score >= 40:
            game_active=False
            screen.blit(score_message, score_message_rect)
            screen.blit(game_win, game_win_rect)
            bg_music.stop()
            victory_music.play()
        if player_rectangle.colliderect(koopa_rect):
            koopa_rect.x = 550
            game_active = False
            death_music.play()
            bg_music.stop()
            pygame.time.delay(2000)

        #map.blit(game_fps, game_fps_rect)
        player_gravity += 1
        player_rectangle.x += player_change
        map_rect.x += map_change
        screen.blit(map, map_rect)
        #fireball_left += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 250: player_rectangle.bottom = 250
        screen.blit(player_surface, player_rectangle)
        if player_rectangle.x >= 530:player_rectangle.x =530
        if player_rectangle.x<=0:player_rectangle.x=0
        goomba_rect.x -= 4
        koopa_rect.x -= 4
        if goomba_rect.left <= -200: goomba_rect.left = 550
        screen.blit(goomba_surf, goomba_rect)
        if koopa_rect.left <= -200:koopa_rect.left = 550
        screen.blit(koopa_surf,koopa_rect)


    else:
        screen.fill((255, 0, 0))
        screen.blit(player_surface, player_rectangle)
        screen.blit(game_name, game_name_rect)
        score_message = text_font.render(f'Your score: {score}', False, (255, 255, 255))
        score_message_rect = score_message.get_rect(center=(270, 230))
        game_win = text_font.render("     Victory", False, (255, 255, 255))
        game_win_rect = game_win.get_rect(center=(200, 200))


        if score == 0:
          screen.blit(game_message,game_message_rect)

        else:
          screen.blit(score_message, score_message_rect)
          screen.blit(game_message, game_message_rect)
    pygame.display.update()
    clock.tick(60)
    print(clock.get_fps())



