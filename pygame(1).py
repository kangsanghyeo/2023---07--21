import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello, pygame!")

clock = pygame.time.Clock()
run = True
gb = [255, 255]

# 게임 루프
while run:
    # 1) 사용자 입력 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # 2) 게임 업데이트
    if gb[0] == 0:
        gb[0] = 255
        gb[1] = 255
    else:
        gb[0] -= 1
        gb[1] -= 1

    # 3) 게임 사태 그리기
    screen.fill(pygame.color.Color(gb[0],255,  gb[1]))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
