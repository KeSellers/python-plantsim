from Simulation_API import PlantSimulationAPI
from plantsim.table import Table
from plantsim.pandas_table import PandasTable



#from api_utils import build_model_edges, build_model_nodes
#from graph_utils import draw_edges,draw_graph,draw_nodes

#plantsim = Plantsim(version='', license_type='Student',visible=True,trust_models=True)
#plantsim.load_model("C:\\Users\\selle\\Desktop\\Masterarbeit\\001_Plant_simulation\\Simulation.spp")
#plantsim.set_path_context(".Models.Fliess")
#plantsim.execute_simtalk("&Method.execute()")

model = PlantSimulationAPI(version='', license_type='Student',visible=False,trust_models=True)

model.load_model("C:\\Users\\selle\\Desktop\\Masterarbeit\\001_Plant_simulation\\Simulation.spp")

model.set_path_context(".Models.Fliessprinzip")

#model.run_simulation(1)
headers =["Durchlaufzeit","Losgroesse1","Losgroesse2","Losgroesse3","AbstandQuelle","ZeitMaschine1","ZeitMaschine2"]
#test = Table(model,"Ergebnisse",headers)
#test = PandasTable(model,"Ergebnisse")#(zugriff auf comuputer verbieten ausstellen)print(test)
#print(test.table)

    













#change_attr(plantsim,"Fraesmaschine1","Bearbeitungszeit", 10)
#change_attr(plantsim,"Fraesmaschine","Bearbeitungszeit", 10)
#change_attr(plantsim,"Fraesmaschine","Bearbeitungszeit", 10)
#change_attr(plantsim,"Fraesmaschine","Bearbeitungszeit", 10)






#Lager_nodes = build_model_nodes(Lager,plantsim)
#Lager_edges = build_model_edges(Lager,Lager_nodes)
#plantsim.set_event_controller()
#plantsim.start_simulation()
#plantsim.CloseModel("C:\\Users\\selle\\Desktop\\Masterarbeit\\001_Plant_simulation\\Simulation.spp")

#Lager_graph = nx.DiGraph()
#Lager_graph = draw_nodes(Lager_graph,Lager_nodes)
#Lager_graph = draw_edges(Lager_graph,Lager_edges)
#draw_graph(Lager_graph)

#def change_attr (sim,name,attr,val):
#    node = sim.set_value(name + "."+attr,val) 
#def set_losgroesse(sim,val1,val2,val3):
#    sim.execute_simtalk("&Method.execute(f'{val1}')")

#change_attr(plantsim,"Fraesmaschine","Bearbeitungszeit", 10)
#change_attr(plantsim,"QuelleLager","Abstand", 10)
#print(plantsim.is_simulation_running())
#set_losgroesse(plantsim,2,17,14)
#print(plantsim.execute_simtalk("variiereLosgroessen()",[10,14,17]))
#print(plantsim.get_value("Ergebnisse"))