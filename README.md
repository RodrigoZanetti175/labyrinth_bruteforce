# Explorador de Labirintos (Iterativo)
### Dupla: Rodrigo Zanetti e Vinícius Crozato

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

- Com os dados principais obtidos, o algoritmo pode iniciar a função principal do programa, que se trata de `navigate()`, a qual recebe .... parâmetros



## Funções

### `get_start_end()`

#### Parâmetros

- **Mapa do labirinto**: Uma lista que contém listas de tuplas formadas por 2 inteiros (linhas, colunas).

####  Retorno

Esta função retorna duas tuplas de dois inteiros (linha, coluna). A primeira representa a coordenada do começo do labirinto e a segunda o final do labirinto. 

*É importante notar que a **primeira** coordenada com valor "2" que é encontrada pela função no mapa é definida como começo*
