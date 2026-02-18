import matplotlib.pyplot as plt
import numpy as np

# Definição dos vetores
a_origem = np.array([4, 1])  # Ponto inicial do vetor a
ponta_a = np.array([2, 3])  # Ponto final do vetor a (deslocamento)
# comentario de como funciona
# ponta_a = a_origem (x,y) + ponta_a (x,y) = (4,1) + (2,3) = (6,4) = este valor sera o ponto no grafico

b_origem = np.array([-3, -1])  # Ponto inicial do vetor b
ponta_b = np.array([-5, 4])  # Ponto final do vetor b (deslocamento)
#comentario de como funciona
#ponta_b = b_origem (x,y) + ponta_b (x,y) = (-3,-1) + (-5,4) = (-8,3) = este valor sera o ponto no grafico

# Criando o gráfico
# 'fig' representa a figura geral do gráfico e pode ser usado para ajustes globais.
# 'ax' é o objeto do eixo onde os vetores serão desenhados.
fig, ax = plt.subplots()
ax.axhline(0, color='black', linewidth=0.5)  # Linha do eixo X
ax.axvline(0, color='black', linewidth=0.5)  # Linha do eixo Y
ax.grid(True, linestyle='--', linewidth=0.5)  # Grade do gráfico
ax.set_xlim(-10, 10)  # Ajuste do limite do eixo X
ax.set_ylim(-10, 10)  # Ajuste do limite do eixo Y
ax.set_xlabel('Eixo X')  # Rótulo do eixo X
ax.set_ylabel('Eixo Y')  # Rótulo do eixo Y
ax.set_title('Representação dos Vetores no Plano Cartesiano')  # Título do gráfico

# Plotando os vetores corretamente
# O método quiver desenha os vetores no gráfico:
# - O primeiro e segundo parâmetros representam a origem do vetor (coordenadas iniciais no plano cartesiano).
# - O terceiro e quarto parâmetros representam o deslocamento (o comprimento e a direção da flecha do vetor).
# - angles='xy' mantém a orientação dos vetores corretamente.
# - scale_units='xy' e scale=1 garantem que os vetores sejam exibidos sem reescalonamento automático.
# - color define a cor do vetor.
# - label atribui um nome ao vetor para aparecer na legenda.
# quiver=flecha
ax.quiver(a_origem[0], a_origem[1], ponta_a[0], ponta_a[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Vetor a')
ax.quiver(b_origem[0], b_origem[1], ponta_b[0], ponta_b[1], angles='xy', scale_units='xy', scale=1, color='green', label='Vetor b')

# Legenda para identificação dos vetores
ax.legend()

# Exibir o gráfico
plt.show()
