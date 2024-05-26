import sys
from summarylm.config.configuration import ConfigurationManager
from summarylm.components.model_trainer import ModelTrainer
from summarylm.logging import logger
from summarylm.exception import CustomException


class ModelTrainerPipeline:
    """
    Pipeline for training pegasus model
    """
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            raise CustomException(e, sys) from e