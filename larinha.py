import pygame
from pygame.locals import *
import random
import math

class Rhombus(pygame.sprite.Sprite): 
    def __init__(self, position, speed, color, size, boundaries):
        super().__init__()
        self.position = position
        self.speed = speed
        self.color = color
        self.size = size
        self.boundaries = boundaries
        self.gravity = 0.01  # Reduzindo a gravidade
        self.image = self.create_rhombus_image()

    def create_rhombus_image(self):
        image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        color = self.color
        half_size = self.size // 2
        pygame.draw.polygon(image, color, [(half_size, 0), (self.size, half_size),
                                           (half_size, self.size), (0, half_size)])
        return image

    def update(self):
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]

        if self.position[0] <= 0 or self.position[0] >= self.boundaries[2]:
            self.speed[0] = -self.speed[0]
        if self.position[1] <= 0 or self.position[1] >= self.boundaries[3]:
            self.speed[1] = -self.speed[1]

class Main:
    def __init__(self):
        self.windowWidth = 960
        self.windowHeight = 640
        self.boundaries = (0, 0, self.windowWidth, self.windowHeight)
        self.mouse = None
        self.gameObjects = []
        screenSize = (self.windowWidth, self.windowHeight)
        self.screen = pygame.display.set_mode(screenSize)
        self.running = False

    def start(self):
        pygame.init()
        self.running = True
        while self.running:
            self.update()
            self.draw()
        pygame.quit()

    def getRandomSpeed(self):
        vx = random.uniform(-0.5, 0.5)  # Reduzindo a velocidade
        vy = random.uniform(-0.5, 0.5)  # Reduzindo a velocidade
        return [vx, vy]

    def getRandomColor(self):
        r = random.randint(150, 255)
        g = random.randint(0, 150)
        b = random.randint(0, 150)
        a = 128
        return (r, g, b, a)

    def createFallingDiamond(self):
        position = [random.randint(0, self.windowWidth), random.randint(0, self.windowHeight)]
        speed = self.getRandomSpeed()
        color = self.getRandomColor()
        size = random.randint(20, 40)
        self.gameObjects.append(Rhombus(position, speed, color, size, self.boundaries))
    
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONUP:
                self.createFallingDiamond()

        for gameobject in self.gameObjects:
            gameobject.update()
        
        return

    def draw(self):
        self.screen.fill((0, 0, 0))
        
        for gameObject in self.gameObjects:
            self.screen.blit(gameObject.image, gameObject.position)
        
        pygame.display.update()
        return

mainGame = Main()
mainGame.start()


