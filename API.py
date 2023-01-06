from plantsim.plantsim import Plantsim
from plantsim.table import Table

plantsim = Plantsim(version='', license_type='Student')
plantsim.load_model("C:\\Users\\selle\\Desktop\\Masterarbeit\\001_Plant_simulation\\Simulation.spp")

plantsim.set_path_context(".Models.Lager")
test = plantsim.get_object(".PackstationRitzelwellen")
#table = Table(plantsim, 'PackstationRitzelwellen')
print(test) 