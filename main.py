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
                    
                    
def get_intersections(m: List[List[int]]) -> List[Tuple[int, int]]:
    intersections = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            vertical = False
            horizontal = False
            if m[i][j] == 0:
                horizontal = m[i-1][j] != 1 or m[i+1][j] != 1
                vertical = m[i][j+1] != 1 or m[i][j-1] != 1
            if vertical and horizontal:
                intersections.append((i,j))                
    return intersections
def print_t_map(m: List[List[int]], t: List[Tuple[int,int]]) -> None:
     for i, row in enumerate(m):
        for j, pos in enumerate(row):
            if pos == 2:
                print(YELLOW + "#", RESET, end="")
            elif (i, j) in t:
                print(YELLOW + "@", RESET, end="")
            else:
                print(colors[pos] + str(pos), RESET, end="")
        print("")
def check_collision(
        m: List[List[int]],
        root: Tuple[int,int],
        target: Tuple[int,int]
)-> bool:
    root_row = root[0]
    root_column = root[1]
    target_row = target[0]
    target_column = target[1]

    if(root_row == target_row):
        # - iterate through the columns to see if there is any collision
        lowest_column, highest_column = (root_column, target_column) if root_column < target_column else (target_column, root_column)

        for i in range(highest_column - lowest_column + 1):
            if(m[root_row][i + lowest_column] == 1):
                print("colisao em colunas de mesma linha")
                return True 
    if(root_column == target_column):
        # - iterate through the rows to see if there is any collision
        lowest_row, highest_row = (root_row, target_row) if root_row < target_row else (target_row, root_row)
        for i in range(highest_row - lowest_row + 1):
            if(m[i + lowest_row][root_column] == 1):
                print("colisao em linhas de mesma coluna")
                return True
    # - given two coordinates, this function should check if there is a wall on the way through these
    # - points (probably a simmilar logic to the get_intersection function)
    return False

def treatment(track : List[Tuple[int,int]]) -> List[Tuple[int,int]]:
    for point in track:

    return False
    # - para os casos em que o caminho percorre uma mesma linha e volta, ele deve apenas manter o ponto de entrada daquela linha ()
    # - manter somente o primeiro e o último ponto de uma linha, já que representam, respectivamente, o ponto de entrada e saída da linha
def navigate2(
    m: List[List[int]],
    start: Tuple[int,int],
    end: Tuple[int,int],
    intersections: List[Tuple[int,int]]
    ) -> List[Tuple[int,int]]:
    done = False 
    current = start
    path = List[Tuple[int,int]]
    path = []
    options: List[Tuple[int,int]]
    previous: List[Tuple[int,int]]
    previous = []
    while not done:
        options = []
        if current[0] == end[0] or current[1] == end[1]:
            ######
            path.append(current)
            path.append(end)
            return path #after this, we should have a function to build the path given the intersection points which make part of it
            done = True #Fim da navegação
        for i in intersections: # - this loop stands for finding if there are options
            if current == i or i in previous:
                continue
            if current[0] == i[0] or current[1] == i[1]:
                print(current)
                print(i)
                if(not check_collision(m, current, i)):
                    options.append(i)
        if not options:
            print("d")
            print(str(path))
            path.pop()
            intersections.remove(current)
            current = previous[-1]
            
        for opt in options: # - this loop iterates through the available options
            if current[0] == opt[0]:
                # ! need to find a way to check if there is a wall on the way between the current point and the targeted intersection
                # ! develop check_collision function
                # ! maybe i can check if there is a collision on the options search loop (located previously)
                print("a")
                previous.append(current)
                path.append(current)
                current = opt
                # - if an option is found, it will go to next iteration (of 'while') to see if the path including that option can be (re)solved
                # - if it can't , the algorithm should exclude that option from the intersections list and see if there are more available options from the previous intersection point.
                # - the whole path will only be built after finding the correct intersection points path 
                found = True
                break
            if current[1] == opt[1]:
                print("b")
                previous.append(current)
                path.append(current)
                current = opt

                found = True
                break
        if found:
            continue
                

def navigate(
    m: List[List[int]],
    start: Tuple[int,int],
    end: Tuple[int,int],
    intersections: List[Tuple[int,int]]
    ) -> List[Tuple[int,int]]:
    current = start
    track: List[Tuple[int,int]]
    track = []
    previous: List[Tuple[int,int]]
    previous = []
    counter = 0
    timeout = 0
    append = True
    i = 0
    while i <= len(intersections):
        print(current)
        if append:
            track.append(current)
        check = False 
        for inter in intersections:
            if current[0] == inter[0] or current[1] == inter[1]:
                counter += 1
        if current[0] == end[0] or current[1] == end[1]:
            print("c " + str(current))
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
            return track
        if(intersections[i][0] == current[0] and intersections[i] not in previous):
            print("a " + str(current))
            check = True
            previous.append(current)
            if intersections[i][1] > current[1]:
                for j in range(intersections[i][1] - current[1]):
                    if(m[intersections[i][0]][current[1]+(j+1)]):
                        check = False 
                    track.append((intersections[i][0],current[1]+(j+1)))
            if current[1] > intersections[i][1]:
                for j in range(current[1] - intersections[i][1] - 1):
                    if(m[intersections[i][0]][intersections[i][1]+(j+1)]):
                        check = False
                    track.append((intersections[i][0], intersections[i][1]+(j+1)))
            append = True
            timeout = 0
            counter = 0  
        if(intersections[i][1] == current[1] and intersections[i] not in previous):
            print("b " + str(current))
            previous.append(current)
            check = True
            if intersections[i][0] > current[0]:
                for j in range(intersections[i][0]-current[0]-1):
                    if(m[current[0]+(j+1)][intersections[i][1]]):
                        check = False
                    track.append((current[0]+(j+1),intersections[i][1]))
            if current[0] > intersections[i][0]:
                for j in range(current[0]-intersections[i][0]-1):
                    if(m[intersections[i][0]+(j+1)][intersections[i][1]]):
                        check = False
                    track.append((intersections[i][0]+(j+1),intersections[i][1]))
            append = True  
            timeout = 0
            counter = 0                  
        elif not check:
            if timeout < counter:
                i+=1
                timeout += 1
                append = False
                continue
            print("d " + str(current))
            print(intersections[i])
            target_index = track.index((previous[-1]))
            track = track[:target_index+1]
            intersections.remove(current)
            print(intersections)
            previous.pop()
            current = track[target_index]
            i = 0
            timeout = 0
            counter = 0  
            continue

        current = intersections[i]
        i += 1

if __name__ == "__main__":
    f = open("Labyrinths/01.txt")
    map = []
    for line in f.readlines():
        linha = []
        for c in list(line):
            if c != "\n":
                linha.append(int(c))
        map.append(linha)

    
    print_map(map)
    start,end = get_start_end(map)
    intersections = get_intersections(map)
    print(get_start_end(map))
    print(get_intersections(map))
    track = navigate2(map, start, end, intersections)
    print(str(track))
    print_t_map(map, track)
