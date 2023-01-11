from plantsim.plantsim import Plantsim
from plantsim.table import Table
import networkx as nx
from DataBase import Lager,Einzelstation,Quelle,Puffer
from api_utils import build_model_edges, build_model_nodes
from graph_utils import draw_edges,draw_graph,draw_nodes

plantsim = Plantsim(version='', license_type='Student',visible=False)
plantsim.load_model("C:\\Users\\selle\\Desktop\\Masterarbeit\\001_Plant_simulation\\Simulation.spp")
plantsim.set_path_context(".Models.Lager")
plantsim.get_value()

#Lager_nodes = build_model_nodes(Lager,plantsim)
#Lager_edges = build_model_edges(Lager,Lager_nodes)
#plantsim.set_event_controller()
#plantsim.start_simulation()
#plantsim.CloseModel("C:\\Users\\selle\\Desktop\\Masterarbeit\\001_Plant_simulation\\Simulation.spp")

#Lager_graph = nx.DiGraph()
#Lager_graph = draw_nodes(Lager_graph,Lager_nodes)
#Lager_graph = draw_edges(Lager_graph,Lager_edges)
#draw_graph(Lager_graph)

