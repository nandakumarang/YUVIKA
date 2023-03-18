from this import s
from rdkit import Chem
from rdkit.Chem import Draw
import pygame
from urllib.request import urlopen
from urllib.parse import quote
import pubchempy as pcp
from rdkit.Chem.rdMolDescriptors import CalcMolFormula
import re

class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

def get_formula(smiles):

    mol = Chem.MolFromSmiles(smiles)
    formula = CalcMolFormula(mol)
    print("Formula: "+ formula)
    return formula



def get_mass(smiles):

    mol = Chem.MolFromSmiles(smiles)
    formula = CalcMolFormula(mol)

    parts = re.findall("[A-Z][a-z]?|[0-9]+", formula)
    mass = 0
    print(parts)
    for index in range(len(parts)):
        if parts[index].isnumeric():
            continue

        atom = Chem.Atom(parts[index])
        multiplier = int(parts[index + 1]) if len(parts) > index + 1 and parts[index + 1].isnumeric() else 1
        mass += atom.GetMass() * multiplier

    return mass

filename = ""



def draw_text(text,font,text_col,x,y):
    t = font.render(text,True,text_col)
    surface.blit(t,(x,y))

# Starting pygame   
pygame.init()
displayWidth = 1280
displayHeight = 720
surface= pygame.display.set_mode((displayWidth, displayHeight ))
pygame.display.set_caption('Structure of ')
#displayImage = pygame.image.load(filename)
base_font = pygame.font.Font(None,40)
base_font2 = pygame.font.Font(None,45)   #Base font sytle and size
user_text = ""
#drawing rectangle
input_rect = pygame.Rect(700,350,140,32)
colour = pygame.Color('white')

#load button images
start_img = pygame.image.load('startbt.png').convert_alpha()
exit_img = pygame.image.load('exit.png').convert_alpha()

#create button instances
start_button = Button(550, 500, start_img, 0.4)
exit_button = Button(1200,50 , exit_img, 0.1)

#Background image
background = pygame.image.load("bgtemp (1).jpg")

temp = "open"

run = True
#This function creates the chemical structure......
def Structure(cname):
    identifiers  = []
    identifiers.append(cname)
    exit_button = Button(1200, 50, exit_img, 0.1)

    def CIRconvert(ids):
        try:
            results = pcp.get_compounds(ids, 'name')
            print(results) 
            for compound in results:
                s = compound.isomeric_smiles
                print (s)
                return s
        except:
            return 'Did not work'

    index = 0
    l= []
    for ids in identifiers:
        l.append(CIRconvert(ids))

    for mysmiles in l :

        if mysmiles != "did not work" :
        
            filename = 'image' + str(index) +'.png'
            Draw.MolToFile( Chem.MolFromSmiles(mysmiles), filename )
            index += 1   
            mass = get_mass(mysmiles)
            formula = get_formula(mysmiles)     
        
    pygame.init()
    displayWidth = 1280
    displayHeight = 720
    surface= pygame.display.set_mode((displayWidth, displayHeight ))
    pygame.display.set_caption('Structure of '+ cname)
    displayImage = pygame.image.load(filename)
    titleImage = pygame.image.load("titlelogo.png")
    width1 = titleImage.get_width()
    height1 = titleImage.get_height()
    scale = 0.5
    reImage = pygame.transform.scale(titleImage, (int(width1 * scale), int(height1 * scale)))
    
    while True : 
  
        surface.fill((255,255,255)) 
        surface.blit(background,(0,0))
        surface.blit(displayImage, (50,250)) 
        surface.blit(reImage, (415,20))
        draw_text("Details about "+user_text,base_font,(255,255,255),500,300)
        draw_text("Mass of "+user_text+": "+str(mass)+" g/mole",base_font,(255,255,255),500,380)
        draw_text("Formula of "+user_text+": "+formula,base_font,(255,255,255),500,480)
        for event in pygame.event.get() : 
   
            if event.type == pygame.QUIT : 
   
                pygame.quit()  
                quit() 
            if exit_button.draw(surface):
                print('EXIT')
                pygame.quit()
            pygame.display.update()   



#Main program
while run :
    for event in pygame.event.get() :
   
        if event.type == pygame.QUIT : 
            run = False
        #For checking key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[0:-1]
            else:
                user_text += event.unicode 
        if start_button.draw(surface):
            print('START')
            temp = "go"
        
        if exit_button.draw(surface):
            print('EXIT')
            temp = "Exit"
 
    if temp == "open":
        surface.fill((0,0,0))

        surface.blit(background,(0,0))
        text_surface = base_font.render(user_text,True,(255,255,255))
        surface.blit(text_surface,(input_rect.x + 10,input_rect.y + 5))
        titleImage = pygame.image.load("titlelogo.png")
        width1 = titleImage.get_width()
        height1 = titleImage.get_height()
        scale = 0.5
        reImage = pygame.transform.scale(titleImage, (int(width1 * scale), int(height1 * scale)))
        surface.blit(reImage, (415,20))


        text_surface3 = base_font2.render("Enter your Compound name and click on start to get details",True,(255,255,255))
        surface.blit(text_surface3,(200,270))
        text_surface2 = base_font.render("Compound Name:",True,(255,255,255))
        surface.blit(text_surface2,(400,350))
        input_rect.w = max(150,text_surface.get_width() + 15)
        pygame.draw.rect(surface,colour,input_rect,2)
        if start_button.draw(surface):
            print('START')
            
        
        if exit_button.draw(surface):
            print('EXIT')

        pygame.display.update()
        
    if temp == "go":
        Structure(user_text)
    if temp == "Exit":
        run = False
    

    
          
    
pygame.quit()
