import pygame 
pygame.init()
import settings


def draw_menu(self,screen, background_colour):
    screen.fill(background_colour)
    ### to draw th etile and buttons may need to come back to it later to chasng e things make it looks nicer 
    title = self.font.render(title, True, settings.white)
    self.screen.blit(title, (settings.screen_width // 2 - title.get_width() // 2, 50))
    ##the buttons
    pygame.draw.rect(self.screen, settings.blue, self.play_button , border_radius=10)
    pygame.draw.rect(self.screen, settings.blue, self.quitgame_button , border_radius=10)
    ##draw button text
    play_text = self.font.render("Play", True, settings.white)
    quitgame_text = self.font.render("Quit", True, settings.white)
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





