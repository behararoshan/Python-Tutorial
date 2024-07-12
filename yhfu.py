def add_vertex(v):
    add_vertex.append(v)
    row =[]
    for i in range(len(add_vertex)-1):
        row.append(0)
    print_graph.append(row)

    for i in graph:
        i.append(0)

def print_graph():
     for i in range(len(add_vertex)):
          for j in range(len(add_vertex)): 
                print (graph[i][j], end =" " )
             
            print()
