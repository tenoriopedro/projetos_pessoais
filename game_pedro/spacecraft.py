import pygame
from pathlib import Path
from pygame.sprite import Sprite

IMAGE_SPACECRAFT = Path(__file__).parent / "files" / "spacecraft.png"


class Spacecraft(Sprite):
    """Classe para gerenciar a espaço nave"""

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        # Carregando a imagem da nave
        self.image = pygame.image.load(IMAGE_SPACECRAFT)
        self.image = pygame.transform.scale(
            self.image, (40, 40)
        )
        self.rect = self.image.get_rect()

        # Posicionando a nave na tela do jogo
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.spacecraft_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.spacecraft_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.spacecraft_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.spacecraft_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_spacecraft(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)