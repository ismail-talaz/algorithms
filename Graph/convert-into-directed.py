def convert(undirected_graph):
    directed_graph={}
    for edge in undirected_graph:
        x,y=edge
        if x not in directed_graph:
            directed_graph[x]=[]
        if y not in directed_graph:
            directed_graph[y]=[]
        directed_graph[x].append(y)
        directed_graph[y].append(x)
    return directed_graph

undirected_graph=[
    ["a","c"],
    ["c","f"],
    ["f","z"],
    ["a","b"],
    ["b","d"],
    ["b","e"],
    ["e","z"]
]

print(convert(undirected_graph))
