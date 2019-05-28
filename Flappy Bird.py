import pygame
import sys, time, os, requests
from random import randint
from time import sleep
from PyQt5.QtWidgets import QApplication, QDialog,QProgressBar, QPushButton


if not os.path.exists("Data"):
    os.makedirs("Data")
if not os.path.exists("Data//Photos"):
    os.makedirs("Data//Photos")
if not os.path.exists("Data//Sounds"):
    os.makedirs("Data//Sounds")
if not os.path.exists("Data//Scores"):
    os.makedirs("Data//Scores")
data_list = ["Data//Photos//Arrow.png","Data//Photos//background.png","Data//Photos//bird0.png","Data//Photos//bird1.png","Data//Photos//bird2.png","Data//Photos//bird3.png","Data//Photos//bird4.png","Data//Photos//wall.png","Data//Sounds//hit.wav","Data//Sounds//point.wav","Data//Scores//Scores.data"]
data_urls = ["https://www.dropbox.com/s/invcntxcmwgophy/Arrow.png?dl=1","https://www.dropbox.com/s/f2am9bhzodfr60v/background.png?dl=1","https://www.dropbox.com/s/pmor5kfwuui64sw/bird0.png?dl=1","https://www.dropbox.com/s/9dm2w2klzmrvn0z/bird1.png?dl=1","https://www.dropbox.com/s/he3f19qg3ef28g5/bird2.png?dl=1","https://www.dropbox.com/s/qoetkeqr575eckn/bird3.png?dl=1","https://www.dropbox.com/s/q8epn72vpsc31o7/bird4.png?dl=1","https://www.dropbox.com/s/jnjypc6eoop5ll8/wall.png?dl=1","https://www.dropbox.com/s/m8k23zftwt5p9h3/hit.wav?dl=1","https://www.dropbox.com/s/ynth9tpnsgfz7jn/point.wav?dl=1","https://www.dropbox.com/s/zofef7hya7u734e/Scores.data?dl=1"]

for i in range(len(data_list)):
    if not os.path.exists(data_list[i]):
        web_download = requests.get(data_urls[i], allow_redirects=True)
        open(data_list[i], 'wb').write(web_download.content)
        print("successfully downloaded " + data_list[i])
def blit_all():
    mainwindow.blit(background, (0,0))
    mainwindow.blit(wallUp_img, (wall_up.x, wall_up.y))
    mainwindow.blit(wallDown_img, (wall_down.x, wall_down.y))
    mainwindow.blit(wallUp_img2, (wall_up2.x, wall_up2.y))
    mainwindow.blit(wallDown_img2, (wall_down2.x, wall_down2.y))
    mainwindow.blit(score_text, (10, 10))
    mainwindow.blit(speed_text,(350,10))
    for i in range(-15,511,15):
        mainwindow.blit(arrowImg,(i,x))
score_file = open("Data//Scores//Scores.data", "r")
score_file_lines = score_file.readlines()
score_file_lines.sort(reverse=True)
best_score = score_file_lines[0]
score_file.close()
pygame.init()

mainwindow = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Falppy Bird')

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
aqua = (0,255,255)


clock = pygame.time.Clock()

wall_up = pygame.Rect(1025, 0, 40, 120)
wall_down = pygame.Rect(1025, 280, 40, 120)
wall_up2 = pygame.Rect(755, 0, 40, 120)
wall_down2 = pygame.Rect(755, 280, 40, 120)

bird =  pygame.Rect(100, 220, 40, 40)

v_wall = -5
gap = 160

v_bird = 2
a_bird = 1

bird_img0 = pygame.image.load('Data\\Photos\\bird0.png')
bird_img0 = pygame.transform.scale(bird_img0, (40,40))
bird_img1 = pygame.image.load('Data\\Photos\\bird1.png')
bird_img1 = pygame.transform.scale(bird_img1, (40,40))
bird_img2 = pygame.image.load('Data\\Photos\\bird2.png')
bird_img2 = pygame.transform.scale(bird_img2, (40,40))
bird_img3 = pygame.image.load('Data\\Photos\\bird3.png')
bird_img3 = pygame.transform.scale(bird_img3, (40,40))
bird_img4 = pygame.image.load('Data\\Photos\\bird4.png')
bird_img4 = pygame.transform.scale(bird_img4, (40,40))
bird_images = [bird_img1, bird_img1, bird_img1, bird_img2, bird_img2, bird_img2, bird_img3, bird_img3, bird_img3, bird_img4, bird_img4, bird_img4]
i_bird_images = 0

wallUp_img = pygame.image.load('Data\\Photos\\wall.png')
wallUp_img = pygame.transform.scale(wallUp_img, (wall_up.w,wall_up.h))
wallDown_img = pygame.image.load('Data\\Photos\\wall.png')
wallDown_img = pygame.transform.scale(wallDown_img, (wall_down.w,wall_down.h))

