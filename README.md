# Explorador de Labirintos (Iterativo)
## Integrantes

- [Breno Saraiva](https://github.com/BrenoSaraiva-exe)
- [Jorge Terence](https://github.com/JorgeTerence)
- [Rodrigo Zanetti](https://github.com/RodrigoZanetti175)
- [Vinicius Crozato](https://github.com/ViniciusCrozato)

## Explicação da Ideia

A ideia foi concebida durante a aula de estrutura de dados, onde, após algumas outras ideias, chegamos a conclusão de que o problema pensado poderia ser resolvido e seria bem interessante para o desenvolvimento do grupo.

## O Problema

Criar um algoritmo que seja capaz de receber um arquivo .txt contendo uma espécie de mapa de um labirinto, onde "1" representa paredes do labirinto, "2" a entrada e saída e "0" representa a trilha que é possível ser explorada. Com os parâmetros recebidos, o algoritmo deve ser capaz de encontrar um dos caminhos possíveis que levam da entrada até a saída do labirinto.

## Ideia de solução

Existem diversas soluções possíveis para o problema, porém, a solução que encontramos, parte do paradigma de iteração, portanto, se trata de uma solução que utiliza iterações para resolução.

Deste modo, chegamos a uma solução que utiliza de alguns parâmetros e conceitos interessantes que pensamos durante o entendimento do problema.

## Solução

- Primeiramente o programa lerá o labirinto e o transformará em uma Lista das linhas do labirinto, onde cada elemento da linha é representado por uma tupla de dois inteiros, ou seja, coordenadas **(l,c)**, onde "l" representa linha e "c" representa coluna.

- Após a leitura do labirinto, o algoritmo passa por uma fase de reconhecimento, onde ele extrairá dados importantes do labirinto, sendo eles:
    - **Começo e Fim**: Passando pela função `get_start_end()`, o algoritmo registrará as coordenadas da entrada e saída do labirinto.

    - **Pontos de Intersecção**: Com a execução da função `get_intersections()`, o programa obeterá os pontos de intersecção do labirinto, que são a base da função principal de navegação. Os pontos de intersecção são aqueles pontos que dão acesso a mais de um sentido(horizontal e vertical), dando brecha para mais possibilidades de navegação.

- Com os dados principais obtidos, o algoritmo pode iniciar a função principal do programa, que se trata de `navigate()`, a qual será responsável por iterar pelos pontos de intersecção, começando pelo início, até encontrar a saída. Durante as iterações, caso o algoritmo acabe em um ponto de intersecção sem saída, a função é capaz de voltar ao ponto de intersecção mais próximo, excluindo o caminho formado até o ponto de intersecção sem saída, o qual é retirado da lista de pontos de intersecção navegáveis.


## Funções

### `get_start_end()`

#### Parâmetros

- **Mapa do labirinto**: Uma lista que contém listas de tuplas formadas por 2 inteiros (linhas, colunas).

####  Retorno

Esta função retorna duas tuplas de dois inteiros (linha, coluna). A primeira representa a coordenada do começo do labirinto e a segunda o final do labirinto. 

*É importante notar que a **primeira** coordenada com valor "2" que é encontrada pela função no mapa é definida como começo*

### `get_intersections()`

#### Parâmetros

- **Mapa do labirinto**: Uma lista que contém listas de tuplas formadas por 2 inteiros (linhas, colunas).

#### Retorno

Esta função retorna uma lista de tuplas(int, int), as quais representam as coordenadas dos pontos de intersecção no labirinto

### `navigate()`


#### Parâmetros

- **Mapa do labirinto**: Uma lista que contém listas de tuplas formadas por 2 inteiros (linhas, colunas).
- **Ponto de Início**: Uma tupla, formada por dois números inteiros, que representa as coordenadas do início do labirinto.
- **Ponto de Saída**: Uma tupla, formada por dois números inteiros, que representa as coordenadas do saída do labirinto.
- **Pontos de Intersecção**: Uma lista que contém tuplas formadas por 2 inteiros (linhas, colunas), as quais representam coordenadas de pontos de intersecção.

#### Retorno

Esta função retorna uma lista de tuplas (coordenadas), que representam os pontos pelos quais o caminho do começo até a saída são formados.


## Análise Big O

Através de algumas análises, foi possível notar que a parte de maior complexidade e peso do algoritmo se trata da iteração que é feita durante a função navigate, a qual pode ser reiniciada caso o caminho percorrido até determinado ponto não tenha saída. Portanto, foi notado que o a função para calcular o tempo de execução depende de duas principais variáveis, sendo elas:

- n ⭢ número de pontos de intersecção;
- m  ⭢ número de vezes que há um "reset" na iteração principal, o qual é causado por caminhos sem saída.

Portanto, a notação Big O deste algoritmo pode ser transcrita para: **O(n*m)**

