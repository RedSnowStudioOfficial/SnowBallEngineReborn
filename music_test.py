import pygame

pygame.init()
pygame.mixer.init()

sound1 = pygame.mixer.Sound("resources/music/thunder-theme.wav")
sound2 = pygame.mixer.Sound("resources/music/Ballin.mp3")

channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)

channel1.play(sound1)
channel2.play(sound2)

while channel1.get_busy() or channel2.get_busy():
    pygame.time.Clock().tick(10)
pygame.quit()