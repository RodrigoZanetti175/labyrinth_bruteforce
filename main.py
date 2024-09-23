#mapear entrada e saida

#mapear pontos de interssecção 

#se uma das direções for a esquerda, a outra nao pode ser direita, por que não seria uma real interssecção

#partir de um dos pontos de entrada/saida até chegar em uma intersecção próxima
#dessa interssecção~

RESET = "\033[0m"
RED = "\x1b[31m"
YELLOW = "\033[93m"

colors = ["", RED, YELLOW]

def print_map(m):
    for row in m:
        for pos in row:
            print(colors[pos] + str(pos), RESET, end="")
        print("")

if __name__ == "__main__":
    f = open("./labyrinth.txt")
    map =[]
    for line in f.readlines():
        linha =[]
        for c in list(line):
            if c != "\n":
                linha.append(int(c))
        map.append(linha)

    print_map(map)