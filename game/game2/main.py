import pygame as pg
import serial
import threading
import queue
import random
import time

import os
# serve per salvare in un file txt lo score migliore in modo che rimanga sempre 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BEST_FILE = os.path.join(BASE_DIR, "best_score.txt")

# CARICA BEST SCORE


if os.path.exists(BEST_FILE):
    try:
        with open(BEST_FILE, "r") as f:
            BEST_SCORE = int(f.read())
    except:
        BEST_SCORE = 0
# CONFIG
 
WIDTH = 1200
HEIGHT = 800

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

pg.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Microbit Space Shooter")

clock = pg.time.Clock()

# QUEUE

q = queue.Queue()

# PLAYER

player = pg.Rect(WIDTH//2, HEIGHT-100, 80, 40)

player_speed = 0
gamma = 0.15

# BULLETS

bullets = []

# ENEMIES

enemies = []
enemy_timer = 0

score = 0

# SERIAL THREAD

class Read_Microbit(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True

    def terminate(self):
        self.running = False

    def run(self):

        port = "COM6"

        s = serial.Serial(port, 115200)

        shoot = 0

        while self.running:

            try:

                data = s.readline().decode(errors="ignore").strip()

                print(data)

                # sparo
                if data == "SHOOT":

                    q.put((0, 1))

                # movimento
                else:

                    x = int(data)

                    q.put((x, 0))

            except Exception as e:
                print(e)

            time.sleep(0.01)

# START THREAD

rm = Read_Microbit()
rm.start()

# FONT

font = pg.font.Font(None, 40)

# GAME LOOP

running = True

while running:

    # EVENTS

    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False

    # READ QUEUE

    if not q.empty():

        x, shoot = q.get()

        # movimento navicella
        player_speed = (1-gamma) * player_speed + x / 3000

        player.x += int(player_speed * 20)

        # sparo
        if shoot == 1:

            bullet = pg.Rect(
                player.centerx - 5,
                player.top,
                10,
                20
            )

            bullets.append(bullet)

    # LIMITI SCHERMO

    if player.left < 0:
        player.left = 0

    if player.right > WIDTH:
        player.right = WIDTH

    # MOVE BULLETS

    for bullet in bullets:
        bullet.y -= 10

    bullets = [b for b in bullets if b.y > 0]

    # SPAWN ENEMIES

    enemy_timer += 1

    if enemy_timer > 30:

        enemy = pg.Rect(
            random.randint(0, WIDTH-50),
            0,
            50,
            50
        )

        enemies.append(enemy)

        enemy_timer = 0

    # MOVE ENEMIES

    for enemy in enemies:
        enemy.y += 5

    # COLLISIONS

    for bullet in bullets[:]:

        for enemy in enemies[:]:

            if bullet.colliderect(enemy):

                if bullet in bullets:
                    bullets.remove(bullet)

                if enemy in enemies:
                    enemies.remove(enemy)

                score += 1

    # GAME OVER

    for enemy in enemies:

        if enemy.colliderect(player):

            running = False

            if score > BEST_SCORE:

                BEST_SCORE = score

                with open(BEST_FILE, "w") as f:
                    f.write(str(BEST_SCORE))

    # DRAW

    screen.fill(BLACK)

    # player
    pg.draw.rect(screen, WHITE, player)

    # bullets
    for bullet in bullets:
        pg.draw.rect(screen, RED, bullet)

    # enemies
    for enemy in enemies:
        pg.draw.rect(screen, GREEN, enemy)

    # score
    text = font.render(f"Score: {score}", True, WHITE)
    text2 = font.render(f"Score best: {BEST_SCORE}", True, WHITE)

    screen.blit(text, (20,20))
    screen.blit(text2, (20,60))

    pg.display.flip()

    clock.tick(60)

# CLOSE

rm.terminate()
rm.join()

pg.quit()