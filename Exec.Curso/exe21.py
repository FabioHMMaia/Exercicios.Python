# Faça um programa em Python que abra e reproduza o audio de um arquivo MP3

# PRIMEIRA OPÇÃO
import pygame #importar sons 
pygame.init() #iniciar o pygame
pygame.mixer.music.load('caminho do seu arquivo de som') #carregar o seu arquivo de som
pygame.mixer.play() #iniciar o seu arquivo de som

while pygame.mixer.music.get_busy():
    continue

#SEGUNDA OPÇÃO
from pydub import AudioSegmet #importando o caminhho 
form pydub.playback import play #importando o play/começar

audio = AudioSegmet.from_file('caminho do seu arquivo de som') #mostrando o caminho atraves da pasta 
play(audio) #iniciando o audio
