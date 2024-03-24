import pygame
import json
def draw_text(text, font, x, y, color, screen):
    '''
    In PyGame, text is drawn in two steps:
      1. Render the text on a temporary surface
      2. Draw the text surface on the screen buffer
    '''
    # Render the text on a temporary surface
    text_surface = font.render(text, True, color)
    
    # Get the rectangle of the text surface. Also, 
    #   Center the text at (x, y).
    #   If we don't center the text, then the default position 
    #     is at the top left corner of the text surface
    text_rect = text_surface.get_rect(center=(x, y))
    
    # Finally draw the text surface on the given screen buffer
    screen.blit(text_surface, text_rect)
    
def read_scores( file_name):
  lst = []
  with open(file_name, "r+") as f:
      file = f.readlines()
      for i in file:
          data = i.rstrip("\n").split(":")
          data[1] = int(data[1])
          lst.append(data)
  return lst
      
def get_character_images():
  with open('assets/images/spritesheet.json', 'r') as json_file:
    data = json.load(json_file)
  new_dic = {}
  for i in data["frames"]:
    if "char" in i:
      new_dic[i] = data["frames"][i]["frame"]
      
  return new_dic
print(get_character_images())

