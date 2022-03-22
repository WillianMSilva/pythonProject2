#para inserir musica baixar a módulo pygame inserindo o codigo abaixo e clicando na lampada vermelha.
import pygame
pygame.init()
#Dentro das aspas inserir o nome do arquivo de música dentro da pasta do projeto. exemplo muisca.mp3
#Comandos para executar a música
pygame.mixer.music.load()
pygame.mixer.music.play()
pygame.event.wait()

