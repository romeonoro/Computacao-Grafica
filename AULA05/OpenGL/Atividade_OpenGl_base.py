
# Importa o pygame e constantes para manipular janela e eventos
import pygame
from pygame.locals import *

# Importa funções da biblioteca OpenGL para renderizar com PyOpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

# Estado do objeto escolhido pelo usuário (controla qual forma será exibida)
objeto_atual = None

# Posições iniciais dos objetos (usadas para movimentação)
cube_pos = [ -6.0, 0.0 ]
tri_pos  = [  0.0, 0.0 ]
pyr_pos  = [  6.0, 0.0 ]

# Zoom e rotação da cena (para visualização geral)
zoom = -15.0
rot_x = 0.0
rot_y = 0.0

# Configurações iniciais do OpenGL
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)          # Cor de fundo preta
    glClearDepth(1.0)                         # Profundidade máxima
    glEnable(GL_DEPTH_TEST)                  # Ativa teste de profundidade
    glDepthFunc(GL_LEQUAL)                   # Critério de profundidade
    glMatrixMode(GL_PROJECTION)              # Muda para matriz de projeção
    glLoadIdentity()
    gluPerspective(45.0, 1280.0 / 480.0, 0.1, 100.0)  # Perspectiva 3D
    glMatrixMode(GL_MODELVIEW)               # Volta para matriz de modelagem

# Reseta posições e transformações dos objetos
def reset_transformations():
    global cube_pos, tri_pos, pyr_pos, zoom, rot_x, rot_y
    cube_pos = [ -6.0, 0.0 ]
    tri_pos  = [  0.0, 0.0 ]
    pyr_pos  = [  6.0, 0.0 ]
    zoom = -15.0
    rot_x = 0.0
    rot_y = 0.0

# Renderiza um cubo 3D colorido
def draw_cube():
    
    #glPushMatrix / glPopMatrix: Serve para "isolar" cada objeto.
    #Sem isso, se você movesse o cubo 5 unidades para a direita, a pirâmide 
    #também começaria 5 unidades para a direita de onde deveria estar.
    glPushMatrix() # Salva a matriz de transformação atual na pilha (Checkpoint)
    
    glTranslatef(cube_pos[0], cube_pos[1], 0)
    glBegin(GL_QUADS)

    # Face traseira
    glColor3f(1, 0, 0)
    glVertex3f(1, 1, -1); glVertex3f(-1, 1, -1); glVertex3f(-1, -1, -1); glVertex3f(1, -1, -1)
    
    # Face frontal
    glColor3f(0, 1, 0)
    glVertex3f(1, -1, 1); glVertex3f(-1, -1, 1); glVertex3f(-1, 1, 1); glVertex3f(1, 1, 1)

    # Face direita
    glColor3f(0, 0, 1)
    glVertex3f(1, 1, 1); glVertex3f(1, 1, -1); glVertex3f(1, -1, -1); glVertex3f(1, -1, 1)

    # Face esquerda
    glColor3f(1, 1, 0)
    glVertex3f(-1, 1, -1); glVertex3f(-1, 1, 1); glVertex3f(-1, -1, 1); glVertex3f(-1, -1, -1)

    # Face superior
    glColor3f(0, 1, 1)
    glVertex3f(1, 1, 1); glVertex3f(-1, 1, 1); glVertex3f(-1, 1, -1); glVertex3f(1, 1, -1)

    # Face inferior
    glColor3f(1, 0, 1)
    glVertex3f(1, -1, -1); glVertex3f(-1, -1, -1); glVertex3f(-1, -1, 1); glVertex3f(1, -1, 1)

    glEnd()
    glPopMatrix() # Restaura a matriz original (descarta a translação do cubo)

# Renderiza um triângulo 2D
def draw_triangle():
    glPushMatrix() # Salva o estado da matriz
    glTranslatef(tri_pos[0], tri_pos[1], 0)
    glBegin(GL_TRIANGLES)
    glColor3f(1, 1, 0)
    glVertex3f(0, 2, 0)
    glVertex3f(-2, -2, 0)
    glVertex3f(2, -2, 0)
    glEnd()
    glPopMatrix() # Restaura o estado da matriz

# Renderiza uma pirâmide com base quadrada
def draw_pyramid():
    glPushMatrix() # Salva o estado da matriz
    glTranslatef(pyr_pos[0], pyr_pos[1], 0)
    
    # Lados
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)
    glVertex3f(0, 1, 0); glVertex3f(-1, -1, 1); glVertex3f(1, -1, 1)
    glColor3f(0, 1, 0)
    glVertex3f(0, 1, 0); glVertex3f(1, -1, 1); glVertex3f(1, -1, -1)
    glColor3f(0, 0, 1)
    glVertex3f(0, 1, 0); glVertex3f(1, -1, -1); glVertex3f(-1, -1, -1)
    glColor3f(1, 1, 0)
    glVertex3f(0, 1, 0); glVertex3f(-1, -1, -1); glVertex3f(-1, -1, 1)
    glEnd()

    # Base
    glBegin(GL_QUADS)
    glColor3f(1, 0, 1)
    glVertex3f(-1, -1, -1); glVertex3f(1, -1, -1); glVertex3f(1, -1, 1); glVertex3f(-1, -1, 1)
    glEnd()
    
    glPopMatrix() # Restaura o estado da matriz

