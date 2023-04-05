# Cubo Sigma - Alfredo e Marcelo


### Funcionalidade de código - 

Para rodar nosso programa, basta clonar o respositório onde este documento está localizado e rodar o arquivo *cubo.py*. É claro que isso é apenas verdade se você já possui as bibliotecas necessárias. Elas não são muitas, apenas duas: *numpy* (responsável por facilitar uito das contas de matrizes) e *pygame* (responsável pela tela que nos mostra o quadrado). Para instalar essas bibliotecas, basta digitar `pip install NOME_DA_BIBLIOTECA` em seu terminal.

O cubo é completamente controlável, com dois modos e direções possíveis. As direções são mais simples de serem explicadas. As teclas "a" (esquerda) e "d" (direita) direcionam o quadrado a se mover em relação ao eixo Y do pygame (nosso eixo X). As teclas "w" (cima) e "s" (baixo) direcionam o quadrado a se mover em relação ao eixo X do pygame (nosso eixo Y). As teclas "k" (anti-horário) e "f" (horário) direcionam o quadrado a se mover em relação ao eixo Z do pygame. O primeiro modo é o "laranja". Nessa situação, o cubo se apresenta com a cor laranja, e roda continuamente na direção escolhida, e muda de direção quando uma nova tecla é apertada. O segunda é o modo "azul", onde o cubo é azul e se move de maneira discreta, também na direção escolhida pelo operador. Há como mudar entre os modos utilizando a tecla "f", que inverte o modo no qual você se encontra. Para voltar ao estado inicial basta aperta "r", o botão de reset.

Há também como aumentar ou diminuir a distância focal da projeção, utilizando as setas do teclado. Para cima é mais, e para baixo é menos

Após essa extensa explicação, está na hora de se divertir e se maravilhar com essa experiência matemática cortezia de Marcelo Marchetto e João Alfredo. 



### Explicação Matemática - 
Em um sistema bi-dimensional, podemos utilizar uma das variáveis que nos são dadas como um ponto de âncora que se mantém estável, nos possibilitando encontrar o estado do outro ponto do array.

 Uma demonstração disso pode ser vista com uma câmera pinhole e um ponto a uma distância $d$ que possui $X_{0}$ e $Y_{0}$ como valores cardeais. Assim, montamos uma matriz da seguinte maneira:

$$
I = 
\begin{bmatrix}
X_{0} \\
Y_{0} \\
1
\end{bmatrix}
$$

O $1$ nessa matriz nos permite manter uma variável como sendo a distância do pinhole a projeção ($d$) durante o processo de multiplicação de matrizes. Mas, como conseguiríamos utilizar esse ponto para chegar no ponto transposto pelo pinhole? 

A reposta está na semelhança de triângulos. Um triângulo pode ser formado, com cateto adjacente que vale $Y_{0}$ e cateto oposto que vale $X_{0}$. Um outro triângulo também pode ser fomado, com com cateto adjacente que vale $Y_{p}$ e cateto oposto que vale $X_{p}$, os valores da projeção do ponto original. Esses triângulos são semelhantes e possuem os mesmos ângulos e, portanto, mesmas tangentes. Dessa maneira:

$$ Tg_{\theta} =  \frac{X_{0}}{Y_{0}} = \frac{X_{p}}{Y_{p}}$$

Isolando $X_{p}$ ficamos com: $\frac{X_{0} Y_{p}}{Y_{0}} = X_{p}$

Com isso, podemos criar uma variável auxiliar, denominada de $W_{p}$. Essa variável tem a função explícita de conseguir o $X_{p}$ de volta no final da operação. Ela tem o seguinte valor: $W_{p} = \frac{Y_{0}}{Y_{p}}$. Ela é o inverso da conta de isolarmos o $X_{p}$, portanto:

$$
X_{p}W_{p} = X_{0}
$$

Agora, temos os passos necessários para montar nossa matriz de transformação. Antes, temos que considerar como a saída do processo será. Com o que temos podemos calcular $X_{p}W_{p}$ (que é equivalente a $X_{0}$), $Y_{p}$ (que é equivalente à distância da superfície projetada ao pinhole) e $W_{p}$ (que é $\frac{Y_{0}}{Y_{p}}$). Dessa maneira, montando nossa matriz tranformação ($T$), temos:

$$
T = 
\begin{bmatrix}
1, 0, 0 \\
0, 0, -d \\
0, -\frac{1}{d}, 0, 
\end{bmatrix}
$$

