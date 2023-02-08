'''
Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.
'''

import pygame

pygame.init()
pygame.mixer.init()

# Carregando o arquivo de áudio
pygame.mixer.music.load('C:/Users/Samue/Music/Pagode/Só Pra Contrariar - Quando É Amor.mp3')

# Iniciando a reprodução
pygame.mixer.music.play()

# Mantendo o programa ativo enquanto o áudio estiver tocando
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

