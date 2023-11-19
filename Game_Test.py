import unittest
import pygame
from pygame import Rect
from pygame.locals import *
import sys
from engine import Animation

class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.player_x = 300
        pygame.init()
        self.screen = pygame.display.set_mode((700,500))
        pygame.display.set_caption("GameTest")
        self.font = pygame.font.Font(None, 24)
        self.player_image = pygame.Surface((55, 55))
        self.platforms = [
            Rect(100, 300, 400, 50),
            Rect(100, 250, 50, 50),
            Rect(450, 250, 50, 50)
        ]
        self.coins = [
            Rect(100, 200, 21, 22),
            Rect(210, 250, 21, 22)
        ]
        self.enemies = [
            Rect(150, 260, 50, 39)
        ]
        self.game_state = "playing"
        self.player_x = 300
        self.player_y = 0
        self.player_speed = 0
        self.player_acceleration = 0.2
        self.score = 0
        self.lives = 3
        self.player_rect = Rect(self.player_x, self.player_y, 55, 55)

    def tearDown(self):
        pygame.quit()
        
    def test_update_player_position(self):
        new_player_rect = (self.player_x, self.player_y, 55, 55)
        keys = {}
        keys[K_a] = False
        keys[K_d] = False
        keys[K_w] = False
        pass
        
        new_player_x = self.player_x
        new_player_y = self.player_y
        if keys[K_a]:
            new_player_x -= 2
        if keys[K_d]:
            new_player_x += 2
        if keys[K_w]:
            self.player_speed = -5
        
        for p in self.platforms:
            if self.player_rect.colliderect(new_player_rect):
                break
            else:
                self.player_x = new_player_x
                self.player_y = new_player_y + self.player_speed
                self.player_speed += self.player_acceleration
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_a:
                    keys[K_a] = True       
             
if __name__ == '__main__':
 unittest.main()