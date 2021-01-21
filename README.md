# mesa-model-assistant
A collection of classes that assist with agent-based modeling in the mesa library. Currently, the package contains the `ModelExplorerMP` module that assists with batchrunning agent-based models implemented in mesa across multiple cores. Specifically, this module overcomes user errors the mesa library multiprocessing batchrunner experiences.

To install mesa-model-assistant run the following code:

<code> pip install git+https://github.com/nikita-sivakumar/mesa-model-assistant.git#egg=mesaModelAssistant<\code>

## ModelExplorerMP
Since agent-based models (ABMs) are inherently stochastic a given parameter combination must be run for multiple iterations to characterize the associated result. Moreover, ABM parameter space explorations require running the model for a variety of parameter combinations over time and for multiple iterations. These parameter explorations can be very computationally expensive. ModelExplorerMP provides an infrastructure to execute batchruns of ABMs in parallel for a variety of user-defined parameter values.

