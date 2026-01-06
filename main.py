import pygame


def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    img = pygame.image.load("res/cat.jpg")
    img = pygame.transform.scale_by(img, screen.height / img.height / 2)

    running = True
    while running:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False

        screen.fill(pygame.Color("black"))

        screen.blit(img, pygame.mouse.get_pos())

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
