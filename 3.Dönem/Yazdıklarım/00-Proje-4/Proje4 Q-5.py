from graphviz import Digraph
import networkx as nx

'''Graphviz baslangici'''
# Node silme islemi problem cikardigindan, gorsellestirmede 2 ayri graph kullanildi.
#graphviz version 0.16  networkx version 2.5

G11 = Digraph(format='jpeg')
G11.attr(rankdir='LR', size='8,5')
G11.attr('node', shape='circle', style='filled', fillcolor="antiquewhite:aquamarine")

G22 = Digraph(format='jpeg')
G22.attr(rankdir='LR', size='8,5')
G22.attr('node', shape='circle', style='filled', fillcolor="antiquewhite:aquamarine")

G11.node(name='0', label='0')
G11.node(name='1', label='1')
G11.node(name='2', label='2')
G11.node(name='3', label='3')
G11.node(name='4', label='4')

G22.node(name='0', label='0')
G22.node(name='1', label='1')
G22.node(name='2', label='2')
G22.node(name='4', label='4')

G11.edge('0', '4', '2')
G11.edge('0', '2', '3')
G11.edge('0', '1', '5')
G11.edge('1', '3', '6')
G11.edge('1', '2', '2')
G11.edge('2', '3', '2')
G11.edge('2', '1', '1')
G11.edge('4', '1', '6')
G11.edge('4', '2', '10')
G11.edge('4', '3', '4')

G22.edge('0', '4', '2')
G22.edge('0', '2', '3')
G22.edge('0', '1', '5')
G22.edge('1', '2', '2')
G22.edge('2', '1', '1')
G22.edge('4', '1', '6')
G22.edge('4', '2', '10')

G11.render('s1', view=True)
G22.render('s2', view=True)
'''Graphviz sonu'''

'''networkx başlangıcı'''
G1 = nx.DiGraph()
# nodlar ekleniyor...
G1.add_node(0)
G1.add_node(1)
G1.add_node(2)
G1.add_node(3)
G1.add_node(4)
G1.nodes()

G1.add_edge(0, 4, weight=2)
G1.add_edge(0, 2, weight=3)
G1.add_edge(0, 1, weight=5)
G1.add_edge(4, 1, weight=6)
G1.add_edge(4, 3, weight=4)
G1.add_edge(4, 2, weight=10)
G1.add_edge(1, 2, weight=2, )
G1.add_edge(2, 1)
G1.adj[2][1]['weight'] = 1
G1.add_edge(1, 3, weight=6)
G1.add_edge(2, 3, weight=2)
G1.edges()
# 4. noddan tüm nodlara en ksıa yollar hesaplanıyor...
for x in range(0, 4):
    if x > 0:
        sp = nx.dijkstra_path(G1, source=4, target=x)
        print("4 numaralı düğümden ", x, " numaralı düğüme en kısa yol:")
        sayac = 0
        for i in sp:
            if sayac < len(sp) - 1:
                print(i, end="==> ")
            else:
                print(i, end=" ")
        print(end="son")
        print(" ")


    else:
        print(x, "hedefine doğrudan bir yol bulunamadı...")
print("----------------------- 3. node kaldırılıyor... ---------------------")
G1.remove_node(3)
for x in range(0, 3):
    if x > 0:
        sp = nx.dijkstra_path(G1, source=4, target=x)
        print("4 numaralı düğümden ", x, " numaralı düğüme en kısa yol:")
        sayac = 0
        for i in sp:
            # sayac<len(sp) if print(i,end="=> ")  else  print(i,end=" ")
            if sayac < len(sp) - 1:
                print(i, end="==> ")
            else:
                print(i, end=" ")
        print(end="son")
        print(" ")

    else:
        print(x, "hedefine doğrudan bir yol bulunamadı...")
'''Graphviz sonu'''
