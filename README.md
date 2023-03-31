# Cubo-$\Sigma$

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

A variável $Z_{p}$ nessa instância seria equivalente a distância do pinhole. Ambas as outras variáveis de entrada ($X_{0}$ e $Y_{0}$) agora seguem o padrão do $X_{0}$ do exemplo bi-dimensional. Isso ocorre pois estamos tecnicamente realizando duas semelhancas diferentes. A primeira é no plano $X$ e $Z$, portanto, o $X_{0}$ é igual a $\frac{X_{p} Z_{0}}{Z_{p}}$. A primeira é no plano $Y$ e $Z$, portanto, o $Y_{0}$ é igual a $\frac{Y_{p} Z_{0}}{Z_{p}}$. Podemos reescrever essas contas como $X_{0} = X_{p}W{p}$ e $Y_{0} = Y_{p}W{p}$, respectivamente, já que ambas possuem $\frac{Z_{0}}{Z_{p}}$ multiplicando alguma variável. O mesmo processo para calcular $W_{p}$ se aplica no tri-dimensional quando comparado ao bi-dimensional, só qeu agora em relação ao $Z$ e não o $Y$ ($W_{p} = \frac{Z_{0}}{Z_{p}}$).