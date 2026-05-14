from settings import*
pygame.font.init()
pygame.display.init()
class Button:
    def __init__(self,display,x,y,text,font,rect_color,font_color):
        self.display=display

        self.x=x
        self.y=y
        self.pos=(x,y)
        ###
        self.font=pygame.font.Font(font,45)
        self.text=text
        self.rect_color=rect_color
        self.original_color=self.rect_color
        self.font_color=font_color
        self.original_font_color=self.font_color

        ###
        self.text_surface=self.font.render(self.text ,True,self.font_color)
        self.text_rect=self.text_surface.get_frect(center=self.pos)
        self.outer_rect=self.text_rect.inflate(45,27).move(0,-5)
        ###
        self.clicked=False
        
        
        

   

    def draw_button(self)   :
       self.update_button()
       
       pygame.draw.rect(self.display,self.rect_color,self.outer_rect,7,3)
       self.display.blit(self.text_surface,self.text_rect)



    def update_button(self):
       mouse=pygame.mouse
       mouse_pos=mouse.get_pos()   
       mouse_clicked=mouse.get_pressed()
       collided=pygame.FRect.collidepoint(self.outer_rect,mouse_pos)

       if collided:
           self.rect_color="#73bdad"
           self.font_color="#73bdad"
          
       else:
           self.rect_color=self.original_color   
           self.font_color= self.original_font_color

       

       if collided and mouse_clicked[0]:
           self.rect_color="#98f5e1"
           self.font_color="#98f5e1"
           self.clicked=True
       else:
           self.clicked=False   
       self.text_surface=self.font.render(self.text ,True,self.font_color)    





       
  
          
       