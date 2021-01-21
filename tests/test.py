from mesa-model-assistant import ModelExplorerMP

def test_ModelExplorerMP(num_cores,
                            model_cls,
                            variable_parameters,
                            fixed_parameters,
                            iterations,
                            max_steps):
    '''
    test that you can instantiate a mesa-model-explorer object
    '''

    model_explorer = ModelExplorerMP(num_cores = num_cores,
                            model_cls=model_cls,
                            variable_parameters=variable_parameters,
                            fixed_parameters=fixed_parameters,
                            iterations=iterations,
                            max_steps=max_steps)
    return model_explorer
