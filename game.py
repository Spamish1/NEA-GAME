import pygame 
from setting import screen_height , screen_width , background_colour , game_title 

class Game:

    def __init__(self, screen):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption(game_title)

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 50)
        self.title_font = pygame.font.SysFont(None, 80)

        self.running = True
        self.game_state = "menu"

        # Game information
        self.score = 0
        self.current_level = 1
        self.current_wave = 1

        # Buttons
        button_width = 250
        button_height = 60

        self.play_button = pygame.Rect(screen_width // 2 - button_width // 2, 150, button_width, button_height)
        self.controls_button = pygame.Rect(screen_width // 2 - button_width // 2, 350, button_width, button_height)

            screen_width // 2 - button_width // 2, 450, button_width, button_height)
            screen_width // 2 - button_width // 2,
            450,
            button_width,
            button_height,
        )

        #will probably need to add more later


    def run(self): #Gameloop
        while self.running:
            if self.game_state == "menu":
                self.handle_menu()
                self.draw_menu()
            elif self.game_state == "playing":
                self.handle_playing()
                self.draw_playing()
            elif self.game_state == "controls":
                self.handle_controls()
                self.draw_controls()    

            self.handle_events()
            self.draw()
            self.update()
            self.clock.tick(60)
        self.quitGame() 
        while True:
            for event in pygame.event.get():
                if event.type == pygame.Quit:
                    pygame.QUIT()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button.checkForInput(pygame.mouse.get_pos())

            screen.fill("white")## will probably need to change to draw later
            button.update() 
            button.changeColor(pygame.mouse.get_Pos())

    pygame.display.update()       

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



def draw_menu(self,screen, background_colour):
    screen.fill(background_colour)
    ### to draw th etile and buttons may need to come back to it later to chasng e things make it looks nicer 
    title = self.font.render("killer waves", True, white)
    self.screen.blit(title, (settings.screen_width // 2 - title.get_width() // 2, 50))
    ##the buttons
    pygame.draw.rect(self.screen, blue, self.play_button , border_radius=10)
    pygame.draw.rect(self.screen, light_blue, self.quitgame_button , border_radius=10)
    ##draw button text
    play_text = self.font.render("Play", True, white)
    quitgame_text = self.font.render("Quit", True, white)
    ###code filled this bit in for me i thnik it as calcxualtion for where to draw buttons 
    self.screen.blit(play_text, (self.play_button.x + self.play_button.width // 2 - play_text.get_width() // 2, self.play_button.y + self.play_button.height // 2 - play_text.get_height() // 2))
    self.screen.blit(quitgame_text, (self.quitgame_button.x + self.quitgame_button.width // 2 - quitgame_text.get_width() // 2, self.quitgame_button.y + self.quitgame_button.height // 2 - quitgame_text.get_height() // 2))



play_button = pygame.Rect(100, 100, 200, 50)
quitgame_button = pygame.Rect(100, 200, 200, 50)
controls_button = pygame.Rect(100, 300, 200, 50)

def draw_buttons(self, screen):
    pygame.draw.rect(screen, (0, 255, 0), play_button)
    pygame.draw.rect(screen, (255, 0, 0), quitgame_button)
    pygame.draw.rect(screen, (0, 0, 255), controls_button)

    def handle_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_button.collidepoint(mouse_pos):
                    self.game_state = "playing"
                elif quitgame_button.collidepoint(mouse_pos):
                    self.running = False
                elif controls_button.collidepoint(mouse_pos):
                    self.game_state = "controls"    


def hover_buttons(rect, text):
    if rect.collidepoint(pygame.mouse.get_pos()):
        color = lightblue
    else:
        color = white

