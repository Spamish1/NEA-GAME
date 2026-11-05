import  pygame 
from settings import tile_size

class Player(pygame.sprite.Sprite) :
    def __init__(self,y_pos, x_pos , max_health ):
            super().__init__()
            self.image = pygame.image.load("player_images/up_frame_1.png")

            self.image.blit("player_images/up_frame_1.png")

        # Initialise the rect at position (x, y)
            self.rect = self.image.get_rect(topleft=(x_pos, y_pos))
            self._max_health = max_health
            self.player_image_forward = pygame.image.load("player_images/up_frame_1.png")

   # def update(self):
    #    keys = pygame.event.type == pygame.KEYDOWN ()     #keys = pygame.keys.get_pressed()     i am changing it say this in dev log
     #   if keys(K_w):
      #      self.player.rect.x_pos -= 5







