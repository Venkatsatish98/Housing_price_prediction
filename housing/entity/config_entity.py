from collections import namedtuple


DataIngestionConfig =  namedtuple('DataIngestionConfig',
['dataset_download_url','tgz_download_dir','raw_data_dir', 'ingested_train_dir', 'ingested_test_dir'])


DataValidationCOnfig = namedtuple('DataValidationConfig', ['schema_file_path'])

DataTransformationConfig = namedtuple('DataTransformationConfig', ["add_bedroom_per_room",
                                                                    "transform_train_dir",
                                                                    "transform_test_dir",
                                                                    "preprocessed_object_file_path"])

ModelTrainerConfig = namedtuple('ModelTrainerConfig', ["trained_model_file_path", "base_accuracy"])

ModelEvaluationConfig = namedtuple('ModelEvaluationConfig', ["model_evaluation_file_path", "time_stamp"])

ModelPusherConfig = namedtuple('ModelPusherConfig', ["export_dir_path"])

