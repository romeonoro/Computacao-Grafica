import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Variáveis de Transformação Espacial
x, y = -1.5, 0  # Translação inicial (Eixos X e Y)
r = 0           # Rotação inicial (Ângulo em graus)
ex, ey, ez = 1, 1, 1  # Escala inicial (Eixos X, Y e Z)

def init():
    # Configuração de cor de fundo (Azul escuro: R=0, G=0, B=1, A=1)
    glClearColor(0, 0, 1, 1) 

    # Configurações de Profundidade e Sombreamento
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST) # Ativa o Z-Buffer (ocultação de faces invisíveis)
    glDepthFunc(GL_LEQUAL)
    glShadeModel(GL_SMOOTH)

    # Configuração da Câmera (Matriz de Projeção)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # gluPerspective(FOV, Aspect Ratio, Near Plane, Far Plane)
    gluPerspective(45, 640/480, 0.1, 100) 
    
    # Retorna para a matriz de manipulação de objetos
    glMatrixMode(GL_MODELVIEW)

def draw():
    # Reinicia as transformações para o frame atual
    glLoadIdentity() 

    # 1. Translação: Move o objeto na tela (Deslocado em Z para afastar a câmera)
    glTranslatef(x, y, -6)  

    # 2. Rotação: Gira o objeto no próprio eixo (Rotacionando apenas no eixo Y)
    glRotatef(r, 0, 1, 0)  

    # 3. Escala: Altera o tamanho do objeto
    glScalef(ex, ey, ez)  

    # --- Desenhando o Primeiro Triângulo ---
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)      # Cor: Vermelho
    glVertex3f(0, 1, 0)     # Vértice Superior
    glVertex3f(-1, -1, 0)   # Vértice Inferior Esquerdo
    glVertex3f(1, -1, 0)    # Vértice Inferior Direito
    glEnd()

    # === EX11: Adicionando um segundo triângulo deslocado no eixo X ===
    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)      # Cor: Verde
    # Vértices idênticos ao primeiro, mas somando +2 no eixo X
    glVertex3f(0 + 2, 1, 0) 
    glVertex3f(-1 + 2, -1, 0) 
    glVertex3f(1 + 2, -1, 0) 
    glEnd()

def main():
    pygame.init()
    # Inicializa a janela gráfica com suporte a OpenGL e Double Buffering
    pygame.display.set_mode((640, 480), DOUBLEBUF | OPENGL)
    init()

    global x, y, r, ex, ey, ez

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                
                # Controles de Translação (Movimentação XY)
                if event.key == K_a: x -= 0.2  # Esquerda
                if event.key == K_d: x += 0.2  # Direita
                if event.key == K_w: y += 0.2  # Cima
                if event.key == K_s: y -= 0.2  # Baixo
                
            if event.type == MOUSEBUTTONDOWN:
                # Controles de Escala via Scroll do Mouse
                if event.button == 4: # Scroll Up (Aumenta)
                    ex += 0.2
                    ey += 0.2
                    ez += 0.2
                if event.button == 5: # Scroll Down (Diminui)
                    ex -= 0.2
                    ey -= 0.2
                    ez -= 0.2
                    
        # Limpa os buffers de cor e profundidade a cada frame
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw()

        # Troca os buffers para exibir o frame renderizado
        pygame.display.flip()
        pygame.time.wait(10) # Pausa curta para limitar o framerate

        # Animação contínua: incrementa o ângulo para giro constante
        r += 3  

    pygame.quit()

if __name__ == "__main__":
    main()
