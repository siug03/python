import pygame
import random


pygame.init()

#화면크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (제목창)
pygame.display.set_caption("컨닝왕")

bg = pygame.image.load("pygame/source/bg.png")

#이벤트 루프 - 종료까지 대기
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((random.randint(0, 254), random.randint(0, 254), random.randint(0, 254)))

    screen.blit(bg, (0, 0))
    pygame.display.update()
#종요처리
pygame.quit()