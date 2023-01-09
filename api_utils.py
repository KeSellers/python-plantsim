from DataBase import Lager,Einzelstation,Quelle,Puffer
def get_data(obj,name,node,sim):
    for attr in obj["attr"]:

           node[attr] = sim.get_value(obj[name]["name"] + "."+attr) 
def build_model_nodes(model,sim): 
    model_nodes=[]          
    for t,name in model["children"]:
        node = {"name":name}
        node["type"] = t
        if t == "Einzelstation":
            get_data(Einzelstation,name,node,sim) 
        elif t=="Quelle":
            get_data(Quelle,name,node,sim)
        elif t=="Puffer":
            get_data(Puffer,name,node,sim)
        model_nodes.append(node.copy()) 
        node.clear()

    return model_nodes
def get_relation(obj,name):
    edges = []
    for edge in obj[name]["relations"]:
        edges.append(edge)
    edge = obj[name]["relations"]
    return edges
def build_model_edges(model,nodes):
    model_edges=[]          
    for t,name in model["children"]:
        if t == "Einzelstation":
            model_edges.extend(get_relation(Einzelstation,name))
        elif t=="Quelle":
            model_edges.extend(get_relation(Quelle,name))
        elif t=="Puffer":
            model_edges.extend(get_relation(Puffer,name))
    
    return model_edges