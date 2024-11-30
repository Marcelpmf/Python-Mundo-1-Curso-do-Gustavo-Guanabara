import pygame

pygame.init() # iniciar uso do pygame
pygame.mixer_music.load('reaper.mp3') # carregar musica
pygame.mixer.music.play() # tocar musica
input()
pygame.event.wait() # espera o evento terminar
