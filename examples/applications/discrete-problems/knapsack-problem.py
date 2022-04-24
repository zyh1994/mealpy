# !/usr/bin/env python
# Created by "Thieu" at 11:03, 29/11/2021 ----------%
#       Email: nguyenthieu2102@gmail.com            %
#       Github: https://github.com/thieu1995        %
# --------------------------------------------------%

# https://developers.google.com/optimization/bin/knapsack

import numpy as np
from mealpy.bio_based import SMA, VCS, BBO, EOA, IWO, SBO, WHO
from mealpy.physics_based import EO
from mealpy.evolutionary_based import MA, FPA, ES, EP, DE, GA, CRO
from mealpy.probabilistic_based import CEM
from mealpy.music_based import HS
from mealpy.system_based import WCA, GCO, AEO
from mealpy.math_based import AOA, HC, SCA
from mealpy.human_based import BRO, CA, FBIO, SARO, SSDO, TLO, GSKA, LCO, ICA, BSO, QSA, CHIO
from mealpy.physics_based import ArchOA, ASO, EFO, HGSO, MVO, WDO, SA, TWO, NRO
from mealpy.swarm_based import ABC, ACOR, AO, BA, WOA, SSA, SLO, SHO, SSO, NMRA, MSA, MRFO, MFO, JA
from mealpy.swarm_based import GOA, CSA, BSA, ALO, BeesA, BES, FFA, FOA, PFA, COA, FA, SFO, SSpiderA, SSpiderO
from mealpy.swarm_based import HHO, GWO, EHO, CSO, DO, SRSR, PSO, BFO, HGS

VALUES = np.array([
    360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147,
    78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28,
    87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276,
    312
])
WEIGHTS = np.array([
    7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0,
    42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71,
    3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13
])
CAPACITY = 850


## 50 dimensions since we have 50 items
## each item has two state: 0 (not put in the bag), 1 (put in the bag)
## so lower bound is 0 and upper bound is 1.99 because
## int(0 -> 0.99) = 0
## int(1 -> 1.99) = 1

LB = [0] * 50
UB = [1.99] * 50

def fitness_function(solution):
    def punish_function(value):
        """
        Using this function to handling constraint optimization problem
        """
        return 0 if value <= CAPACITY else value

    solution_int = solution.astype(int)                 # Convert float to integer here
    current_capacity = np.sum(solution_int * WEIGHTS)
    temp = np.sum(solution_int * VALUES) - punish_function(current_capacity)
    return temp


problem_dict1 = {
    "fit_func": fitness_function,
    "lb": LB,
    "ub": UB,
    "minmax": "max",
}

## Run the algorithm
model1 = MVO.OriginalMVO(problem_dict1, epoch=100, pop_size=50)
best_position, best_fitness = model1.solve()
print(f"Best solution: {best_position}, Best fitness: {best_fitness}")
print(model1.solution[0].astype(int))