wallUp_img2 = pygame.image.load('Data\\Photos\\wall.png')
wallUp_img2 = pygame.transform.scale(wallUp_img2, (wall_up2.w,wall_up2.h))
wallDown_img2 = pygame.image.load('Data\\Photos\\wall.png')
wallDown_img2 = pygame.transform.scale(wallDown_img2, (wall_down2.w,wall_down2.h))

background = pygame.image.load('Data\\Photos\\background.png')
background = pygame.transform.scale(background, (500,400))

arrowImg = pygame.image.load('Data\\Photos\\Arrow.png')
arrowImg = pygame.transform.scale(arrowImg, (30,30))

none_font = pygame.font.SysFont('JLSDataGothicR_NC', 50)
none_text = none_font.render('Press Space To Start', True, red)

score_font = pygame.font.SysFont('JLSDataGothicR_NC', 40)
score_text = score_font.render('Score: 0', True, blue)

pause_font = pygame.font.SysFont('JLSDataGothicR_NC', 100)
pause_text = pause_font.render('Paused', True, aqua)

resume_text1 = pause_font.render('1', True, aqua)
resume_text2 = pause_font.render('2', True, aqua)
resume_text3 = pause_font.render('3', True, aqua)

gameover_font = pygame.font.SysFont('JLSDataGothicR_NC', 100)
gameover_text = pause_font.render('Gameover', True, red)

retry_font = pygame.font.SysFont('JLSDataGothicR_NC', 50)
retry_text = retry_font.render('Press Enter To Retry', True, aqua)

best_score_font = pygame.font.SysFont('JLSDataGothicR_NC', 23)
best_score_text = best_score_font.render('Best Score: ' + best_score, True, blue)


