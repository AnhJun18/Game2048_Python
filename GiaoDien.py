import pygame
from Define import *


def initWindown():
    menuScreen = pygame.display.set_mode((WIDTH, HEIGHT))
    icon = pygame.image.load('assets/images/icon.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('2048')
    menuScreen.fill(BG_SCREEN)
    return menuScreen


def setMenuScreen(menuScreen):
    menuScreen.fill(BG_SCREEN)
    game = pygame.image.load('assets/images/gameled.png')
    menuScreen.blit(game, (120, 0))

    bg = pygame.image.load('assets/images/logo.png')
    menuScreen.blit(bg, (120, 100))

    pygame.draw.rect(menuScreen, BG_BLOCK, (WIDTH / 2 - 125, 300, 250, 50), border_radius=8)
    font = pygame.font.SysFont('Bahnschrift', 32)
    text = font.render('Play Game', True, (0, 0, 0))
    menuScreen.blit(text, (WIDTH / 2 - 65, 302))

    pygame.draw.rect(menuScreen, BG_BLOCK, (WIDTH / 2 - 125, 370, 250, 50), border_radius=8)
    font = pygame.font.SysFont('Bahnschrift', 32)
    text = font.render('Rank', True, (0, 0, 0))
    menuScreen.blit(text, (WIDTH / 2 - 30, 375))

    pygame.draw.rect(menuScreen, BG_BLOCK, (WIDTH / 2 - 125, 440, 250, 50), border_radius=8)
    font = pygame.font.SysFont('Bahnschrift', 32)
    text = font.render('Quit', True, (0, 0, 0))
    menuScreen.blit(text, (WIDTH / 2 - 30, 445))


def thanhcongcu(menuScreen: pygame.Surface):
    pygame.draw.rect(menuScreen, BG_SCREEN, (0, 0, 530, 60), border_radius=8)
    pygame.draw.rect(menuScreen, BG_BLOCK, (20, 10, 40, 40), border_radius=8)
    home = pygame.image.load('assets/images/home.png')
    menuScreen.blit(home, (22, 12))

    pygame.draw.rect(menuScreen, BG_BLOCK, (70, 10, 40, 40), border_radius=8)
    home = pygame.image.load('assets/images/reset.png')
    menuScreen.blit(home, (69, 10))

    # khung in điểm hiện tại
    pygame.draw.rect(menuScreen, BG_TEXT, (155, 10, 160, 40), border_radius=5)
    font = pygame.font.SysFont('Bahnschrift', 15)
    text = font.render('Score:', True, (0, 0, 0))
    menuScreen.blit(text, (166, 18))

    # khung in điểm cao nhất
    pygame.draw.rect(menuScreen, BG_TEXT, (330, 10, 160, 40), border_radius=5)
    font = pygame.font.SysFont('Bahnschrift', 15)
    text = font.render('Best: ', True, (0, 0, 0))
    menuScreen.blit(text, (341, 18))


def background(menuScreen: pygame.Surface) -> None:
    pygame.draw.rect(menuScreen, NEN, (0, 60, 530, 530))
    for i in range(COLS):
        for j in range(LINE):
            rect = (i * 130 + 10, j * 130 + 70, 116, 116)
            pygame.draw.rect(menuScreen, BG_BLOCK, rect, border_radius=8)


def drawText(menuScreen: pygame.Surface, rect: pygame.Rect, val):
    font = pygame.font.Font('assets/fonts/ClearSans-Bold.ttf', FRONT_SIZE[val])
    text = font.render(str(val), True, (250, 250, 245))
    if val >= 2048:
        text = font.render(str(val), True, (255, 120, 20))
    text_x = rect.center[0] - text.get_rect().width // 2
    text_y = rect.center[1] - text.get_rect().height // 2 - 5
    menuScreen.blit(text, (text_x, text_y))


def drawBlock(menuScreen: pygame.Surface, ds) -> None:
    for i in range(COLS):
        for j in range(LINE):
            val = ds[i][j]
            if val != 0:
                rect = pygame.Rect(j * 130 + 10, i * 130 + 70, 116, 116)
                pygame.draw.rect(menuScreen, BLOCK_COLORS[val], rect, border_radius=8)
                drawText(menuScreen, rect, val)


def drawmh(menuScreen: pygame.Surface, ds):
    background(menuScreen)
    drawBlock(menuScreen, ds)


def drawgameover(menuScreen: pygame.Surface):
    menuScreen1 = menuScreen.convert_alpha()
    menuScreen1.fill((255, 160, 122, 150))
    font = pygame.font.Font('assets/fonts/ClearSans-Bold.ttf', 30)
    text = font.render('Game  Over', True, (0, 0, 10))
    menuScreen1.blit(text, (175, 200))
    menuScreen.blit(menuScreen1, (0, 60))
def bangxephang(menuScreen: pygame.Surface,) -> None:
    menuScreen.fill((0,0,0))
    pygame.draw.rect(menuScreen, (102, 205, 170), (100, 60, 330, 460))
    pygame.draw.rect(menuScreen, (176, 224, 230), (180, 30, 170, 50), border_radius=8)
    game = pygame.image.load('assets/images/topbxh.png')
    menuScreen.blit(game, (200, 30))

    pygame.draw.rect(menuScreen, BG_BLOCK, (20, 10, 40, 40), border_radius=8)
    home = pygame.image.load('assets/images/home.png')
    menuScreen.blit(home, (22, 12))

    file = open('BXH.txt')
    list = file.readlines()
    for i in range(len(list)):
        if i< 3:
            pygame.draw.rect(menuScreen, COLORBXH[i], (145, 90 + 43 * i, 240, 38), border_radius=10)
            font = pygame.font.SysFont('Bahnschrift', 20)
            text = font.render(list[i].rstrip(), True, (0, 0, 0))
            menuScreen.blit(text, (250, 93 + 43 * i))
        else:
            pygame.draw.rect(menuScreen, (240,248,255),(145, 90 + 43*i,240,38), border_radius=10)
            font = pygame.font.SysFont('Bahnschrift', 20)
            text = font.render(list[i].rstrip(), True, (0, 0, 0))
            menuScreen.blit(text, (250, 93 + 43*i))