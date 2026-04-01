# Relatório de Exercícios

Este documento detalha as modificações implementadas no arquivo `TesteOpenGl.py`, contemplando a resolução dos exercícios de 1 a 10 através da manipulação de estados do OpenGL e transformações geométricas.

| Exercício | Descrição da Alteração | Antes | Depois | Resultado Prático |
| :--- | :--- | :--- | :--- | :--- |
| **EX1** | Cor de Fundo da Janela | `glClearColor(0.0, 0.0, 0.0, 1.0)` | `glClearColor(1.0, 1.0, 1.0, 1.0)` | O fundo da área de renderização foi alterado de preto para branco absoluto. |
| **EX2** | Rotação no Eixo X | Eixo Y: `(r, 0, 1, 0)` | Eixo X: `(r, 1, 0, 0)` | O objeto deixou de girar horizontalmente e passou a rotacionar no sentido vertical ("cambalhota"). |
| **EX3** | Rotação Simultânea X e Y | Eixo X: `(r, 1, 0, 0)` | Eixos X e Y: `(r, 1, 1, 0)` | A combinação dos vetores resultou em um eixo de rotação diagonal de 45 graus. |
| **EX4** | Cor do Polígono | Amarelo: `(1, 1, 0)` | Preto: `(0, 0, 0)` | O triângulo foi renderizado em preto, gerando alto contraste com o fundo branco. |
| **EX5** | Ampliação dos Vértices | `(0,1,0)`, `(-1,-1,0)`, `(1,-1,0)` | `(0,2,0)`, `(-2,-2,0)`, `(2,-2,0)` | As coordenadas foram expandidas, dobrando o tamanho físico do triângulo na malha. |
| **EX6** | Sentido e Velocidade | `r += 3` (Anti-horário, lento) | `r -= 10` (Horário, rápido) | O giro foi invertido para o sentido horário e a velocidade angular foi triplicada. |
| **EX7** | Centralização Inicial | `x = -1.5` | `x = 0` | A translação inicial no eixo X foi anulada, instanciando o objeto no centro da tela. |
| **EX8** | Modificação da Escala | `ex=1, ey=1, ez=1` | `ex=2, ey=2, ez=2` | O objeto inicia a renderização com o dobro de sua proporção (escala 2x). |
| **EX9** | Inversão de Controles | `A` (-0.2), `D` (+0.2) | `A` (+0.2), `D` (-0.2) | A lógica de input foi invertida: a tecla `A` move para a direita e `D` move para a esquerda. |
| **EX10** | Câmera/Zoom (Eixo Z) | Sem controle de profundidade | `zoom = -6`, Teclas `Z` e `X` | Adicionada translação no eixo Z. `Z` aproxima o objeto do observador e `X` o afasta. |
