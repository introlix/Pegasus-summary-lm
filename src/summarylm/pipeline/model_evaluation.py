import sys
from summarylm.config.configuration import ConfigurationManager
from summarylm.components.model_evaluation import ModelEvaluation
from summarylm.logging import logger
from summarylm.exception import CustomException


class ModelEvaluationPipeline:
    """
    Pipeline for pegasus model evaluation
    """
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.evaluation()
        except Exception as e:
            raise CustomException(e, sys) from e