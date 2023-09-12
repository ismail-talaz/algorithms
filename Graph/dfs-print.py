from stack import Stack

def iterativeDfsPrint(graph,src):

    stack=Stack()
    stack.push(src)
    while stack.isEmpty()==False:
        current=stack.pop()
        print(current)
        if current not in graph:continue
        for neighbour in graph[current]:
            stack.push(neighbour) 

def recursiveDfsPrint(graph,src):
    print(src)
    if src not in graph:return
    for neighbour in graph[src]:
        recursiveDfsPrint(graph,neighbour)

graph={
    "a":["b","c"],
    "b":["d","e"],
    "c":["f"],
    "f":["z"],
    "e":["z"]
}

iterativeDfsPrint(graph,"a")
recursiveDfsPrint(graph,"a")
