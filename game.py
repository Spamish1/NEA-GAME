import pygame 
from settings import screen_height , screen_width , background_colour , game_title , colour_txt , font_name , font_size , small_fontsize
import sys
from map_parts import tile_info 
from maps import tile_map_level_1


class Game:
 
    def __init__(self):
        pygame.init()
        self.small_fontsize = pygame.font.SysFont(font_name, small_fontsize)
        self.font = pygame.font.SysFont(font_name, font_size)
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption(game_title)
        #REMEMER my game states will all be here remember for readability and scalability later  
        self.lvl_1 = False 
        self.game_menu = False 
        self.game_options_and_intructions = False
        self.clock = pygame.time.Clock() 
        self.running = True
        self.score = 0
        self.currentlevel = 1  
        self.currentwave = 1
        self.back_button = pygame.Rect(screen_width // 2 - 60, screen_height // 850, 400, 100) 
        self.Play_Game_button = pygame.Rect(screen_width // 2 - 200, screen_height // 3, 400, 100) 
        self.Quit_button = pygame.Rect(screen_width // 2 - 200, screen_height // 1.5, 400, 100)
        self.Controls_button = pygame.Rect(screen_width // 2 - 200, screen_height // 2, 400, 100)
        #will probably need to add more later

    def update_map(self,tile_map_level_1, tile_size, tile_info ):
        for i in  range(len(tile_map_level_1)):
            for j in range(len(tile_map_level_1[0])):
                 self.screen.blit(tile_info[tile_map_level_1[i][j]], (j * tile_size, i * tile_size)) 


    
     
     #tile_size = int((screen_width + 5) / (len(tile_map_level_1[0])-0.9))

    tile_size = 57 ## move to  setiings so no ciruclar import from game to entitties 

    for key in tile_info:
        tile_info[key] = pygame.transform.scale(tile_info[key], (tile_size, tile_size))   # fits tile images ino the gard



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
            elif  event.type == pygame.MOUSEBUTTONDOWN and self.Play_Game_button.collidepoint(event.pos):  
                print ("Play Game button pressed")
                self.lvl_1 = True
                self.game_menu = False
                self.game_options_and_intructions == False  
            elif  event.type == pygame.MOUSEBUTTONDOWN and  self.Quit_button.collidepoint(event.pos): 
                print ("Quit button pressed")
                self.running = False
            elif  event.type == pygame.MOUSEBUTTONDOWN and self.Controls_button.collidepoint(event.pos):  
                print ("Controls and isntructions button pressed")
                self.game_options_and_intructions = True
            elif event.type == pygame.MOUSEBUTTONDOWN and self.back_button.collidepoint(event.pos):
                print ("Back button pressed")
                self.game_options_and_intructions = False
                self.game_menu = True
            elif self.lvl_1 == True and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.lvl_1 = False
                self.game_menu = True
                self.game_options_and_intructions == False 
                if self.lvl_1 == True and self.game_menu == False :
                 if event.type == pygame.MOUSEBUTTONDOWN and  self.Quit_button.collidepoint(event.pos):
                  print ("Quit button pressed")
                  self.running = True

                

            #if event.type == pygame.MOUSEBUTTONDOWN: 
                #print ("Mouse button pressed at:", event.pos)




    def  get_screen_coordinates():
        return(x-y,(x+y)/2)


    def draw_entities(object,screen):
        self.screen.blit(object.image, get_screen_coordinates()(object.rect.x,object.rect.y))







    ###REMEMBER WHENEVER I DRAW SOMETHIN ON SCREEN COME HERE AND ADD IT TO THE DRAW FUNCTION
    def draw(self):
        self.screen.fill(background_colour)
        if self.game_menu == True :
            self.draw_text("Play Game", self.font, colour_txt, screen_width // 2 - 100, screen_height // 3)
            self.draw_text("Quit", self.font, colour_txt, screen_width // 2 - 45, screen_height // 1.5)
            self.draw_text("Controls and instructions", self.font, colour_txt, screen_width // 2 - 220, screen_height // 2)
            self.Quit_button = pygame.Rect(screen_width // 2 - 200, screen_height // 1.5, 400, 100)
            self.Play_Game_button = pygame.Rect(screen_width // 2 - 200, screen_height // 3, 400, 100)
            
        if self.game_options_and_intructions == True:
            self.game_menu = False
            self.screen.fill(background_colour)
            self.draw_text("Back", self.font, colour_txt, screen_width // 2 - 60, screen_height // 850)
            self.draw_text("Welcome to the game!", self.font, colour_txt, screen_width // 2 - 220, screen_height // 5)
            self.draw_text("These are your controls : movement, W A S D  attack , left click on your mouse  ", self.small_fontsize, colour_txt, screen_width // 2 - 400, screen_height // 2.7)
            self.draw_text("A brief description of the game: When you begin you will see a health bar and an equipped weapon,", self.small_fontsize, colour_txt, screen_width // 2 - 500, screen_height // 1.92 )
            self.draw_text("you must use this weapon to defeat enemies , in doing so , you score will increase over time,  ", self.small_fontsize, colour_txt, screen_width // 2 - 500, screen_height // 1.80)
            self.draw_text("do this to get to the next wave, once all waves are cleard, you can kill the boses unlocking a new level.  ", self.small_fontsize, colour_txt, screen_width // 2 - 500, screen_height // 1.7)
            self.Quit_button = pygame.Rect(screen_width // 2 - 20000, screen_height // 10000.5, 400, 100)
            self.Play_Game_button = pygame.Rect(screen_width // 2 - 20011, screen_height // 10000.5, 400, 100)

        if self.lvl_1 == True:
            self.update_map(tile_map_level_1, self.tile_size, tile_info)
            self.draw_text("Level:" + str(self.currentlevel), self.font, colour_txt, screen_width // 2 - 60, screen_height // 850)
            self.draw_text("Wave:" + str(self.currentwave), self.font, colour_txt, screen_width // 2 - 100, screen_height // 1.5)
            self.draw_text("Score: " + str(self.score), self.font, colour_txt, screen_width // 2 - 100, screen_height // 1.3)




        pygame.display.flip()    ##remebr to leave outside of if  staments to avoid the wierd  flashing 


















    
    def quitGame(self): 
        pygame.quit()
        