# Lê teclas pressionadas e atualiza estado dos objetos conforme a opção escolhida
def handle_keys():
    global zoom, rot_x, rot_y
    keys = pygame.key.get_pressed()

    # Zoom e rotação globais
    if keys[K_z]: zoom += 0.2
    if keys[K_x]: zoom -= 0.2
    if keys[K_r]: rot_y += 2
    if keys[K_f]: rot_y -= 2
    if keys[K_q]: rot_x += 2
    if keys[K_e]: rot_x -= 2

    # Controle de posição por tipo de objeto
    if objeto_atual == 1:
        if keys[K_w]: cube_pos[1] += 0.1
        if keys[K_s]: cube_pos[1] -= 0.1
        if keys[K_a]: cube_pos[0] -= 0.1
        if keys[K_d]: cube_pos[0] += 0.1
    elif objeto_atual == 2:
        #insira aqui o código para as teclas do triangulo
        print("caso 2") #retire esse print após ajustar
   
    elif objeto_atual == 3:
         #insira aqui o código para as teclas do cubo
         print("caso 3")  #retire esse print após ajustar
         
         
    elif objeto_atual == 4:
        #insira aqui o código para as teclas da pyramide
        print("caso 4")  #retire esse print após ajustar
        
        
        
    elif objeto_atual == 5:
        #insira aqui o código para as teclas da movimentação dos 3 objetos juntos
        print("caso 5")  #retire esse print após ajustar
    
    
    
    elif objeto_atual == 6:
        # Controle individual
        #insira aqui o código para as teclas de movimentação separada de cada objeto, voce deve controlar cada um conforme 
        #as teclas sugeridas no arquivo passado com as instruções
        print("caso 6")  #retire esse print após ajustar



# Renderiza a cena com os objetos escolhidos
def draw_scene():
    glLoadIdentity()
    glTranslatef(0, 0, zoom)
    glRotatef(rot_y, 0, 1, 0)
    glRotatef(rot_x, 1, 0, 0)
    if objeto_atual == 1:
        draw_cube()
    elif objeto_atual == 2:
        draw_triangle()
    elif objeto_atual == 3:
        draw_cube()
        draw_triangle()
    elif objeto_atual == 4:
        draw_pyramid()
    elif objeto_atual in [5, 6]:
        draw_cube()
        draw_triangle()
        draw_pyramid()

# Função principal do programa
def main():
    global objeto_atual

    # Mostra o menu no terminal
    print("=== MENU DE FORMAS ===")
    print("1 - Cubo") 
    print("2 - Triângulo") 
    print("3 - Cubo + Triângulo") 
    print("4 - Apenas Pirâmide") 
    print("5 - Todos juntos (WASD para todos)") 
    print("6 - Todos com controle individual") 

    # Captura a escolha do usuário antes de abrir a janela
    try:
        objeto_atual = int(input("Escolha uma opção: ")) 
    except:
        print("Opção inválida!") 
        return

    # Agora inicia o Pygame e configura a janela OpenGL
    pygame.init()
    pygame.display.set_mode((1280, 480), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Trabalho 01 - Computação Gráfica")
    init()

    #reseta as transformacoes conforme a funcao usada
    reset_transformations()

    # Força a janela para frente no Windows
    try:
        import ctypes
        hwnd = pygame.display.get_wm_info()['window']
        ctypes.windll.user32.ShowWindow(hwnd, 5)
        ctypes.windll.user32.SetForegroundWindow(hwnd)
    except:
        pass  # Ignora em outros sistemas operacionais

    # Loop principal do programa
    running = True
    while running:
        for event in pygame.event.get():
            # Tecla 'esc' ou fechar a janela
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE): 
                running = False  #sai do programa

        #chama a funcao das teclas pressionadas
        handle_keys()

        # Limpa o buffer de cor (o que foi desenhado antes) e o buffer de profundidade (Z-buffer),
        # garantindo que a tela comece "limpa" para o próximo frame sem sobrepor imagens anteriores.
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #chama a funcao para desenhar a cena escolhida
        draw_scene()

        # Atualiza a janela com o que foi desenhado. 
        pygame.display.flip()
        # Pausa a execução por 10 milissegundos. Isso controla a velocidade do loop (FPS), 
        # evitando que a CPU consuma 100% de processamento sem necessidade.
        pygame.time.wait(10)

    pygame.quit()

# Executa o programa
if __name__ == "__main__":
    main()
