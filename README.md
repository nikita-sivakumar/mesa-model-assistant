# mesa-model-assistant
A collection of classes that assist with agent-based modeling in the mesa library. Currently, the package contains the `ModelExplorerMP` module that assists with batchrunning agent-based models for various parameter combinations across multiple cores. Specifically, this module overcomes errors the mesa library multiprocessing batchrunner throws.

To install mesa-model-assistant run the following code:

```
pip install git+https://github.com/nikita-sivakumar/mesa-model-assistant.git#egg=mesaModelAssistant
```

## ModelExplorerMP
Since agent-based models (ABMs) are inherently stochastic a given parameter combination must be run for multiple iterations to characterize the associated result. Moreover, ABM parameter space explorations require running the model for a variety of parameter combinations over time and for multiple iterations. These parameter explorations can be very computationally expensive. ModelExplorerMP provides an infrastructure to execute batchruns of ABMs in parallel for a variety of user-defined parameter values.

To use ModelExplorerMP import the module as follows:

<code>
  from mesaModelAssistant import ModelExplorerMP as mp
</code>

Instantiate a ModelExplorerMP object as follows:

```
batchrunner = mp.ModelExplorerMP(model_cls= class in which model is defined,
                              num_cores= number of cores over which you want to parallelize the batchrunner,
                              variable_parameters = dictionary of variable parameters,
                              fixed_parameters = dictionary of fixed parameters,
                              iterations = number of times each parameter combination should be run,
                              max_steps = number of steps each model should be run to)
```

To run each parameter combination use the `schedule_run_all_param_combinations()` method.
The method will return all data collected by the DataCollector() object defined in model_cls for each parameter combination overtime, in the form of a list of dictionaries, in which the key is the parameter combination and iteration and the value is the returned data frame. You may analyze this data however you please :)

```
param_exploration_results = batchrunner.schedule_run_all_param_combinations()
```

For a tutorial on how to implement an ABM in mesa and use the ModelExplorerMP module to explore the ABM parameter space, visit the [MesaModelExplorerMP-tutorial] (MesaModelExplorerMP-Tutorial.ipynb).
