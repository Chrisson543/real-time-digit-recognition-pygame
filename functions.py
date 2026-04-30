from config import *
import pygame

def draw_grid(screen):
    for y in range(1, grid_size):
        for x in range(1, grid_size):
            pygame.draw.line(screen, WHITE, (0, (y * block_size) + gap), (screen_dim.x, (y * block_size) + gap))
            pygame.draw.line(screen, WHITE, (x * block_size, 0 + gap), (x * block_size, screen_dim.y ))


def draw(screen, grid):
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == 1:
                pygame.draw.rect(screen, WHITE, pygame.Rect(x * block_size, y * block_size, block_size, block_size))


def click(mouse_pos, grid):
    x, y = mouse_pos[0] // block_size, mouse_pos[1] // block_size
    gp = gap // block_size

    if x < grid_size and y < grid_size:
        if grid[y, x] != 1:
            grid[y, x] = 1

def draw_text(surface, text, x, y, size=gap, color=(255, 255, 255)):
    font = pygame.font.SysFont(None, size)
    rendered = font.render(text, True, color)
    surface.blit(rendered, (x, y))