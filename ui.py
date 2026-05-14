
from settings import*
from Buttons import Button
pygame.font.init()
class UI:
    def __init__(self,display,background):
        self.display=display
        self.background=background
        self.x=H/2
        self.y=V/2
        
        ###
        self.font=pygame.font.Font("images\Oxanium-Bold.ttf",70)
        self.font2=pygame.font.Font("images\Oxanium-Bold.ttf",26)
        self.start_button=Button(self.display,self.x,self.y,"START","images\Oxanium-Bold.ttf","white","white")
        self.credits_button=Button(self.display,self.x,self.y+100,"CREDIT","images\Oxanium-Bold.ttf","white","white")
        self.quit_button=Button(self.display,self.x,self.y+200,"QUIT","images\Oxanium-Bold.ttf","white","white")
        ###
        self.text_surface=self.font.render("SPACE INVADER",True,"white")
        self.text_rect=self.text_surface.get_frect(center=(H/2,200))
        
        

    def draw(self):
       self.display.blit(self.background)
       self.display.blit(self.text_surface,self.text_rect)
       self.menu()
    def menu(self):
        
        self.start_button.draw_button()
        self.credits_button.draw_button()
        self.quit_button.draw_button()

    def clicked_buttons(self):
        return [self.start_button.clicked,self.credits_button.clicked,self.quit_button.clicked]


class Credit(UI):
    def __init__(self,display,background ):
        super().__init__(display,background)
        self.text_surface=self.font.render("CREDIT:",True,"white")
        self.text_rect=self.text_surface.get_frect(center=(H/2,200))

    def menu(self):
      text_surface=self.font.render(" -LARBI CHERIF ABDOLLAH\n -ISHAK\ KHALI\n -MOUAS AYOUB",True,"#73bdad",)
      text_rect=text_surface.get_frect(center=(H/2,V/2+50))
      text_surface1=self.font2.render(" press ENTER to go back to menu",True,"white")
      text_rect1=text_surface1.get_frect(topleft=(10,20))
      self.display.blit(text_surface,text_rect)
      self.display.blit(text_surface1,text_rect1)

    


    

        
        
            



   