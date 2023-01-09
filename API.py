from plantsim.plantsim import Plantsim
from plantsim.table import Table
import networkx as nx
from DataBase import Lager,Einzelstation,Quelle,Puffer
from api_utils import build_model_edges, build_model_nodes

plantsim = Plantsim(version='', license_type='Student',visible=False)
plantsim.load_model("C:\\Users\\selle\\Desktop\\Masterarbeit\\001_Plant_simulation\\Simulation.spp")
plantsim.set_path_context(".Models.Lager")


Lager_nodes = build_model_nodes(Lager,plantsim)
Lager_edges = build_model_edges(Lager,Lager_nodes)



Lager_graph = nx.Graph()
for node in Lager_nodes:
    for k, v in node.items():
        if k=="name":
            name = v
            Lager_graph.add_node(v)
            break
for edge in Lager_edges:
    if edge :
        Lager_graph.add_edge(edge[0],edge[1])


import matplotlib.pyplot as plt

nx.draw_networkx(Lager_graph,with_labels=True)
#nx.draw_planar(Lager)
plt.show()