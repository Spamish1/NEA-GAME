import pygame 
from settings import screen_height , screen_width , background_colour , game_title , colour_txt , font_name , font_size 
import sys




class Game:
 
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont(font_name, font_size)
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption(game_title)
        self.clock = pygame.time.Clock() 
        self.running = True
        #game state 
        self.score = 0
        self.currentlevel = 1 
        self.currentwave = 1
        self.Play_Game_button = pygame.Rect(screen_width // 2 - 200, screen_height // 3, 40, 10)
        self.Quit_button = pygame.Rect(screen_width // 2 - 200, screen_height // 1.5, 40, 10)
        self.Controls_button = pygame.Rect(screen_width // 2 - 200, screen_height // 2, 40, 10)
        
        #will probably need to add more later


    
    def run(self): #Gameloop###self.update was here but causes issues as there was no attribute update for game 
        while self.running:
            self.handle_events()
            self.draw()
            self.clock.tick(60)
            print("Running")
        self.quitGame()    
        


    def draw_text(self, text, font, colour_txt, x, y):
        img = font.render(text, True, colour_txt)
        self.screen.blit(img, (x, y))        



    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False 
            if  event.type == pygame.MOUSEBUTTONDOWN and event.pos == self.Play_Game_button.collidepoint(event.pos):  ##play game button   
                print ("Play Game button pressed")
            if  event.type == pygame.MOUSEBUTTONDOWN and event.pos == self.Quit_button.collidepoint(event.pos):  ##quit button   
                print ("Quit button pressed")
            if  event.type == pygame.MOUSEBUTTONDOWN and event.pos == self.Controls_button.collidepoint(event.pos):  ##controls button   
                print ("Controls button pressed")
            if event.type == pygame.MOUSEBUTTONDOWN: 
                print ("Mouse button pressed at:", event.pos)
            # #else:    
               # print ("Mouse button pressed at:", event.pos)## maybe add event.pos to print the position of the mouse click
            ### this is a test t osee if i have the correct rectangels

    #def update(self):   ##change later  
        #pass


    ###REMEMBER WHENEVER I DRAW SOMETHIN ON SCREEN COME HERE AND ADD IT TO THE DRAW FUNCTION
    def draw(self):
        self.screen.fill(background_colour)
        self.draw_text("Play Game", self.font, colour_txt, screen_width // 2 - 200, screen_height // 3)
        self.draw_text("Quit", self.font, colour_txt, screen_width // 2 - 200, screen_height // 1.5)
        self.draw_text("Controls", self.font, colour_txt, screen_width // 2 - 200, screen_height // 2)
        pygame.display.flip()
   
    def quitGame(self):
        pygame.quit()

