import networkx as nx
import matplotlib.pyplot as plt
from pandas import DataFrame

G = nx.DiGraph()

G.add_nodes_from(["Account balance", "Account Statement", "Account",
                  "Account Statement form", "Account Statement workflow",
            "Bill pay", "Check", "Check request",
                  "Canceled check", "Canceled check workflow",
                  "Canceled check form"])

G.add_edge("Account", "Account balance", weight=5)

G.add_edge("Account", "Account Statement workflow", weight=7)
G.add_edge("Account Statement", "Account Statement form", weight=1)
G.add_edge("Account Statement", "Account Statement workflow", weight=1)

G.add_edge("Check", "Check request", weight=1)
G.add_edge("Check", "Canceled check", weight=1)
G.add_edge("Canceled check", "Canceled check workflow", weight=1)
G.add_edge("Canceled check", "Canceled check form", weight=1)

pos = nx.random_layout(G, center=None, dim=2, random_state=10)
nx.draw(G, pos, with_labels = True)
#nx.draw_networkx_labels(G, pos, labels = G.nodes)
edge_labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, labels = edge_labels)
#plt.show()


descendants = nx.descendants(G, "Account")
page_rank_results = nx.pagerank(G, alpha= 0.9, weight='weight')
df = DataFrame.from_dict(page_rank_results, orient='index')
temp = list(descendants)
print(df.loc[temp].sort_values(by=[0], ascending=False))


#print(nx.descendants(G, "Check"))
#print(nx.pagerank(G, alpha=0.9, weight='weight'))

#def search():


#print(nx.descendants(G, "Account"))
'''
update edge
if G.has_edge("Account", "Account balance"):
    G["Account"]["Account balance"]['weight'] +=1
    #print(G["Account"]["Account balance"]['weight'])

print(nx.pagerank(G, alpha=0.9, weight='weight'))
'''