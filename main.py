from settings import*
from classes import *
from ui import UI,Credit
import sys
        


def collision():
    global running

    collision_player=pygame.sprite.spritecollide(player,meteor_sprite,False,pygame.sprite.collide_mask)
    collision_player_lazer=pygame.sprite.spritecollide(player,enemy_lazer,False,pygame.sprite.collide_mask)
    if collision_player or collision_player_lazer:
        running=False
        music_sound.stop()
        time.sleep(0.3)
        game_over_sound.play()   
        time.sleep(1.5)
            

    for lazer in lazer_sprites:
        collision_lazer_enemy=pygame.sprite.spritecollide(lazer,enemies_sprites,True,pygame.sprite.collide_mask)
        collision_lazer=pygame.sprite.spritecollide(lazer,meteor_sprite,True,pygame.sprite.collide_mask)
        if collision_lazer or collision_lazer_enemy:
            lazer.kill()
            Explosion_Animation(all_sprites,explsion_frames,lazer.rect.center).update(dt)
            explosion_sound.play()


def enemy_despawn(diffucilty):
    total_number=0
    for enemy in enemies_sprites:
        total_number+=1
        if total_number>int(diffucilty):
            enemy.kill()
            
        
        
def display_text():
   
    font=pygame.font.Font("images/Oxanium-Bold.ttf",25)
    label=font.render(f"score: {current_time_1}",True,"#d9d0d4")
    label_rect=label.get_rect(midbottom=(H/2,V-50))
    surface.blit(label,label_rect)
    pygame.draw.rect(surface,"#d9d0d4",label_rect.inflate(56,43).move(3,-5),5,10)
        




####initializing
pygame.init()
H,V=1280,720
surface=pygame.display.set_mode((H,V))
pygame.display.set_caption("space invader!")
### variables
state="menu"
background=pygame.image.load("images/BG.png")
background=pygame.transform.scale(background,(H,V))
speed=400
difficulty=2
running=True
menu=UI(surface,background)
credit=Credit(surface,background)

clock=pygame.Clock()


#### IMPORTING
meteor_surface=pygame.image.load("images/meteor.png")
explsion_frames=[pygame.image.load(f"images/explosion/{i}.png") for i in range(11)]
###player
player_sprite_right=[pygame.image.load(f"images/player/right/{i}.png")for i in range(2)]
player_sprite_left=[pygame.image.load(f"images/player/left/{i}.png") for i in range(2)]
player_sprite=pygame.image.load(f"images/player/0.png").convert_alpha()
exaust=[pygame.image.load(f"images/exaust/{i}.png") for i in range(5)]
player=Player(all_sprites,300,player_sprite,player_sprite_right,player_sprite_left)
####blue
enemyBlue_right=[pygame.image.load(f"images/enmies/blue/right/{i}.png")for i in range(2)]
enemyBlue_left=[pygame.image.load(f"images/enmies/blue/left/{i}.png") for i in range(2)]
enemyBlue_sprite=pygame.image.load(f"images/enmies/blue/0.png").convert_alpha()
###red
enemyRed_right=[pygame.image.load(f"images/enmies/red/right/{i}.png")for i in range(2)]
enemyRed_left=[pygame.image.load(f"images/enmies/red/left/{i}.png") for i in range(2)]
enemyRed_sprite=pygame.image.load(f"images/enmies/red/0.png").convert_alpha()

lazer_enemy_surface=pygame.image.load(f"images/lazer2.png").convert_alpha()
###events
meteor_event=pygame.event.custom_type()
pygame.time.set_timer(meteor_event,500)

enemies_event=pygame.event.custom_type()
pygame.time.set_timer(enemies_event,randint(1000,1500))

#####



if __name__=="__main__":
    while running:
        current_time_1=pygame.time.get_ticks()//100
        dt=clock.tick()/1000
        
       

        
    
        
    ###
    
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                     
            if state=="game":

                if event.type==meteor_event:
                    Meteor((all_sprites,meteor_sprite),meteor_surface,(randint(0,H),0),speed)

                
                if event.type==enemies_event:
                    index=0
                    if current_time_1>=150:
                        difficulty+=0.07
                        speed=600
                        
                        choice([Enemy((all_sprites,enemies_sprites),enemyBlue_sprite,enemyBlue_right,enemyBlue_left,(randint(0,H),randint(-30,-20)) ,player),
                        Enemy((all_sprites,enemies_sprites),enemyRed_sprite,enemyRed_right,enemyRed_left,(randint(0,H),randint(-30,-20)),player)]
                            )

                
            
                    
           
        if state=="menu":
                menu.draw()
                buttons=menu.clicked_buttons()
                if buttons[0]:
                   state="game"
                   menu=None
                   
                elif buttons[1]:
                    credit=Credit(surface,background)
                    state="credit"
                    menu=None
                    
                    
                    

                elif buttons[2]:
                    pygame.quit()
                    sys.exit()
    


         

        
                     
                    

                        
                       
                    
                        


                
                
        
        elif state=="game":
            current_time=pygame.time.get_ticks()//100
            current_time_1=current_time
            

            speed+=uniform(0.1,0.4)
            if speed>=800:
                 speed=800

            surface.blit(background)
            all_sprites.draw(surface)
            display_text()
            collision()
            enemy_despawn(difficulty)          
        
            all_sprites.update(dt)
        
        elif state=="credit":
             credit.draw()
             if pygame.key.get_pressed()[pygame.K_RETURN]:
                 state="menu"
                 menu=UI(surface,background)    
                 credit=None
                 
                
                
            


        
        
        



            

        pygame.display.update()
    

    pygame.quit()
    time.sleep(2.5)
    sys.exit()




