import pygame
import sys
from game  import Game 
import setting


class Button():
    def __init__(self,image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(centre=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = self.screen.render(self.text_input, True ,"white" ) ## self.screen may not work here i may nedd fill or draw 
        self.text = _rect = self.text.get_rect(center=(self.x_pos, self.y_pos))


    def update(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.text, self.text_rect)


    def checkforinput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top):
          print("buuton press")   


    def changeColour(self, position):
        if position[0] in range(self.rct.left, self.rect.right) and position[1] in range(self.rect.top):
            self.text = self.screen.render(self.text_input ,True, "green")  # ##### all the self .scrren around ghere may ned to be replaced with some some of fot variable
        else:
            self.text = self.screen.render(self.text_input ,True, "white") 


button_surface = pygame.image.load("buton.png") ### nned to get an image from internet to act as my buttons for my menu 
button_surface = pygame.transform.scale(button_surface, (0 , 0))  ### the zeros may need to be changed if i nned to scale the image size later

button = Button(button_surface, 400, 300, "clicke me ")

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







      