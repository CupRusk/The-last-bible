import pygame_gui, pygame
from ui.settings import SCREEN_WIDTH, SCREEN_HEIGHT

def create_hello_button(manager):
    return pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 25), (200, 50  )),
        text='Привет',
        manager=manager
    )