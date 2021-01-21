import numpy as np
import pandas as pd
import multiprocessing
from itertools import product

from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

class ModelExplorerMP:
    def __init__(
        self,
        num_cores=None,
        model_cls=None,
        variable_parameters=None,
        fixed_parameters=None,
        iterations=None,
        max_steps=None
    ):
        self.num_cores = num_cores
        self.model_cls = model_cls
        self.variable_parameters = variable_parameters
        self.fixed_parameters = fixed_parameters
        self.iterations = iterations
        self.max_steps = max_steps
        
    def schedule_run_all_param_combinations(self):
        # define all parameter combinations for which the model must be run.
        parameter_combinations = self.generate_run_matrix()
#         print(parameter_combinations)
        
        # determine how many times parallelization of cores must be repeated to complete runs
        total_runs = len(parameter_combinations)
        num_cycles = 1
        if (total_runs % self.num_cores) > 0:
            num_cycles = int(total_runs / self.num_cores) + 1
        else:
            num_cycles = int(total_runs / self.num_cores)
        
        index_1 = 0
        index_2 = self.num_cores
        outputs_all = []
        for i in range(num_cycles):
            if __name__ == '__main__':
                print("i to the main function.")
                pool = multiprocessing.Pool()
                pool = multiprocessing.Pool(processes=self.num_cores)
                inputs = parameter_combinations[index_1:index_2]
                
                outputs = pool.map(self.instantiate_and_run_model,inputs)
                outputs_all.append(outputs)
                index_1 = index_2
                index_2 = index_2 + self.num_cores
        return outputs_all
                
    def generate_run_matrix(self):
        params = list(self.variable_parameters.values())
        run_matrix = list(product(*params))
        run_matrix = [list(i) for i in run_matrix]
        full_run_matrix = [[i,k] for i in run_matrix for k in range(self.iterations)]
        return full_run_matrix
    
    def instantiate_and_run_model(self,param_combination_i):
        variables = list((self.variable_parameters).keys())
        print('Run {} = {}; Iteration {} started.'.format(variables, param_combination_i[0],param_combination_i[1])) 
        
        args = (self.fixed_parameters).copy()
        c=0
        for i in variables:
            args[i] = param_combination_i[0][c]
            c=c+1

        # instantiate the model
        model = self.model_cls(**args)
        
        # run the model
        for s in range(self.max_steps):
            model.step()
            
        # collect and return data from model run
        print('Run {}; Iteration {} finished.'.format(param_combination_i[0],param_combination_i[1]))
        df = model.datacollector.get_model_vars_dataframe()
        output_name = '{}_{}_run_{}'.format(variables, param_combination_i[0],param_combination_i[1])
        return {output_name: df}