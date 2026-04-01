# Respostas aos Exercícios 
---

### EX11: Movimentação Sincronizada

> **Pergunta:** Ao pressionar as teclas de movimento, o que acontece com os dois triângulos? Por que eles se movem em sincronia?

**Resposta:**
Ao pressionar as teclas de movimento (`W`, `A`, `S`, `D`), ambos os triângulos se deslocam **simultaneamente e na mesma direção**. 

Eles se movem em sincronia porque a transformação de translação (`glTranslatef(x, y, -6)`) é aplicada à matriz de visualização logo no início da função `draw()`, imediatamente após o `glLoadIdentity()`. 

Como essa função altera o **estado global da matriz de transformação** antes que qualquer um dos triângulos seja desenhado, ela afeta tudo o que vem em seguida no pipeline de renderização daquele frame. Como não há um novo `glLoadIdentity()` ou operações de isolamento (como `glPushMatrix`/`glPopMatrix`) separando o desenho do primeiro triângulo do segundo, ambos herdam a mesma transformação espacial geométrica.

---

### EX13: Rotação Independente

> **Pergunta:** O que aconteceu? Qual a diferença entre o giro dos triângulos?

**Resposta:**
Os triângulos passaram a girar em **velocidades distintas**. O primeiro triângulo gira mais rápido que o segundo. 

Isso ocorreu devido à utilização de variáveis de rotação independentes com incrementos diferentes (por exemplo, `r += 3` para o primeiro e `r2 += 2` para o segundo). Isso demonstra como o **isolamento das matrizes** (utilizando `glLoadIdentity()` antes de desenhar cada forma) e o uso de variáveis de estado separadas permitem que cada objeto na cena tenha seu próprio comportamento de animação, de forma totalmente autônoma.

---

### EX14: Controle Total Desvinculado

> **Pergunta:** O que acontece? Consigo controlar cada triângulo em separado agora?

**Resposta:**
**Sim, agora temos controle total e independente sobre cada objeto da cena.** Como cada triângulo possui seu próprio conjunto de variáveis de estado (posição, rotação, escala e zoom) e as matrizes de transformação são zeradas individualmente com `glLoadIdentity()`, um objeto pode ser manipulado sem afetar o outro. 

Na prática, passamos a tratar cada elemento como uma entidade única dentro do ambiente 3D, facilitando a criação de cenas complexas. Agora podemos dar zoom, alterar a escala e mover cada triângulo de forma independente, utilizando os seguintes controles:

* **Triângulo 1:** Movimento (`W`, `A`, `S`, `D`) | Zoom (Scroll do mouse)
* **Triângulo 2:** Movimento (`I`, `J`, `K`, `L`) | Zoom (`C`, `V`)
