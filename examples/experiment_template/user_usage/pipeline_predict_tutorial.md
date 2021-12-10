# Pipeline Quickstart
	This documentation will give a brief tutorial of how to use a pipeline to build a 
	hetero secureboost tree model and then predict new instances using learnt model.

## Fitting a Hetero SecureBoost Model

Import needed components for building a hetero secureboost model:
* Reader: for reading raw data
* DataTransform: transform raw data to Instances
* Intersection: component to find intersections of guest and host samples
* HeteroSecureBoost: the tree component
* Data: Class that defines data in dsl flow

Codes below give details of building a model 
```python
    from pipeline.backend.pipeline import PipeLine # Pipeline 
    from pipeline.component import Reader, DataTransform, Intersection, HeteroSecureBoost # fate components
    from pipeline.interface import Data  # data flow
    
    # define dataset name and namespace
    guest_train_data = {"name": "breast_hetero_guest", "namespace": "experiment"}
    host_train_data = {"name": "breast_hetero_host", "namespace": "experiment"}

    # initialize pipeline, set guest as initiator and set guest/host party id
    pipeline = PipeLine().set_initiator(role="guest", party_id=9999).set_roles(guest=9999, host=10000)

    # define components
    # reader read raw data 
    reader_0 = Reader(name="reader_0")
    reader_0.get_party_instance(role="guest", party_id=9999).component_param(table=guest_train_data)
    reader_0.get_party_instance(role="host", party_id=10000).component_param(table=host_train_data)
    # data transform
    data_transform_0 = DataTransform(name="data_transform_0", with_label=True)
    data_transform_0.get_party_instance(role="host", party_id=10000).component_param(with_label=False)
    # find sample intersection using Intersection components
    intersect_0 = Intersection(name="intersection_0")
    # hetero secureboost components, setting algorithm parameters
    hetero_secureboost_0 = HeteroSecureBoost(name="hetero_secureboost_0",
                                             num_trees=5,
                                             bin_num=16,
                                             task_type="classification",
                                             objective_param={"objective": "cross_entropy"},
                                             encrypt_param={"method": "iterativeAffine"},
                                             tree_param={"max_depth": 3})

    # add components to pipeline, in the order of task execution
    pipeline.add_component(reader_0)\
        .add_component(data_transform_0, data=Data(data=reader_0.output.data))\
        .add_component(intersect_0, data=Data(data=data_transform_0.output.data))\
        .add_component(hetero_secureboost_0, data=Data(train_data=intersect_0.output.data))

    # compile & fit pipeline
    pipeline.compile().fit()
    
    # save train pipeline
    pipeline.dump("pipeline_saved.pkl")
```

After training, we save pipeline as 'pipeline_saved.pkl'

## Predict instances

After finish fitting secureboost model, we can run prediction by creating a new pipeline, which reuses
fate components in the training step. We load training pipeline from 'pipeline_saved.pkl'.

```python
    from pipeline.backend.pipeline import PipeLine
    from pipeline.component.reader import Reader
    from pipeline.interface.data import Data
    
    # load train pipeline
    pipeline = PipeLine.load_model_from_file('pipeline_saved.pkl')
    # deploy components in training step
    pipeline.deploy_component([pipeline.data_transform_0, pipeline.intersection_0, pipeline.hetero_secure_boost_0])
    # set new instances to predict
    # new dataset
    guest_train_data = {"name": "new_hetero_guest", "namespace": "experiment"}
    host_train_data = {"name": "new_hetero_host", "namespace": "experiment"}
    # set new reader
    reader_0 = Reader(name="reader_0")
    reader_0.get_party_instance(role="guest", party_id=9999).algorithm_param(table=guest_train_data)
    reader_0.get_party_instance(role="host", party_id=10000).algorithm_param(table=host_train_data)
    # new predict pipeline
    predict_pipeline = PipeLine()
    # update reader
    predict_pipeline.add_component(reader_0)
    # add selected components from train pipeline onto predict pipeline
    predict_pipeline.add_component(pipeline,data=Data(predict_input={pipeline.data_transform_0.input.data: reader_0.output.data}))
    # run predict model
    predict_pipeline.predict()
```


	