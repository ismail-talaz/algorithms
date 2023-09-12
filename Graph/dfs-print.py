from stack import Stack

def iterativeDfsPrint(graph,src):
    visited=set()
    stack=Stack()
    stack.push(src)
    while stack.isEmpty()==False:
        current=stack.pop()
        if current in visited:continue
        else:visited.add(current)
        print(current)
        if current not in graph:continue
        for neighbour in graph[current]:
            stack.push(neighbour) 

def recursiveDfsPrint(graph,src,visited=set()):

    if src in visited:return
    print(src)
    visited.add(src)

    if src not in graph:return
    for neighbour in graph[src]:
        recursiveDfsPrint(graph,neighbour,visited)

graph={
    "a":["b","c"],
    "b":["d","e"],
    "c":["f"],
    "f":["z"],
    "e":["a"]
}

iterativeDfsPrint(graph,"a")
recursiveDfsPrint(graph,"a")
