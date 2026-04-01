# Exercício 01: Pesquisa sobre Algoritmos de Rasterização de Círculos

**Aluno:** Romeo Noro Guterres <br>
**Professor:** André F. dos Santos

---

O objetivo desta pesquisa é apresentar e explicar dois métodos otimizados para o desenho de circunferências, distintos das soluções matemáticas básicas (Cartesiana e Paramétrica) vistas em aula.

## 1. Algoritmo de Ponto Médio para Círculos (Midpoint Circle Algorithm / Bresenham)

Este algoritmo é uma adaptação do Algoritmo de Bresenham para linhas, otimizado especificamente para o traçado de circunferências.

* **Principal Vantagem:** A sua maior vantagem é a extrema eficiência computacional. Diferente das soluções cartesiana e paramétrica que exigem cálculos pesados de ponto flutuante, raízes quadradas (Teorema de Pitágoras) ou funções trigonométricas (seno e cosseno), este algoritmo utiliza **apenas operações aritméticas simples com números inteiros** (adição, subtração e deslocamento de bits). Além disso, ele calcula apenas os pixels de um único octante (1/8 do círculo) e espelha os resultados para os outros sete octantes usando a simetria natural da circunferência, reduzindo o processamento em 87,5%.

* **Como decide qual pixel pintar:**
  O algoritmo avança pixel a pixel ao longo do eixo X (de 0 até o raio `R`). Em cada passo, ele precisa decidir se a coordenada Y deve ser mantida ou decrementada em 1. Para isso, ele avalia uma **variável de decisão** calculada no "ponto médio" exato entre os dois pixels candidatos (o pixel imediatamente ao lado e o pixel ao lado e abaixo). 
  Se esse ponto médio estiver *dentro* da circunferência matemática ideal, o perímetro real está mais próximo do pixel superior, então o Y é mantido. Se o ponto médio estiver *fora* da circunferência, o perímetro real está mais próximo do pixel inferior, então o Y é decrementado.

---

## 2. Algoritmo de Xiaolin Wu para Círculos (Wu's Anti-aliased Circle)

Trata-se de uma extensão do algoritmo de Xiaolin Wu para linhas, adaptado para desenhar circunferências.

* **Principal Vantagem:**
  A vantagem absoluta deste método é a **qualidade visual (Antialiasing)**. Os algoritmos baseados em inteiros (como o Ponto Médio) geram bordas serrilhadas (efeito "escadinha"), pois os pixels são limitados a uma grade quadrada. O algoritmo de Wu suaviza essas bordas, criando a ilusão ótica de um círculo perfeitamente redondo e liso, o que é fundamental em interfaces de usuário modernas e motores gráficos.

* **Como decide qual pixel pintar:**
  Em vez de acender um único pixel sólido por coordenada, o algoritmo de Wu pinta sempre **dois pixels adjacentes** na borda da curva em cada iteração. Ele calcula a distância fracionária exata entre a borda matemática ideal do círculo e os centros desses dois pixels. 
  A cor ou a opacidade (Alpha) distribuída para cada pixel é proporcional a essa distância. O pixel que estiver mais próximo da linha ideal recebe uma cor mais forte (maior opacidade), enquanto o pixel mais distante recebe uma cor mais fraca (maior transparência). Isso cria um degradê suave nas bordas da forma geométrica.
