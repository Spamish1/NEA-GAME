import  pygame 
from settings import tile_size
class Player( pygame.sprite.Sprite) :
    def __init__(self,y_pos, x_pos , max_health ):                                          
      super().__init__()
      self.up1 =  pygame.image.load("player_images/up_frame_1.png" ).convert_alpha()
      self.up2 =  pygame.image.load("player_images/up_frame_2.png" ).convert_alpha()
      self.image =  pygame.image.load("player_images/idle_stand.png" ).convert_alpha()  ### need to make a seperate images for standing pose
      self.right2 =  pygame.image.load("player_images/right_frame_2.png" ).convert_alpha()
      self.right1 = pygame.image.load("player_images/right_frame_1.png" )
      self.down1 = pygame.image.load("player_images/down_frame_1.png" ).convert_alpha()   
      self.down2 = pygame.image.load("player_images/down_frame_2.png" ).convert_alpha()           ######   need to make an idle animation and have that as self .image so when hes not moving he jsy trsands adn have an else in the movemnt at he bottom for this animatioon
      self.left1 = pygame.image.load("player_images/left_frame_1.png" )
      self.left2 = pygame.image.load("player_images/left_frame_2.png" )
      self.image = pygame.transform.scale(self.image, (64,64))
      
      self.current_frame = 0 
                

        
      
      
                                     

    #Initialise the rect at position(x,y)
      self.rect = self.image.get_rect(topleft=(x_pos,y_pos))
      self.__max_health = max_health 
      self.player_xpos = x_pos
      self.player_ypos = y_pos




  







