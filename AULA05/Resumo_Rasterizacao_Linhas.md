# Resumo: Investigação de Algoritmo de Rasterização de Linhas

**Romeo Noro Guterres**

---

### 1. Qual o nome do algoritmo encontrado?
**Algoritmo de Linha de Xiaolin Wu** (Xiaolin Wu's line algorithm).

### 2. Qual é a principal vantagem dele em relação ao DDA?
A principal vantagem deste algoritmo em relação ao DDA é a **qualidade visual superior**, pois ele aplica **antialiasing** (suavização) de forma nativa e muito eficiente. 

Enquanto o DDA (e também o Algoritmo de Bresenham) desenha linhas que frequentemente apresentam um efeito visual de "escadinha" (serrilhado ou *aliasing*) ao pintar pixels inteiros com 100% de opacidade, o algoritmo de Wu minimiza drasticamente esse problema. Ele desenha linhas que parecem perfeitamente retas e suaves ao olho humano, variando a intensidade luminosa (ou transparência) dos pixels de acordo com a precisão matemática da reta.

### 3. Como ele decide qual é o próximo pixel a ser pintado?
Diferente do DDA, que arredonda o valor e escolhe apenas um único pixel em cada passo, o algoritmo de Wu pinta **dois pixels adjacentes** (por exemplo, um acima e outro abaixo da posição matemática exata da linha) em cada iteração.

A decisão sobre como pintar esses pixels baseia-se na distância fracionária entre a reta matemática ideal e o centro matemático dos pixels da tela:
1. O algoritmo calcula a coordenada fracionária exata por onde a linha passa (ex: `Y = 3.25`).
2. A intensidade (ou opacidade) de cada um dos dois pixels pintados será inversamente proporcional à sua distância da reta ideal.
3. **Exemplo:** Como `3.25` está mais próximo do pixel `3` (75% de proximidade) do que do pixel `4` (25% de proximidade), o pixel da posição `3` é desenhado com 75% de brilho/opacidade, e o pixel `4` é desenhado com 25% de brilho/opacidade. Se a linha passasse exatamente no meio (`3.50`), ambos receberiam 50% de intensidade.

### 4. Lógica conceitual do processo (Opcional)
Abaixo está um pseudocódigo demonstrando a lógica central do cálculo de intensidade em cada passo:

```python
# Para cada ponto X ao longo do eixo principal da reta:

y_real = calcular_y_exato(x)  # Ex: 3.25
y_inteiro = int(y_real)       # Ex: 3 (Pixel inferior)
fracao = y_real - y_inteiro   # Ex: 0.25 (Distância do pixel inferior)

# O pixel inferior recebe a intensidade complementar (1 - 0.25 = 0.75 ou 75%)
desenhar_pixel(x, y_inteiro, opacidade = 1 - fracao)

# O pixel superior (y_inteiro + 1) recebe a intensidade da fração (0.25 ou 25%)
desenhar_pixel(x, y_inteiro + 1, opacidade = fracao)
