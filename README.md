# mesa-model-assistant
A collection of classes that assist with agent-based modeling in the mesa library. Currently, the package contains the `ModelExplorerMP` module that assists with batchrunning agent-based models for various parameter combinations across multiple cores. Specifically, this module overcomes errors the mesa library multiprocessing batchrunner throws.

To install mesa-model-assistant run the following code:

<div>
<code>pip install git+https://github.com/nikita-sivakumar/mesa-model-assistant.git#egg=mesaModelAssistant</code>
</div>

## ModelExplorerMP
Since agent-based models (ABMs) are inherently stochastic a given parameter combination must be run for multiple iterations to characterize the associated result. Moreover, ABM parameter space explorations require running the model for a variety of parameter combinations over time and for multiple iterations. These parameter explorations can be very computationally expensive. ModelExplorerMP provides an infrastructure to execute batchruns of ABMs in parallel for a variety of user-defined parameter values.

To use ModelExplorerMP import the module as follows:

<code>
  from mesaModelAssistant import ModelExplorerMP as mp
</code>

Instantiate a ModelExplorerMP object as follows:

<div>
  <code>
    batchrunner  = mp.ModelExplorerMP(model_cls= class in which model is defined,
                                                      num_cores= number of cores over which you want to parallelize the batchrunner,
                                                      variable_parameters = dictionary of variable parameters,
                                                      fixed_parameters = dictionary of fixed parameters,
                                                      iterations = number of times each parameter combination should be run,
                                                      max_steps = number of steps each model should be run to)
  </code>
</div
