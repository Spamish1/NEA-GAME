import pygame 
from setting import screen_height , screen_width , background_colour , game_title 

class Game:

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

        #will probably need to add more later


    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            self.update()
            self.clock.tick(60)
        self.quitGame()    

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False 
            

    def update(self):
        pass

    def draw(self):
        self.screen.fill(background_colour)
        pygame.display.flip()

    def quitGame(self):
        pygame.quit()
