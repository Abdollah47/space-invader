from settings import *
pygame.mixer.init()
class Player(pygame.sprite.Sprite):
    def __init__(self,groups,speed,image,frames1,frames2) :
        super().__init__(groups)
        
        self.frames1=frames1
        self.frames2=frames2
        self.current_frame=0
        self.image=image
        self.original_image=self.image
        self.rect=self.image.get_rect(center=(H/2,V/2))
        self.speed=speed
        self.direction=pygame.Vector2()
        ### cooldown
        self.can_shoot=True
        self.laser_shot_timer=0
        self.cooldown_duration=225
        ###mask
        self.mask=pygame.mask.from_surface(self.image)
        self.exaust=Exaust(all_sprites,exaust,self.rect.midleft)
        ###
        

        

      
    def update(self,dt):
        self.exaust.rect.midtop=self.rect.center-pygame.Vector2(2,0)
        keys=pygame.key.get_pressed()
        self.direction.x=int(keys[pygame.K_RIGHT])-int(keys[pygame.K_LEFT])
        self.direction.y=int(keys[pygame.K_DOWN])-int(keys[pygame.K_UP])
        self.direction=self.direction.normalize() if self.direction  else self.direction
        self.rect.center+=self.direction*self.speed*dt
        recent_keys=pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            Lazer((all_sprites,lazer_sprites),pygame.image.load("images/laser1.png"),self.rect.midtop,-1)
            lazer_sound.play()
            self.laser_shot_timer=pygame.time.get_ticks()
            self.can_shoot=False


        if self.direction==(0,0):
            self.current_frame+=100*dt
            self.image=self.original_image
            
        elif self.direction.x>0:
            self.current_frame=0
            self.image=self.frames1[self.current_frame]
        elif self.direction.x<0:
            self.current_frame=0
            self.image=self.frames2[self.current_frame]   

        
        

           
            
                

        self.shoot_timer()

    def shoot_timer(self):
        current_time=pygame.time.get_ticks()
        if not self.can_shoot:
            if current_time-self.laser_shot_timer>=self.cooldown_duration:
                self.can_shoot=True
        
            
           
     
               


class Star(pygame.sprite.Sprite):
    def __init__(self,groups,image):
        super().__init__(groups)
        self.image=image
        self.rect=self.image.get_rect(center=  (randint(0,H),randint(0,V)))
        

class Lazer(pygame.sprite.Sprite) :
    def __init__(self,groups,surface,pos,direction):
        super().__init__(groups)
        self.image=surface
        self.direction=direction
        self.rect=self.image.get_frect(center=pos)
        self.mask=pygame.mask.from_surface(self.image)


    def update(self,dt):
        self.rect.centery+=self.direction*400*dt
        if self.rect.bottom<0 or self.rect.top>V+20:
            self.kill()
        
        
        
class Meteor(pygame.sprite.Sprite):
    def __init__(self,groups,surface,pos,speed):
        super().__init__(groups)
        self.original_surf=surface
        self.image=self.original_surf
        self.rect=self.image.get_frect(midbottom=pos)
        self.mask=pygame.mask.from_surface(self.image)

        self.life_time=4000
        self.direction=pygame.math.Vector2(uniform(-0.5,0.5),1)
        self.speed=speed

        ####
        self.angle=0
        self.speed_rotate=randint(20,50)


    def update(self,dt):
        self.rect.center+=self.direction*self.speed*dt
       
        current_time=pygame.time.get_ticks()
        if self.rect.top>V:
            self.kill()
        self.angle+=self.speed_rotate*dt
        self.image=pygame.transform.rotozoom(self.original_surf,self.angle,1)
        self.rect=self.image.get_frect(center=self.rect.center)

class Explosion_Animation(pygame.sprite.Sprite):
    def __init__(self,groups,surface,pos):
        super().__init__(groups)    
        self.frames=surface
        self.current_frame=0
        self.image=self.frames[self.current_frame]
        self.rect=self.image.get_frect(center=pos)
        self.scale_ratio=0
        self.speed=0
    
    def update(self,dt):
        self.current_frame+=100*dt
        self.scale_ratio+=1*dt
        self.image=self.frames[int(self.current_frame)%len(self.frames)]
        if self.current_frame>=20:
                    self.current_frame=0
                    self.kill()

class Exaust(pygame.sprite.Sprite):
    def __init__(self, groups,surface,pos):
        super().__init__(groups)
        
        self.frames= surface
        self.current_frame=0
        self.image=self.frames[self.current_frame]
        self.rect=self.image.get_frect(center=pos)     

    def update(self,dt):
        self.current_frame+=100*dt
        self.image=self.frames[int(self.current_frame)%len(self.frames)]
        if self.current_frame>4:
            self.current_frame=0


class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups,player_surface,player_right_surface,player_left_surface,pos,player):
        super().__init__(groups)
        self.original_image=player_surface
        self.image=self.original_image
        self.rect=self.image.get_frect(center=pos)
        self.player=player
        self.current_frame=0
        self.frames1=player_right_surface
        self.frames2=player_left_surface
        self.mask=pygame.mask.from_surface(self.image)

        ###
        self.direction=pygame.math.Vector2(0,0)
        self.speed=randint(50,75)
        ##
        self.timer=pygame.time.get_ticks()



    def update(self,dt):     

        if self.direction==(0,0):
            self.current_frame+=100*dt
            self.image=self.original_image
            
        elif self.direction.x>0:
            self.current_frame=0
            self.image=self.frames1[self.current_frame]
        elif self.direction.x<0:
            self.current_frame=0
            self.image=self.frames2[self.current_frame]   

        
        self.path_find()   
        self.shooting_logic()  
        self.rect.center+=self.direction*self.speed*dt  
        


    def path_find(self):
       
       dx=self.rect.centerx-self.player.rect.centerx   
       dy=self.rect.centery-self.player.rect.centery
       if dx>0:
           self.direction.x=-1
       if dx<0:
           self.direction.x=1  
       if dx==0:
           self.direction.x=0
           self.rect.centerx=self.player.rect.centerx
           

       if dy<0:
           self.direction.y=1
       if self.rect.centery>=400:
           self.direction.y=0

    def shooting_logic(self):
        dx=self.rect.centerx-self.player.rect.centerx
        current_time=pygame.time.get_ticks()
        timer=-self.timer+current_time
        if timer>=randint(1000,1200):
            self.timer=current_time
            if abs(dx)<100:
                Lazer((all_sprites,enemy_lazer),lazer_enemy_surface,self.rect.midbottom,1)
                lazer_sound.play()

        
        

        
        

    


            
        

       

###improt          
lazer_enemy_surface=pygame.image.load(f"images/lazer2.png")
exaust=[pygame.image.load(f"images/exaust/{i}.png") for i in range(5)]
lazer_sound=pygame.mixer.Sound("audio\laser.wav")
lazer_sound.set_volume(0.5)
music_sound=pygame.mixer.Sound("audio\game_music.wav")
music_sound.play(-1)
damage_sound=pygame.mixer.Sound("audio\damage.ogg")
explosion_sound=pygame.mixer.Sound("audio\explosion.wav")
game_over_sound=pygame.mixer.Sound("audio/game_over.mp3")
##sprite groups
all_sprites=pygame.sprite.Group()  
meteor_sprite=pygame.sprite.Group()
lazer_sprites=pygame.sprite.Group()    
enemy_lazer=pygame.sprite.Group() 
enemies_sprites=pygame.sprite.Group() 


###
