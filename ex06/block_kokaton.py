import pygame as pg
import sys
from random import randint
import os
from pygame.locals import *
import math

# 画面サイズ
SCREEN = Rect(0, 0, 400, 400)

class Block(pg.sprite.Sprite):
    def __init__(self, filename, x, y):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = pg.image.load(filename).convert()
        self.rect = self.image.get_rect()
        # ブロックの左上座標
        self.rect.left = SCREEN.left + x * self.rect.width
        self.rect.top = SCREEN.top + y * self.rect.height

class Screen:
    def __init__(self,title,wh,bgimg):
        pg.display.set_caption(title) #　追いつめられるこうかとん
        self.sfc = pg.display.set_mode(wh)   #(1600, 900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg) 
        self.bgi_rct = self.bgi_sfc.get_rect()
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) # 

def main():
    pg.init()
    screen = pg.display.set_mode(SCREEN.size)
    scr = Screen("逃げろ！こうかとん", (1600,900), "fig/pg_bg.jpg")
    
    for x in range(1, 15):
        for y in range(1, 11):
            Block("C:/Users/admin/Desktop/ProjExD2022/block.png", x, y)
if __name__ == "__main__":
    main()
        