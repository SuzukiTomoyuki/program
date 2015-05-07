import networkx as nx
import matplotlib.pyplot as plt
from random import random,randint
 
N = 1000
K = 5
 
def make_small_world_network(n,k,p):
    assert p >= 0 and p <=1, "p is reconnect probability"
    assert n > 0, "n is num nodes"
    assert k > 0, "2*k is num of link per one node"
 
    G = nx.Graph()
    G.add_nodes_from(xrange(1,n+1))
 
    for i in xrange(1,n+1):
        for j in xrange(1,k+1):
            v = i
            u = i+j 
            if u > n:
                u = u % (n+1) + 1
            G.add_edge(v,u)
 
    for i in xrange(1,n+1):
        for j in xrange(1,k+1):
            if random() < p:
                # reconnect edge
                v = i
                old_u = i+j
                if old_u > n:
                    old_u = old_u % (n+1) + 1
                new_u = randint(1,n)
                while v != new_u and G.has_edge(v,new_u):
                    new_u = randint(1,n)
                G.remove_edge(v,old_u)
                G.add_edge(v,new_u)
    return G
 
 
def main():
    ps = []
    ls = []
    cs = []
    for i in xrange(1,10):
        ps.append(0.0001*i)
    for i in xrange(1,10):
        ps.append(0.001*i)
    for i in xrange(1,10):
        ps.append(0.01*i)
    for i in xrange(1,10):
        ps.append(0.1*i)
    ps.append(1)
 
    G0 = make_small_world_network(N,K,0)
    L0 = nx.average_shortest_path_length(G0)
    C0 = nx.average_clustering(G0)
 
    for p in ps:
        G = make_small_world_network(N,K,p)
        l = nx.average_shortest_path_length(G)
        c = nx.average_clustering(G)
        ls.append(l/L0)
        cs.append(c/C0)
        print("{0} {1} {2}".format(p,l/L0,c/C0))
 
    plt.xlabel("p")
    plt.semilogx(ps,ls,"rs",label="L(p)/L0")
    plt.semilogx(ps,cs,"bo",label="C(p)/C0")
    plt.legend()
    plt.savefig("small.png")
 
if __name__ == "__main__":
    main()