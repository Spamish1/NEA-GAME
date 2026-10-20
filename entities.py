import  pygame 
from settings import tile_size
class Player :
    def __init__(self,y_pos, x_pos , max_health ):
        self.player_yposition = y_pos
        self.player_xposition = x_pos 
        self.__player_maxhealth = max_health  ## player max health is private at this moment may not be in future 
        self.player_image_forward = pygame.image.load("player_images/up_frame_1.png") #  going t onned several for the plaeyr to turna round properly
        self.rect = self.image.get_rect()                     ### might need to make this player_image_forward instead of image and make it so that all the animations have it like this s o that they all have hitboxes 
        self.rect.x_pos = x_pos * tile_size
        self.rect.y_pos = x_pos * tile_size

    def update(self):
        keys = pygame.keys.get_pressed()     
        if keys(K_W):
            self.player.rect.x_pos -= 5







