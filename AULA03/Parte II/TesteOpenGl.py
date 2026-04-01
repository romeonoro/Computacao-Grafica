import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# EX7: Posição inicial centralizada no eixo X (valor original era -1.5)
x = 0 
y = 0 
r = 0

# EX8: Escala inicial do triângulo aumentada (valores originais eram 1)
ex = 2 
ey = 2 
ez = 2 

# EX10: Variável de controle de profundidade (eixo Z)
zoom = -6 

def init():
    # EX1: Define a cor de fundo da janela para branco (RGBA)
    glClearColor(1.0, 1.0, 1.0, 1.0) 

    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 640/480, 0.1, 100)
    
    glMatrixMode(GL_MODELVIEW)

def draw():
    glLoadIdentity()
    
    # EX10: Aplica a translação utilizando a variável de zoom no eixo Z
    glTranslatef(x, y, zoom)

    # EX2: Rotação exclusiva no eixo X (efeito de "cambalhota"). 
    # Descomente a linha abaixo e comente a do EX3 para ativar:
    # glRotatef(r, 1, 0, 0)  
    
    # EX3: Rotação simultânea nos eixos X e Y (efeito de giro diagonal a 45 graus)
    glRotatef(r, 1, 1, 0)  

    glScalef(ex, ey, ez)
    glBegin(GL_TRIANGLES)

    # EX4: Define a cor do triângulo para preto (RGB)
    glColor3f(0, 0, 0) 

    # EX5: Vértices do triângulo ampliados para formar um desenho maior
    glVertex3f(0, 2, 0)
    glVertex3f(-2, -2, 0)
    glVertex3f(2, -2, 0)

    glEnd()

def main():
    pygame.init()
    pygame.display.set_mode((640, 480), DOUBLEBUF | OPENGL)
    init()

    global x, y, r, ex, ey, ez, zoom

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                
                # EX9: Controles de movimentação horizontal invertidos
                if event.key == K_a:
                    x += 0.2  # 'A' move o objeto para a DIREITA
                if event.key == K_d:
                    x -= 0.2  # 'D' move o objeto para a ESQUERDA
                
                # Controles de movimentação vertical
                if event.key == K_w:
                    y += 0.2
                if event.key == K_s:
                    y -= 0.2
                
                # EX10: Controles de profundidade (Zoom)
                if event.key == K_z:
                    zoom += 0.2  # Aproxima (move no sentido positivo de Z)
                if event.key == K_x:
                    zoom -= 0.2  # Afasta (move no sentido negativo de Z)
            
            # Controles de escala com o Scroll do Mouse
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 4: # Scroll Up
                    ex += 0.2
                    ey += 0.2
                    ez += 0.2
                if event.button == 5: # Scroll Down
                    ex -= 0.2
                    ey -= 0.2
                    ez -= 0.2
                    
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw()

        pygame.display.flip()
        pygame.time.wait(10)

        # EX6: Rotação contínua no sentido anti-horário com velocidade aumentada
        r -= 10 

    pygame.quit()

if __name__ == "__main__":
    main()
