import networkx as nx

def main():
    grafo={
        1:[2,3],
        2:[1,4],
        3:[1],
        4:[2]
    }
    G=nx.Graph(grafo)

if __name__=="__main__":
    main()