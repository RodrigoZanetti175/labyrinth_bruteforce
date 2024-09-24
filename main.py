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
def print_t_map(m: List[List[int]], t: List[Tuple[int,int]]) -> None:
    for row in m:
        for pos in row:
            print(colors[pos] + str(pos), RESET, end="")
        print("")

def navigate(
    m: List[List[int]],
    start: Tuple[int,int],
    end: Tuple[int,int],
    interssections: List[Tuple[int,int]]
    ) -> List[Tuple[int,int]]:
    current = start
    track: List[Tuple[int,int]]
    track = []
    previous: List[Tuple[int,int]]
    previous = []
    i = 0
    while i <= len(interssections):
        track.append(current)
        check = False 
        if current[0] == end[0] or current[1] == end[1]:
            if current[0] == end[0] and end[1] > current[1]:
                for j in range(end[1] - current[1]):
                    track.append((end[0], current[1]+(j+1)))
            if current[0] == end[0] and current[1] > end[1]:
                for j in range(current[1]-end[1]-1):
                    track.append((end[0], end[1]+(j+1)))
            if current[1] == end[1] and current[0] > end[0]:
                for j in range(end[1] - current[1]-1):
                    track.append((current[0]+(j+1), end[1]))
            if current[1] == end[1] and end[0] > current[0]:
                for j in range(current[0]-end[0]-1):
                    track.append((end[0]+(j+1),end[1]))   
            print('c')
            return track
        if(interssections[i][0] == current[0] and interssections[i] not in previous):
            print('a ' + str(current))
            check = True
            previous.append(current)
            if interssections[i][1] > current[1]:
                for j in range(interssections[i][1] - current[1]):
                    if(m[interssections[i][0]][current[1]+(j+1)]):
                        check = False 
                    track.append((interssections[i][0],current[1]+(j+1)))
            if current[1] > interssections[i][1]:
                for j in range(current[1] - interssections[i][1] - 1):
                    if(m[interssections[i][0]][interssections[i][1]+(j+1)]):
                        check = False
                    track.append((interssections[i][0], interssections[i][1]+(j+1)))
                    # Salvar a ultima interssecção e se der errado ler track em ordem reversa para encontrar de onde
                    # é preciso continuar a procurar e excluir todo o caminho feito a partir daquele ponto.
        if(interssections[i][1] == current[1] and interssections[i] not in previous):
            print('b ' + str(current))
            previous.append(current)
            check = True
            if interssections[i][0] > current[0]:
                for j in range(interssections[i][0]-current[0]-1):
                    if(m[current[0]+(j+1)][interssections[i][1]]):
                        check = False
                    track.append((current[0]+(j+1),interssections[i][1]))
            if current[0] > interssections[i][0]:
                for j in range(current[0]-interssections[i][0]-1):
                    if(m[interssections[i][0]+(j+1)][interssections[i][1]]):
                        check = False
                    track.append((interssections[i][0]+(j+1),interssections[i][1]))                    
        elif not check:
            #É necessário arrumar alguma maneira de ele reitarar pelos valores de interssections
            #para que ele consiga voltar a valores de "decisão"

            #Arrumar maneira de iterar desde  o começo todas as vezes 
            print('d ' + str(current))
            print(previous)
            target_index = track.index((previous[-1]))
            print(track)
            track = track[:target_index+1]
            print(track)
            interssections.remove(current)
            print(previous)
            print(interssections)
            previous.pop()
            print(i)
            current = track[target_index]
            i = 0
            continue

        current = interssections[i]
        i += 1
        
        

   # (p[0], p[1] - 1) -> cima
   # (p[0], p[1] + 1) -> baixo
   # (p[0] - 1, p[1]) -> esquerda
   # (p[0] + 1, p[1]) -> direita
   
   #a -> mesma linha
   #b -> mesma coluna
   #c -> final
   #d -> voltar

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
    