'''
This program performs the Floyd Warshalls algorithm and rebuilds the shortest
path between any 2 nodes given the user's input for x and y. It should also
read data from a user entered file, if no file name chosen, the program will
default to testData.txt.
'''

global TEST
TEST = "testData.txt"
global INFINITE
INFINITE = 'x'


'''
This function implements the floyd warshalls algorithm. It returns two values
the final graph(An) and the traceback graph containing the intermediate steps.
    Args:
        - graph: graph read from a file.
        - vertices: total number of nodes/vertices in graph
'''
def floyd_Warshalls(graph, vertices):
    A0 = graph
    traceback = []
    for k in range(vertices):
        # Create intermediate graph
        Ak = [ [] for vertex in range(vertices)]
        print()
        for i in range(vertices):
            for j in range(vertices):
                try:
                    a = A0[i][j]
                    b1 = A0[i][k]
                    b2 = A0[k][j]
                    b = b1 + b2
                    val = min(a, b)
                    Ak[i].append(val)
                except TypeError:
                    if A0[i][j] == INFINITE and (A0[i][k] != INFINITE
                                            and A0[k][j] != INFINITE):
                        Ak[i] += [A0[i][k] + A0[k][j]]
                    else:
                        Ak[i] += [A0[i][j]]
        displayIntermediate(A0)
        traceback.append(A0)
        A0 = Ak
    traceback.append(A0)
    return A0, traceback

'''
Displays each graph to the screen.
    Args:
        - graph: graph read from file or intermediate graph
'''
def displayIntermediate(graph):
    for i in range(len(graph)):
        print(graph[i])

def getFileName():
    print("Please enter a file name below. \n(**Note: Do not enter the" +
            " .txt file type, only enter the name)\n", end='')
    fileName = str(input("File name -> ")) + ".txt"
    return fileName

'''
Grabs the data from a given file, or the default file and parses each line.
It then returns the resulting graph and n for the total nodes in the graph.
    Args:
        - fileName: name provided by user or the default
'''
def getData(fileName=TEST):
    f = open(fileName, 'r')
    graph = []
    # 1st line is the dimensions of graph
    n = int(f.readline())
    for line in f:
    val = ""
    newLine = []
    for char in line:
        if char != INFINITE and char != ' ':
            val += char
        elif char == ' ':
            try:
                newLine.append(int(val))
                val = ""
            except ValueError:
                pass
        else:
            newLine.append(char)
    try:
        newLine.append(int(val))
    except ValueError:
        pass
    graph.append(newLine)
    return graph, n

'''
Designed to perform the traceback and determine the shortest path between x
and y.
    Args:
        - traceback: list of intermediate graphs
        - x, y: the two nodes the user would like to find the shortest path
            between them
'''
def trackChanges(traceback, x, y):
    k = y
    path = list()
    while (k - 1) >= x:
        row = col = x - 1
        while row < y:
            while col < y:
                if traceback[k][row][col] != traceback[k-1][row][col]:
                    path = [k] + path
                    row = y
                    break
                col += 1
        row += 1
    k -= 1
    # If the nodes are equal you have to return just one of the nodes
    if x == y:
        return [x]
    return [x] + path + [y]

'''
This function is to be called at start of program so that it can be used to
find the shortest path given nodes x and y that are entered by the user.
'''
def getXY():
    print("Please enter the nodes you want to find below.")
    x = int(input(" x -> "))
    y = int(input(" y -> "))
    return x, y
