'''
This file serves as the file that runs the floyd_warshalls.py program.
'''
import floyd_warshalls as fw
def __main__():
    pass
if __name__ == "__main__":
    fileName = fw.getFileName()
    if fileName == ".txt":
        graph, nodes = fw.getData()
    else:
        graph, nodes = fw.getData(fileName)
    x, y = fw.getXY()
    result, tb = fw.floyd_Warshalls(graph, nodes)
    print()
    fw.displayIntermediate(result)
    path = fw.trackChanges(tb, x, y)
    print("Path -> " + str(path))
