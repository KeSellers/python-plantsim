import numpy as np

def generate_samples(n_samples):

    losgroesse_1 = []
    losgroesse_2 = []
    losgroesse_3 = []
    bearbzeit_1 = []
    bearbzeit_2 = []
    abstandzeit_1 = []
    for i in range(n_samples):

        losgroesse_1.append(np.random.randint(0,20))
        losgroesse_2.append(np.random.randint(0,20))
        losgroesse_3.append(np.random.randint(0,20))
        bearbzeit_1.append(np.random.randint(30,420))
        bearbzeit_2.append(np.random.randint(30,420))
        abstandzeit_1.append(np.random.randint(30,420))

    print(losgroesse_1)
