import pygame
import sys
from functions import *
from config import *
import torch
from torch import nn
from CNN import CNN

pygame.font.init()

screen = pygame.display.set_mode(screen_dim)
clock = pygame.time.Clock()

grid = torch.zeros((grid_size, grid_size), dtype=torch.int)

model = CNN(
    conv_layers=nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=8, kernel_size=3,stride=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        ),
    dense_layers=nn.Sequential(
            nn.Linear(8*13*13, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, 10)
        )
)
model.load("../models/cnn_mnist_model.pth", is_eval=True)

timer = 0
prediction = 0

while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                grid = torch.zeros((grid_size, grid_size), dtype=torch.int)

    draw_grid(screen)
    draw(screen, grid)

    mouse_pos = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:
        click(mouse_pos, grid)

    if pygame.time.get_ticks() - timer >= 500:
        timer = pygame.time.get_ticks()
        X = grid.reshape(-1, 1, 28, 28).float()
        prediction = torch.argmax(model.predict(X), dim=1).item()

    draw_text(screen, 'Prediction: ' + str(prediction), 0, 0)

    pygame.display.update()
    clock.tick(FPS)

    timer += 1