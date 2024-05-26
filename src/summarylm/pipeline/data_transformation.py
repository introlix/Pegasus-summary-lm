import sys
from summarylm.config.configuration import ConfigurationManager
from summarylm.components.data_transformation import DataTransformation
from summarylm.logging import logger
from summarylm.exception import CustomException


class DataTransformationPipeline:
    """
    Pipeline for data transformation to convert data into right format
    """
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.convert()
        except Exception as e:
            raise CustomException(e, sys) from e