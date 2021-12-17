from typing import Text
import pygame as pg
import zanechessgame_engine as Engine
from pygame.locals import *

#global variables

#initilizing pyagme just in case 

pg.init()

# ---Window---

WIDTH = 250
HEIGHT = 250
MAX_FPS = 15

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BROWN = (150, 75, 0)
RED = (255,0, 0)


def main():

    screenT = pg.display.set_mode((WIDTH, HEIGHT))
    screenT.fill((65,225,200))
    pg.init()
    icon = pg.image.load( "venv/Chess/images/bQ.png")
    pg.display.set_caption('Timer')
    pg.display.set_icon(icon)   
    clock = pg.time.Clock()
    timer_white = pg.time.Clock()
    timer_black = pg.time.Clock()
    counter, counter1, text, text1 = 100000, 100000,'100000'.rjust(3), '100000'.rjust(3)
    pg.time.set_timer(pg.USEREVENT, 1000)
    font = pg.font.SysFont('Consolas', 30)

    class button():
        
        #colours for button and text
        
        
        button_col = (255, 255, 255)
        hover_col = (75, 225, 255)
        click_col = (50, 150, 255)
        text_col = (0,0,0)
        width = 80
        height = 50

        def __init__(self, x, y, text):
            self.x = x
            self.y = y
            self.text = text

        def draw_button(self):

            global clicked
            action = False
            clicked = False
            font = pg.font.SysFont('Constantia', 20)
            #get mouse position
            #pos = pg.mouse.get_pos()

            #create pygame Rect object for the button
            button_rect = Rect(self.x, self.y, self.width, self.height)
            
            #check mouseover and clicked conditions
            
            pg.draw.rect(screenT, self.button_col, button_rect)
            
            #add shading to button
            pg.draw.line(screenT, BLACK, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
            pg.draw.line(screenT, BLACK, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

            #add text to button
            text_img = font.render(self.text, True, self.text_col)
            text_len = text_img.get_width()
            screenT.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 18))
            return action

    def buttonColorManage(pos):
        ResetButton.button_col = (GREEN)
        WhiteButton.draw_button()
        BlackButton.draw_button()
        ResetButton.draw_button()


    gs =  Engine.GameState()
    running = True 
    print(HEIGHT//100)
    print(WIDTH-WIDTH//3)
    myfont = pg.font.SysFont("public-sans", 50)   
    label1 = myfont.render("TIMER", 1, (255,255,0))
    screenT.blit(label1, (30,35))
    ResetButton = button(150,25,'RESET')
    WhiteButton = button(40,90,'WHITE')
    BlackButton = button(40,190,'BLACK') 
    ResetButton.draw_button()
    WhiteButton.draw_button()
    BlackButton.draw_button()
   
   
   
    while running:
    
        for EVENT in pg.event.get(): 
            if EVENT.type == pg.QUIT: 
                running = False

            if EVENT.type == pg.MOUSEBUTTONDOWN: 
                posb = pg.mouse.get_pos()

                if (30 <= posb[0] <= 120 and 80 <= posb[1] <= 140):
                    
                    timerw= True
                    while timerw is True:
                        for EVENT in pg.event.get():
                            posb = pg.mouse.get_pos()
                            if EVENT.type == pg.MOUSEBUTTONDOWN and (30 <= posb[0] <= 120 and 180 <= posb[1] <= 240):
                                timerw = False
                                timerb = True
                                break
                        else:
                            WhiteButton.button_col = (WHITE) 
                            BlackButton.button_col = (RED)
                            counter -= 1
                            text = str(counter).rjust(3) if counter > 0 else '!!!'
                            screenT.fill((65,225,200), rect=(135,100, WIDTH-WIDTH//3,HEIGHT//1))
                            screenT.blit(font.render(text, True, (255, 0, 0)), (140,100))
                            screenT.blit(font.render(text1, True, (255, 0, 0)), (140,200))
                            pg.display.flip()
                            pg.display.update()
                            timer_white.tick(60)
                            timer_black.tick(60)
                            pg.time.wait(10)
                elif (30 <= posb[0] <= 120 and 180 <= posb[1] <= 240):
                    
                    timerb = True
                    while timerb is True:
                        for EVENT in pg.event.get():
                            posb = pg.mouse.get_pos()
                            if EVENT.type == pg.MOUSEBUTTONDOWN and (30 <= posb[0] <= 120 and 80 <= posb[1] <= 140):
                                timerb = False
                                timerw = True
                                break
                        else:
                            WhiteButton.button_col = (RED) 
                            BlackButton.button_col = (WHITE)
                            counter1 -= 1
                            text1 = str(counter1).rjust(3) if counter1 > 0 else '!!!'
                            screenT.fill((65,225,200), rect=(135,100, WIDTH-WIDTH//3,HEIGHT//1))
                            screenT.blit(font.render(text, True, (255, 0, 0)), (140,100))
                            screenT.blit(font.render(text1, True, (255, 0, 0)), (140,200))
                            pg.display.flip()
                            pg.display.update()
                            timer_white.tick(60)
                            timer_black.tick(60)
                            pg.time.wait(10)
                elif (140 <= posb[0] <= 230 and 15 <= posb[1] <= 85):
                    WhiteButton.button_col = (WHITE) 
                    BlackButton.button_col = (WHITE)
                    counter, counter1, text, text1 = 100000, 100000,'100000'.rjust(3), '100000'.rjust(3)
                    screenT.fill((65,225,200), rect=(135,100, WIDTH-WIDTH//3,HEIGHT//1))
                break
                    
            posbut = pg.mouse.get_pos()
            buttonColorManage(posbut)

        screenT.blit(font.render(text, True, (255, 0, 0)), (140,100))
        screenT.blit(font.render(text1, True, (255, 0, 0)), (140,200))
        clock.tick(MAX_FPS)
        pg.display.flip()
        pg.display.update()

main()