import array

import moderngl
import pygame


def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 800), pygame.OPENGL | pygame.DOUBLEBUF)

    ctx = moderngl.create_context()

    img = pygame.image.load("res/cat.jpg")
    img = pygame.transform.scale_by(img, screen.height / img.height / 2)

    v0 = pygame.Vector2(0, 0.5)
    v1 = v0.rotate(120)
    v2 = v1.rotate(120)
    vbo = ctx.buffer(data=array.array('f', [
        v0.x, v0.y, 1, 0, 0,
        v1.x, v1.y, 0, 1, 0,
        v2.x, v2.y, 0, 0, 1,
    ]))

    with open("res/shaders/triangle.vert", "r") as f:
        vs = f.read()
    with open("res/shaders/triangle.frag", "r") as f:
        fs = f.read()

    program = ctx.program(vertex_shader=vs, fragment_shader=fs)

    vao = ctx.vertex_array(program, vbo, "a_pos", "a_color")

    running = True
    while running:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False

        screen.fill(pygame.Color("black"))

        screen.blit(img, pygame.mouse.get_pos())

        vao.render(mode=moderngl.TRIANGLES)

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
