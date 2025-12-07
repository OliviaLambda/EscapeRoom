import pygame

class Candle(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, name):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (176, 352))
        self.rect = self.image.get_rect(center=(x, y))
        self.name = name

class TextBox(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (960, 540))
        self.rect = self.image.get_rect(center=(x, y))