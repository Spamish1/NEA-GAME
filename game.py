import pygame 
from settings import screen_height , screen_width , background_colour , game_title , colour_txt , font_name , font_size , small_fontsize
import sys




class Game:
 
    def __init__(self):
        pygame.init()
        self.small_fontsize = pygame.font.SysFont(font_name, small_fontsize)
        self.font = pygame.font.SysFont(font_name, font_size)
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption(game_title)
        #REMEMER my game states will all be here remember for readability and scalability later  
        self.game_menu = False 
        self.game_options_and_intructions = False
        self.clock = pygame.time.Clock() 
        self.running = True
        self.score = 0
        self.currentlevel = 1  
        self.currentwave = 1
        self.Play_Game_button = pygame.Rect(screen_width // 2 - 200, screen_height // 3, 400, 100) 
        self.Quit_button = pygame.Rect(screen_width // 2 - 200, screen_height // 1.5, 400, 100)
        self.Controls_button = pygame.Rect(screen_width // 2 - 200, screen_height // 2, 400, 100)
        
        #will probably need to add more later


    
    def run(self): #Gameloop###self.update was here but causes issues as there was no attribute update for game 
        while self.running:
            self.handle_events()
            self.draw()
            self.clock.tick(60)
            
        self.quitGame()    
        


    def draw_text(self, text, font, colour_txt, x, y):
        img = font.render(text, True, colour_txt)
        self.screen.blit(img, (x, y))        


                ########## REMMEBR TO ADD THE PAUSE SYSTEM EARLY ON IF I DECIDE I NEED IT   
    def handle_events(self):
        for event in pygame.event.get():
            self.game_menu = True
            if event.type == pygame.QUIT:
                self.running = False 
            if  event.type == pygame.MOUSEBUTTONDOWN and self.Play_Game_button.collidepoint(event.pos):  
                print ("Play Game button pressed")
            if  event.type == pygame.MOUSEBUTTONDOWN and  self.Quit_button.collidepoint(event.pos): 
                print ("Quit button pressed")
                self.running = False
            if  event.type == pygame.MOUSEBUTTONDOWN and self.Controls_button.collidepoint(event.pos):  
                print ("Controls and isntructions button pressed")
                self.game_options_and_intructions = True
                
                 

            #if event.type == pygame.MOUSEBUTTONDOWN: 
                #print ("Mouse button pressed at:", event.pos)


    ###REMEMBER WHENEVER I DRAW SOMETHIN ON SCREEN COME HERE AND ADD IT TO THE DRAW FUNCTION
    def draw(self):
        self.screen.fill(background_colour)
        if self.game_menu == True :
            self.draw_text("Play Game", self.font, colour_txt, screen_width // 2 - 100, screen_height // 3)
            self.draw_text("Quit", self.font, colour_txt, screen_width // 2 - 45, screen_height // 1.5)
            self.draw_text("Controls and instructions", self.font, colour_txt, screen_width // 2 - 220, screen_height // 2)
           
        if self.game_options_and_intructions == True:
            self.game_menu = False
            self.screen.fill(background_colour)
            self.draw_text("Welcome to the game!", self.font, colour_txt, screen_width // 2 - 220, screen_height // 5)
            self.draw_text("These are your controls : movement, W A S D  attack , left click on your mouse  ", self.small_fontsize, colour_txt, screen_width // 2 - 400, screen_height // 2.7)
            self.draw_text("A brief description of the game: When you begin you will see a health bar and an equipped weapon,", self.small_fontsize, colour_txt, screen_width // 2 - 400, screen_height // 1.92 )
            self.draw_text("you must use this weapon to defeat enemies , in doing so , you scroe will increase over time,  ", self.small_fontsize, colour_txt, screen_width // 2 - 400, screen_height // 1.80)
            self.draw_text("do this to get to the next wave, once all waves are cleard, you can kill the boses unlocking a new level.  ", self.small_fontsize, colour_txt, screen_width // 2 - 400, screen_height // 1.7)
            
        pygame.display.flip()

   
    def quitGame(self): 
        pygame.quit()
        