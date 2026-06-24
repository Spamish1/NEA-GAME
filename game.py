import pygame 
from setting import screen_height , screen_width , background_colour 

class game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption(game_title)
        self.clock = pygame.time.Clock() 
        self.running = True
        #game state 
        self.score = 0
        self.currentlevel = 1 
        self.currentwave = 1

        #will probably need to add mroe later


    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        self.quit()    

