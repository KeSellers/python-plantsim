import time
from plantsim.plantsim import Plantsim


class PlantSimulationAPI(Plantsim):
    def __init__(self, version='', visible=True, trust_models=False, license_type='Student'):
        super().__init__(version, visible, trust_models, license_type)
        self.head = None




    def run_simulation(self,n_samples = 1000):
        
        for i in range(n_samples):
            self.execute_simtalk("StartSim")
            while self.is_simulation_running():
                time.sleep(0.01)