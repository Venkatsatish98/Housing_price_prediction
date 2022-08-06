#from tkinter import E
from housing.entity.config_entity import DataIngestionConfig, DataValidationCOnfig, DataTransformationConfig,\
ModelTrainerConfig, ModelPusherConfig, TrainingPipelineconfig
from housing.util.util import read_yaml_file
from housing.logger import logging
import sys, os
from housing.constant import *
from housing.exception import HousingException




class configuration:

    def __init__(self,
        config_file_path = CONFIG_FILE_PATH,
        current_time_stamp = CURRENT_TIME_STAMP
        )-> None:
        self.config_info = read_yaml_file(file_path = config_file_path)
        self.training_pipeline_config = self.get_training_pipeline_config()
        self.time_stamp = current_time_stamp


    def get_data_ingested_config(self) ->DataIngestionConfig:
        pass


    def get_data_validation_config(self) ->DataValidationCOnfig:
        pass


    def get_data_transformation_config(self) ->DataTransformationConfig:
        pass


    def get_model_trainer_config(self)->ModelTrainerConfig:
        pass

    def get_model_pusher_config(self)->ModelPusherConfig:
        pass

    def get_training_pipeline_config(self) ->TrainingPipelineconfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR, 
            training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )

            training_pipeline_config = TrainingPipelineconfig(artifact_dir=artifact_dir)
            logging.info(f"Training_pipeline_config: {training_pipeline_config}")
            return training_pipeline_config

        except Exception as e:
            raise HousingException(e,sys) from e





