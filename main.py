#mapear entrada e saida

#mapear pontos de interssecção 

#se uma das direções for a esquerda, a outra nao pode ser direita, por que não seria uma real interssecção

#partir de um dos pontos de entrada/saida até chegar em uma intersecção próxima
#dessa interssecção

#achar próximo ponto de intersecção

from typing import List, Tuple


RESET = "\033[0m"
RED = "\x1b[31m"
YELLOW = "\033[93m"

colors = ["", RED, YELLOW]



def print_map(m: List[List[int]]) -> None:
    for row in m:
        for pos in row:
            print(colors[pos] + str(pos), RESET, end="")
        print("")

def get_start_end(m: List[List[int]]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    check = False
    for i in range(len(m)):
        for j in range(len(m[i])):
            if check:
                if m[i][j] == 2:
                    end = (i, j)
                    return start, end
            else:
                if m[i][j] == 2:
                    start = (i, j)
                    check = True
                    
                    
def get_interssections(m: List[List[int]]) -> List[Tuple[int, int]]:
    interssections = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            vertical = False
            horizontal = False
            if m[i][j] == 0:
                horizontal = not m[i-1][j] or not m[i+1][j]
                vertical = not m[i][j+1] or not m[i][j-1]
            if vertical and horizontal:
                interssections.append((i,j))                
    return interssections

def navigate(
    m: List[List[int]],
    start: Tuple[int,int],
    end: Tuple[int,int],
    interssections: List[Tuple[int,int]]
    ) -> List[Tuple[int,int]]:
    current = start
    track: List[Tuple[int,int]]
    track.append(current)
    for i in interssections:
        if(i[0] == current[0]):
            if i[1] > current[1]:
                for j in range(i[1]-current[1]):
                    track.append((i[0],j+current[1]))
                    # Salvar a ultima interssecção e se der errado ler track em ordem reversa para encontrar de onde
                    # é preciso continuar a procurar e excluir todo o caminho feito a partir daquele ponto.
                    
        #Condição de Fim
        if current == end:
            return track

   # (p[0], p[1] - 1) -> cima
   # (p[0], p[1] + 1) -> baixo
   # (p[0] - 1, p[1]) -> esquerda
   # (p[0] + 1, p[1]) -> direita

if __name__ == "__main__":
    f = open("./labyrinth.txt")
    map = []
    for line in f.readlines():
        linha = []
        for c in list(line):
            if c != "\n":
                linha.append(int(c))
        map.append(linha)

    
    print_map(map)
    start,end = get_start_end(map)
    interssections = get_interssections(map)
    print(get_start_end(map))
    print(get_interssections(map))
    print(navigate(map, start, end, interssections))
    