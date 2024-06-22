from pygame import *

win_height = 500
win_width = 600

window = display.set_mode((win_width, win_height))
background_color = (200,255,255)
window.fill(background_color)


class GameSprite(sprite.Sprite):
    def __init__(self, player_img, player_x, player_y, width, height, speed):
        self.image = transform.scale(image.load(player_img), (width,height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed
        self.height = height

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < win_height - self.height:
            self.rect.y += self.speed

    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < win_height - self.height:
            self.rect.y += self.speed

paddle_1 = Player("racket.png", 30, 200, 50, 150, 4)
paddle_2 = Player("racket.png", win_width - 60, 200, 50, 150, 4)
ball = GameSprite("tenis_ball.png", 200, 200, 50, 50, 4)

game_over = False
FPS = 60
clock = time.Clock()
dx = ball.speed
dy = ball.speed
while not game_over:
    for e in event.get():
        if e.type == QUIT:
            game_over = True
        
    paddle_1.reset()
    paddle_2.reset()
    ball.reset()

    ball.rect.x += dx
    ball.rect.y += dy

    if ball.rect.x > win_width - 50 or ball.rect.x < 0:
        dx *= -1
    if ball.rect.y > win_height - 50 or ball.rect.y < 0:
        dy *= -1


    paddle_1.update_l()
    paddle_2.update_r()

    display.update()
    clock.tick(FPS)
