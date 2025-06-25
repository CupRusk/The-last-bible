import pygame, pygame_gui
from ui.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from ui.ui import create_hello_button

def init_window():
    pygame.init()
    pygame.display.set_caption("The Last Bible")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    
    manager = pygame_gui.UIManager((800, 600))
    hello_button = create_hello_button(manager)
    hello_button 
    while running:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            manager.process_events(event)
        
        
        

        screen.fill((30, 30, 30)) 
        manager.update(time_delta)
        manager.draw_ui(screen)

        pygame.display.flip()  
        clock.tick(FPS)        # Ограничение FPS

    pygame.quit()
