import random
from GiaoDien import *
from Define import *

def init_matrix(ds):
    for i in range(4):
        for j in range(4):
            ds[i][j] = 0
    for k in range(2):
        add_block(ds)

def add_block(ds):
    while True:
        i = random.randint(0, 3)
        j = random.randint(0, 3)
        if (ds[i][j] == 0):
            break
    ds[i][j] = random.choice(VAL_CHOICE)


def output_ds(ds):
    print("======================")
    for i in range(4):
        for j in range(4):
            print(format(ds[i][j], "3d"), end='    ')
        print()


def update_diem(plus):
    global souce
    souce += plus
    pygame.draw.rect(menuScreen, BG_TEXT, (220, 10, 90, 40), )
    font = pygame.font.SysFont('Bahnschrift', 15)
    text = font.render(str(souce), True, (0, 0, 0))
    menuScreen.blit(text, (220, 18))


def getbest():
    file = open('BXH.txt')
    best = int(file.readline())
    pygame.draw.rect(menuScreen, BG_TEXT, (400, 10, 90, 40), )
    font = pygame.font.SysFont('Bahnschrift', 15)
    text = font.render(str(best), True, (0, 0, 0))
    menuScreen.blit(text, (400, 18))


def move_left(ds):
    dsdadichchuyen = []
    codichchuyen = False
    for i in range(4):
        for j in range(1, 4):
            if ds[i][j] == 0:
                continue
            for k in reversed(range(j)):
                if (ds[i][k] != 0):
                    x = i
                    y = k
                    break
            else:
                x = i
                y = j
            if (x, y) == (i, j):
                ds[i][0] = ds[x][y]
                ds[x][y] = 0
                codichchuyen = True
            else:
                if ds[i][j] == ds[x][y] and (x, y) not in dsdadichchuyen:
                    ds[x][y] *= 2;
                    ds[i][j] = 0
                    dsdadichchuyen.append((x, y))
                    update_diem(ds[x][y])
                    codichchuyen = True
                elif (y + 1 != j):
                    ds[x][y + 1] = ds[i][j]
                    ds[i][j] = 0
                    codichchuyen = True
    return codichchuyen


def move_right(ds):
    dsdadichchuyen = []
    codichchuyen = False
    for i in range(4):
        for j in reversed(range(3)):
            if ds[i][j] == 0:
                continue
            for k in range(j + 1, 4):
                if (ds[i][k] != 0):
                    x = i
                    y = k
                    break
            else:
                x = i
                y = j
            if (x, y) == (i, j):
                ds[i][3] = ds[x][y]
                ds[x][y] = 0
                codichchuyen = True
            else:
                if ds[i][j] == ds[x][y] and (x, y) not in dsdadichchuyen:
                    ds[x][y] *= 2;
                    ds[i][j] = 0
                    dsdadichchuyen.append((x, y))
                    update_diem(ds[x][y])
                    codichchuyen = True
                elif (y - 1 != j):
                    ds[x][y - 1] = ds[i][j]
                    ds[i][j] = 0
                    codichchuyen = True

    return codichchuyen


def move_up(ds):
    dsdadichchuyen = []
    codichchuyen = False
    for j in range(4):
        for i in range(1, 4):
            if ds[i][j] == 0:
                continue
            for k in reversed(range(i)):
                if (ds[k][j] != 0):
                    x = k
                    y = j
                    break
            else:
                x = i
                y = j
            if (x, y) == (i, j):
                ds[0][j] = ds[x][y]
                ds[x][y] = 0
                codichchuyen = True
            else:
                if ds[i][j] == ds[x][y] and (x, y) not in dsdadichchuyen:
                    ds[x][y] *= 2;
                    ds[i][j] = 0
                    dsdadichchuyen.append((x, y))
                    update_diem(ds[x][y])
                    codichchuyen = True
                elif (x + 1 != i):
                    ds[x + 1][j] = ds[i][j]
                    ds[i][j] = 0
                    codichchuyen = True
    return codichchuyen


def move_down(ds):
    dsdadichchuyen = []
    codichchuyen = False
    for j in range(4):
        for i in reversed(range(3)):
            if ds[i][j] == 0:
                continue
            for k in range(i + 1, 4):
                if (ds[k][j] != 0):
                    x = k
                    y = j
                    break
            else:
                x = i
                y = j
            if (x, y) == (i, j):
                ds[3][j] = ds[x][y]
                ds[x][y] = 0

                codichchuyen = True
            else:
                if ds[i][j] == ds[x][y] and (x, y) not in dsdadichchuyen:
                    ds[x][y] *= 2;
                    ds[i][j] = 0
                    dsdadichchuyen.append((x, y))
                    update_diem(ds[x][y])
                    codichchuyen = True
                elif (x - 1 != i):
                    ds[x - 1][j] = ds[i][j]
                    ds[i][j] = 0
                    codichchuyen = True
    return codichchuyen


def cannot_move(ds):
    for i in range(4):
        for j in range(4):
            if ds[i][j] == 0:
                return False
            if i > 0:
                if ds[i - 1][j] == ds[i][j]:
                    return False
            if i < 3:
                if ds[i + 1][j] == ds[i][j]:
                    return False
            if j > 0:
                if ds[i][j - 1] == ds[i][j]:
                    return False
            if j < 3:
                if ds[i][j + 1] == ds[i][j]:
                    return False

    return True


def isFull(ds):
    for i in range(4):
        for j in range(4):
            if (ds[i][j] == 0):
                return False
    return True


def isWin(ds):
    for i in range(4):
        for j in range(4):
            if (ds[i][j] == 2048):
                return True
    return False