Nossa matriz resultante ($R$) será da seguinte forma:

$$
R = 
\begin{bmatrix}
X_{p}W_{p} \\
Y_{p} \\
W_{p}
\end{bmatrix}
$$

Com isso, conseguimos extrair o $X_{p}$ do primeiro elemento da matriz, já que conhecemos o valor de $W_{p}$, assim, chegando no resultado esperado. 

O processo para as três dimensões não é tão diferentes. Quando isolamos os dois campos ($X$ e $Y$), vemos que eles podem ser indepentes se nós definirmos $Z$ como a variável estática. Nossas matrizes ficariam então:

$$
I = 
\begin{bmatrix}
X_{0} \\
Y_{0} \\
Z_{0} \\
1
\end{bmatrix}
$$

$$
T = 
\begin{bmatrix}
1,0,0,0 \\
0,1,0,0 \\
0,0,0,-d \\
0,0,-\frac{1}{d},0, 
\end{bmatrix}
$$

$$
R = 
\begin{bmatrix}
X_{p}W_{p} \\
Y_{p}W_{p}\\
Z_{p} \\
W_{p}
\end{bmatrix}
$$

A variável $Z_{p}$ nessa instância seria equivalente a distância do pinhole. Ambas as outras variáveis de entrada ($X_{0}$ e $Y_{0}$) agora seguem o padrão do $X_{0}$ do exemplo bi-dimensional. Isso ocorre pois estamos tecnicamente realizando duas semelhancas diferentes. A primeira é no plano $X$ e $Z$, portanto, o $X_{0}$ é igual a $\frac{X_{p} Z_{0}}{Z_{p}}$. A primeira é no plano $Y$ e $Z$, portanto, o $Y_{0}$ é igual a $\frac{Y_{p} Z_{0}}{Z_{p}}$. Podemos reescrever essas contas como $X_{0} = X_{p}W{p}$ e $Y_{0} = Y_{p}W{p}$, respectivamente, já que ambas possuem $\frac{Z_{0}}{Z_{p}}$ multiplicando alguma variável. O mesmo processo para calcular $W_{p}$ se aplica no tri-dimensional quando comparado ao bi-dimensional, só que agora em relação ao $Z$ e não o $Y$ ($W_{p} = \frac{Z_{0}}{Z_{p}}$).

Esse é o processo matemático por trás da nossa projeção, onde, na tela, todos pontos $X_{p}$ e $Y_{p}$ são plotados, nos dando os vértices do nosso cubo. Conectando esses vértices, conseguimos nossas arestas, realmente conseguindo representar um cubo em duas dimensões. 

Ainda podemos aplicar vários tipos de rotações a esse cubo, por ele ser representado por uma matriz. As matrizes de rotação tem os seguintes modelos: 

$$
R_x = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & \cos(\theta) & -\sin(\theta) & 0 \\
0 & \sin(\theta) & \cos(\theta) & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$
$$
R_y = \begin{bmatrix}
\cos(\theta) & 0 & \sin(\theta) & 0 \\
0 & 1 & 0 & 0 \\
-\sin(\theta) & 0 & \cos(\theta) & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$
$$
R_z = \begin{bmatrix}
\cos(\theta) & - \sin(\theta) & 0 & 0 \\
\sin(\theta) & \cos(\theta) & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Escolhendo nosso ângulo, realizamos a seguinte conta: 

$$
C_R = R C
$$

A matriz $Cubo_{R}$ é nossa matriz do cubo rotacionado, nos permitindo representar a rotação do cubo em duas dimensões. Vale a pena ressaltar que esse processo de rotação apenas funciona se seu cubo estiver complemente centralizado no ponto (0,0,0), ou seja, na origem de todas as três posições cardeais. 

Para que possamos ver o cubo, ele precisa estar a uma certa distância do nosso pinhole ("câmera"). Portanto, após o processo de rotação, transladamos o cubo a uma distância $n$. O resultado fica assim: 

$$
T = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & n \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

$$
C_T = T C_R
$$

Mais uma vez, para que o cubo esteja centralizado na nossa tela, necessitamos de uma segunda translação. Dessa vez, a matriz $T_tela$ genérica seria:

$$
T_{tela} = \begin{bmatrix}
1 & 0 & 0 & Tamanho_x \\
0 & 1 & 0 & Tamanho_y \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

A conta que nos daria as posições finais do cubo é:

$$
C_d = T_{tela} C_T
$$

