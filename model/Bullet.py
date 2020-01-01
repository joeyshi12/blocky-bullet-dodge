import pygame
from pygame.surface import Surface

from model.Observer import Observer


class Bullet(Observer):
    RADIUS: int = 10
    COLOUR: tuple = (100, 100, 255)

    display: Surface
    x: int
    y: int
    vx: int
    vy: int

    def __init__(self, display: Surface, pos: tuple, vel: tuple):
        self.display = display
        self.x, self.y = pos
        self.vx, self.vy = vel

    def update(self):
        """updates bullet position by adding vx to x and vy to y;
        if bullet hits wall, its velocity is reflected"""
        self.x += self.vx
        self.y += self.vy
        if self.x < 0:
            self.vx = abs(self.vx)
        if self.x > self.display.get_width():
            self.vx = -abs(self.vx)
        if self.y < 0:
            self.vy = abs(self.vy)
        if self.y > self.display.get_height():
            self.vy = -abs(self.vy)

    def draw(self):
        """draws bullet on display"""
        pygame.draw.circle(self.display, self.COLOUR, (self.x, self.y), self.RADIUS)