def updateBXH(souce):
    files = open('BXH.txt')
    list = files.readlines()
    if (len(list) == 10 and int(list[len(list) - 1]) >= souce):
        return
    files = open('BXH.txt', 'w')
    list.append(str(souce) + '\n')
    list = [int(i) for i in list]
    list.sort(reverse=True)
    if len(list) > 10:
        del list[10:len(list)]
    list = [str(i) + '\n' for i in list]
    files.writelines(list)


def change(menuScreen: pygame.Surface, mouse: pygame.mouse, modes):
    if modes["Play"] == False and modes["Home"] == True:
        if WIDTH / 2 - 125 <= mouse[0] <= (WIDTH / 2 - 125 + 250) and 300 <= mouse[1] <= 350:
            pygame.draw.rect(menuScreen, BG_BLOCK2, (WIDTH / 2 - 125, 300, 250, 50), border_radius=8)
            playgame(menuScreen)
        else:
            pygame.draw.rect(menuScreen, BG_BLOCK, (WIDTH / 2 - 125, 300, 250, 50), border_radius=8)
            playgame(menuScreen)

        if WIDTH / 2 - 125 <= mouse[0] <= (WIDTH / 2 - 125 + 250) and 370 <= mouse[1] <= 420:
            pygame.draw.rect(menuScreen, BG_BLOCK2, (WIDTH / 2 - 125, 370, 250, 50), border_radius=8)
            rank(menuScreen)
        else:
            pygame.draw.rect(menuScreen, BG_BLOCK, (WIDTH / 2 - 125, 370, 250, 50), border_radius=8)
            rank(menuScreen)

        if WIDTH / 2 - 125 <= mouse[0] <= (WIDTH / 2 - 125 + 250) and 440 <= mouse[1] <= 490:
            pygame.draw.rect(menuScreen, BG_BLOCK2, (WIDTH / 2 - 125, 440, 250, 50), border_radius=8)
            drawquit(menuScreen)
        else:
            pygame.draw.rect(menuScreen, BG_BLOCK, (WIDTH / 2 - 125, 440, 250, 50), border_radius=8)
            drawquit(menuScreen)


if __name__ == '__main__':
    ds = [[0 for i in range(4)] for j in range(4)]
    souce = 0
    init_matrix(ds)
    # ds = [[32, 4, 0, 0], [512, 256, 8, 0], [2048, 64, 4, 0], [128, 32, 2, 2]]
    output_ds(ds)
    pygame.init()
    menuScreen = initWindown()
    setMenuScreen(menuScreen)
    pygame.display.update()
    clock = pygame.time.Clock()
    audio = pygame.mixer.Sound
    musicHome = audio('assets/music/SoundTheme.mp3')
    musicGameOver = audio('./assets/music/MusicGameOver.mp3')
    musicWin = audio('./assets/music/MusicWin.mp3')
    musicHome.play(10)

    game_over = False
    running = True
    modes = {"Play": False,
             "Home": True,
             "Bxh": False
             }
    win = False;
    while running:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIDTH / 2 - 125 <= mouse[0] <= (WIDTH / 2 - 125 + 250) and 300 <= mouse[1] <= 350 and modes[
                    "Home"] == True:
                    background(menuScreen)
                    thanhcongcu(menuScreen)
                    drawBlock(menuScreen, ds)
                    modes["Home"] = False
                    modes["Play"] = True
                    update_diem(0)
                    getbest()
                    if game_over:
                        drawgameover(menuScreen)
                        musicHome.stop()

                if WIDTH / 2 - 125 <= mouse[0] <= (WIDTH / 2 - 125 + 250) and 370 <= mouse[1] <= 420 and modes[
                    "Home"] == True:
                    bangxephang(menuScreen)
                    modes["Home"] = False
                    modes["Bxh"] = True
                if WIDTH / 2 - 125 <= mouse[0] <= (WIDTH / 2 - 125 + 250) and 440 <= mouse[1] <= 490 and modes[
                    "Home"] == True:
                    running = False
                if 22 <= mouse[0] <= 66 and 12 <= mouse[1] <= 52 and modes["Home"] == False:
                    if game_over and modes["Play"]:
                        musicHome.play()
                    modes["Play"] = False
                    setMenuScreen(menuScreen)
                    modes["Home"] = True

                if 69 <= mouse[0] <= 109 and 10 <= mouse[1] <= 50 and modes["Play"] == True:
                    if game_over:
                        musicHome.play()
                        game_over = False
                    souce = 0
                    init_matrix(ds)
                    update_diem(0)
                    getbest()
                    background(menuScreen)
                    drawBlock(menuScreen, ds)
                    pygame.display.update()
            if event.type == pygame.KEYDOWN and modes["Play"] == True and not game_over:
                dichuyen = False
                if event.key == pygame.K_LEFT:
                    dichuyen = move_left(ds)
                elif event.key == pygame.K_RIGHT:
                    dichuyen = move_right(ds)
                elif event.key == pygame.K_UP:
                    dichuyen = move_up(ds)
                elif event.key == pygame.K_DOWN:
                    dichuyen = move_down(ds)
                if dichuyen == False:
                    continue
                if not isFull(ds) and dichuyen == True:
                    add_block(ds)
                if isWin(ds) and win == False:
                    musicWin.play()
                    win = True

                output_ds(ds)
                drawmh(menuScreen, ds)

                if cannot_move(ds) and dichuyen == True:
                    musicHome.stop()
                    musicGameOver.play()
                    game_over = True
                    drawgameover(menuScreen)
                    updateBXH(souce)

            else:
                continue
        mouse = pygame.mouse.get_pos()
        change(menuScreen, mouse, modes)
        pygame.display.update()