speed_text = score_font.render('Speed: 1',True,blue)
score_file_status = False
p = 0
score = 0
x=372
s=2
v=2
status=None

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            score_file = open("Data//Scores//Scores.data", "a")
            score_file.write(str(score)+"\n")
            score_file.close()
            pygame.quit()
            sys.exit()
    if score > int(best_score):
        best_score = int(best_score)
        best_score=score
        best_score = str(best_score)
    pressed=pygame.key.get_pressed()
    
    if status==None:
        blit_all()
        mainwindow.blit(best_score_text,(10,45))
        mainwindow.blit(bird_images[i_bird_images], (bird.x, bird.y))
        i_bird_images += 1
        mainwindow.blit(none_text, (25, 120))
        bird.y = bird.y + v_bird
        v_bird = v_bird + a_bird
        bird.y -= s

        if bird.y>=200:
            v_bird=-5

        if i_bird_images == len(bird_images):
            i_bird_images = 0
            
        if pressed[pygame.K_SPACE]:
            status='playing'

    if status=='playing':
        
        blit_all()
        mainwindow.blit(bird_images[i_bird_images], (bird.x, bird.y))
        speed_text = score_font.render('Speed: '+str(p+1),True,blue)
        i_bird_images += 1
        
        if i_bird_images == len(bird_images):
            i_bird_images = 0
            
        wall_up.x = wall_up.x + v_wall
        wall_down.x = wall_down.x + v_wall
        wall_up2.x = wall_up2.x + v_wall
        wall_down2.x = wall_down2.x + v_wall      
        if wall_up.x <= -45 :
            wall_up.x = 505
            wall_down.x = 505         
            wall_up.h = randint(40,200)
            wall_down.height = 400 - wall_up.height - gap
            wall_down.y = wall_up.height + gap
            wallUp_img = pygame.transform.scale(wallUp_img, (wall_up.w,wall_up.h))
            wallDown_img = pygame.transform.scale(wallDown_img, (wall_down.w,wall_down.h))

        if wall_up.x > bird.x + v_wall and wall_up.x <= bird.x and bird.y>0:
            pygame.mixer.music.load('Data\\Sounds\\point.wav')
            pygame.mixer.music.play(0)
            score += 1
            score_text = score_font.render('Score: ' + str(score), True, blue)
            if score%5 == 0:
                p+=1
                v_wall -= p
            if wall_up.x > bird.x + v_wall and wall_up.x <= bird.x and bird.y<=0:
                status='gameover'


        if wall_up2.x <= -45 :
            wall_up2.x = 505
            wall_down2.x = 505         
            wall_up2.height = randint(40,200)
            wall_down2.height = 400 - wall_up2.height - gap
            wall_down2.y = wall_up2.height + gap
            wallUp_img2 = pygame.transform.scale(wallUp_img2, (wall_up2.w,wall_up2.h))
            wallDown_img2 = pygame.transform.scale(wallDown_img2, (wall_down2.w,wall_down2.h))

        if wall_up2.x > bird.x + v_wall and wall_up2.x <= bird.x and bird.y>0:
            pygame.mixer.music.load('Data\\Sounds\\point.wav')
            pygame.mixer.music.play(0)
            score += 1
            score_text = score_font.render('Score: ' + str(score), True, blue)
            if score%5 == 0:
                p+=1
                v_wall -= p
            if wall_up2.x > bird.x + v_wall and wall_up2.x <= bird.x and bird.y<=0:
                status='gameover'
                   
        bird.y = bird.y + v_bird
        v_bird = v_bird + a_bird
        
        if pressed[pygame.K_p]:
            status='pause'
            
        if pressed[pygame.K_SPACE]:
            v_bird = -5
        
        if bird.y>340 or bird.colliderect(wall_up) or bird.colliderect(wall_down) or bird.colliderect(wall_up2) or bird.colliderect(wall_down2):
            pygame.mixer.music.load('Data\\Sounds\\hit.wav')
            pygame.mixer.music.play(0)
            status='gameover'        

    if status=='pause':
        blit_all()
        mainwindow.blit(bird_images[i_bird_images], (bird.x, bird.y))
        mainwindow.blit(pause_text, (100,100))
 
        if pressed[pygame.K_SPACE]:
            
            blit_all()
            mainwindow.blit(bird_images[i_bird_images], (bird.x, bird.y))
            mainwindow.blit(resume_text3, (215,115))
            time.sleep(1)
            pygame.display.update()
            clock.tick(30)


            blit_all()
            mainwindow.blit(bird_images[i_bird_images], (bird.x, bird.y))
            mainwindow.blit(resume_text2, (215,115))
            time.sleep(1)
            pygame.display.update()
            clock.tick(30)
            
            blit_all()
            mainwindow.blit(bird_images[i_bird_images], (bird.x, bird.y))
            mainwindow.blit(resume_text1, (220,115))
            time.sleep(1)
            pygame.display.update()
            clock.tick(30)
            sleep(1)

            blit_all()
            mainwindow.blit(bird_images[i_bird_images], (bird.x, bird.y))

            status='playing'

    if status=='gameover':
        
        if not score_file_status:
            score_file = open("Data//Scores//Scores.data", "a")
            score_file.write(str(score)+"\n")
            score_file.close()
            score_file = open("Data//Scores//Scores.data", "r")
            score_file_lines = score_file.readlines()
            score_file_lines.sort(reverse=True)
            best_score = score_file_lines[0]
            score_file.close()
            score_file_status = True
            
        blit_all()
        mainwindow.blit(best_score_text,(10,45))
        birdImg_rotated = pygame.transform.rotate(bird_img1, -70)
        mainwindow.blit(birdImg_rotated, (bird.x, bird.y))
        mainwindow.blit(gameover_text, (52.5, 115))
        mainwindow.blit(retry_text, (30, 190))
        
        best_score_text = best_score_font.render('Best Score: ' + best_score, True, blue)

        if bird.y<320:
            bird.y+=v
            v+=1
        if bird.y>=320:
            status='final'        

    if status=='final':
        
        blit_all()
        mainwindow.blit(best_score_text,(10,45))
        birdImg_rotated = pygame.transform.rotate(bird_img0, -70)
        mainwindow.blit(gameover_text, (52.5, 115))
        mainwindow.blit(retry_text, (30, 190))
        mainwindow.blit(birdImg_rotated, (bird.x, bird.y))
        
        if pressed[pygame.K_RETURN]:
            
            score_file = open("Data//Scores//Scores.data", "a")
            score_file.write(str(score)+"\n")
            score_file.close()
            score_file = open("Data//Scores//Scores.data", "r")
            score_file_lines = score_file.readlines()
            score_file_lines.sort(reverse=True)
            best_score = score_file_lines[0]
            score_file.close()

            best_score_text = best_score_font.render('Best Score: ' + best_score, True, blue)
            score = 0
            v_bird = -10
            a_bird = 1
            v_wall = -5
            p=0
            v=0
            score_text = score_font.render('Score: '+str(0), True, blue)

            wall_up = pygame.Rect(1025, 0, 40, 120)
            wall_down = pygame.Rect(1025, 280, 40, 120)
            wall_up2 = pygame.Rect(755, 0, 40, 120)
            wall_down2 = pygame.Rect(755, 280, 40, 120)
            bird =  pygame.Rect(80, 220, 40, 40)
            wallUp_img = pygame.transform.scale(wallUp_img, (wall_up.w,wall_up.h))
            wallDown_img = pygame.transform.scale(wallDown_img, (wall_down.w,wall_down.h))
            wallUp_img2 = pygame.transform.scale(wallUp_img2, (wall_up2.w,wall_up2.h))
            wallDown_img2 = pygame.transform.scale(wallDown_img2, (wall_down2.w,wall_down2.h))

            status='playing'



    pygame.display.update()
    clock.tick(30)


     
