# Resumo da Atividade: Interatividade com Objetos em OpenGL

Nesta atividade, o código base fornecido foi complementado para implementar a interatividade via teclado em 6 cenários distintos de renderização. O desafio principal foi preencher a lógica condicional (`elif`) da função `handle_keys()` para manipular a translação das formas geométricas.

### O que foi implementado:

* **Opções 1 a 4 (Movimentação Padrão):** Foi implementada a movimentação (cima, baixo, esquerda, direita) utilizando o padrão de teclas `WASD`. Para isso, os índices correspondentes dos arrays `cube_pos`, `tri_pos` e `pyr_pos` foram atualizados individualmente de acordo com a opção selecionada no menu.

* **Opção 5 (Movimentação em Conjunto):** As transformações dos três objetos foram vinculadas à mesma entrada. Ao pressionar `WASD`, os valores nos arrays do cubo, triângulo e pirâmide foram incrementados ou decrementados de forma simultânea, garantindo que todos se movessem em sincronia pela cena.

* **Opção 6 (Controle Individual):** O controle individual de cada entidade geométrica foi habilitado associando blocos condicionais únicos a teclas de atalho distintas para o mesmo frame de renderização:
  * **Cubo:** Controlado pelas teclas `I`, `K` (eixo Y) e `J`, `L` (eixo X).
  * **Triângulo:** Controlado pelas teclas `G`, `B` (eixo Y) e `V`, `N` (eixo X).
  * **Pirâmide:** Controlada pelas **Setas Direcionais** do teclado.

> **Nota sobre a Opção 6:** Durante a implementação, as instruções originais citavam o uso das teclas "1, K" para o controle do eixo Y do cubo. Para manter um layout ergonômico e mais intuitivo no teclado (o padrão direcional da mão direita), a tecla "1" foi substituída pela tecla "I" no código fonte (`K_i`).
