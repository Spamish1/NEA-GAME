import  pygame 
from settings import tile_size
class Player( pygame.sprite.Sprite) :
    def __init__(self,y_pos, x_pos , max_health ):
      super().__init__()
      self.image = pygame.Surface((32,32))    ####going to have t oput player over red square or make red square invisible either one to make player image the only one seen 
      self.image.fill((255,0,0))

    #Initialise the rect at position(x,y)
      self.rect = self.image.get_rect(topleft=(x_pos,y_pos))
      self.__max_health = max_health 
      self.player_xpos = x_pos
      self.player_ypos = y_pos




  







