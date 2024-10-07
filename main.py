import pygame
pygame.mixer.init()
songs=["music1.mp3","music2.mp3","music3.mp3","music4.mp3","music5.mp3","music6.mp3","music7.mp3","music8.mp3","music9.mp3","music10.mp3","music11.mp3","music12.mp3"]

def playmusic(mymusic):
    pygame.mixer.music.load(mymusic)
    pygame.mixer.music.play()
    print(f"Now playing{mymusic}")

print("Welcome to simple music ")
print("Avaliable songs")

for song in songs:
    print(song)

choice=int(input("choose a song(1/2/3/4/5/6/7/8/9/10/11/12): "))


if choice==1:
    playmusic(songs[0])
if choice==2:
    playmusic(songs[1])
if choice==3:
    playmusic(songs[2])
if choice==4:
    playmusic(songs[3])
if choice==5:
    playmusic(songs[4])
if choice==6:
    playmusic(songs[5])
if choice==7:
    playmusic(songs[6])
if choice==8:
    playmusic(songs[7])
if choice==9:
    playmusic(songs[8])
if choice==10:
    playmusic(songs[9])
if choice==11:
    playmusic(songs[10])
if choice==12:
    playmusic(songs[11])
input("Just press enter to stop: ")
pygame.mixer.music.stop()