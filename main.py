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
                horizontal = not m[i-1][j] or not m[i+1][j]
                vertical = not m[i][j+1] or not m[i][j-1]
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
    i = 0
    while i <= len(intersections):
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
            return track
        if(intersections[i][0] == current[0] and intersections[i] not in previous):
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
        if(intersections[i][1] == current[1] and intersections[i] not in previous):
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
        elif not check:
            target_index = track.index((previous[-1]))
            track = track[:target_index+1]
            intersections.remove(current)
            previous.pop()
            current = track[target_index]
            i = 0
            continue

        current = intersections[i]
        i += 1

if __name__ == "__main__":
    f = open("Labyrinths/labyrinth.txt")
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
    track = navigate(map, start, end, intersections)
    print_t_map(map, track)
