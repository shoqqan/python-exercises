import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((590, 800))
backgrounds = [
    'python-exercises/lab-7/music-player/images/linkinpark.jpg',
    'python-exercises/lab-7/music-player/images/caramel.jpg',
    'python-exercises/lab-7/music-player/images/three6mafia.jpg',
    'python-exercises/lab-7/music-player/images/gmfu.jpg',
]
songs = [
    'python-exercises/lab-7/music-player/music/linkinpark.mp3',
    'python-exercises/lab-7/music-player/music/caramel.mp3',
    'python-exercises/lab-7/music-player/music/three6mafia.mp3',
    'python-exercises/lab-7/music-player/music/gmfu.mp3',
]
background_index = 0
bg_image = pygame.image.load(backgrounds[background_index]).convert()
converted_background = pygame.transform.scale(bg_image, (590, 800))
pygame.mixer.music.load(songs[background_index])
pygame.mixer.music.play()
play = False
finish = False

while not finish:

    screen.blit(converted_background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if background_index == 3:
                    background_index = 0
                else:
                    background_index = background_index + 1
                bg_image = pygame.image.load(backgrounds[background_index]).convert()
                converted_background = pygame.transform.scale(bg_image, (590, 800))
                pygame.mixer.music.load(songs[background_index])
                pygame.mixer.music.play()

            elif event.key == pygame.K_LEFT:
                if background_index == 0:
                    background_index = 3
                else:
                    background_index = background_index - 1
                bg_image = pygame.image.load(backgrounds[background_index]).convert()
                converted_background = pygame.transform.scale(bg_image, (590, 800))
                pygame.mixer.music.load(songs[background_index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_SPACE:
                play = not play
                if play:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
    pygame.display.flip()
