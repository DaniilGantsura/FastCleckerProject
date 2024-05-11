import pygame
from random import randint

pygame.init()

p = (73, 30, 133)
mw = pygame.display.set_mode((500, 500))
mw.fill(p)
clock = pygame.time.Clock()


class Area():
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def new_color(self, n_color):
        self.fill_color = n_color

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)


class Label(Area):
    def set_text(self, text, fsize, text_color):
        self.image = pygame.font.Font(None, fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


cards = []
x = 50
for i in range(4):
    newcard = Label(x, 180, 70, 100, (0, 0, 0))
    newcard.set_text("Click", 30, (255, 0, 4))
    cards.append(newcard)
    x += 100
wait = 0
point = Label(20, 20, 150, 40, p)
point.set_text('Total: 0', 30, (0, 0, 0))
total = 0
while True:
    if wait == 0:
        wait = 40
        click = randint(0, 3)
        for i in range(4):
            cards[i].new_color((0, 0, 0))
            cards[i].fill()
            if i == click:
                cards[i].draw()
    else:
        wait -= 1
    point.draw()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                for i in range(4):

                    if cards[i].collidepoint(x, y):
                        if i == click:
                            cards[i].new_color((250, 0, 225))
                            total += 1
                            point.set_text(f'Total: {total}', 30, (0, 0, 0))


                        else:
                            cards[i].new_color((0, 4, 255))
                    cards[i].fill()

    pygame.display.update()
    clock.tick(40)