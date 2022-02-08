import pygame

name = ""
updateables = []
drawables = pygame.sprite.LayeredDirty
fps = 30

def set_fps(tempfps):
    global fps
    fps = tempfps
    return