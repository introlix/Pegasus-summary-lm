import sys
from summarylm.config.configuration import ConfigurationManager
from summarylm.components.data_validation import DataValidation
from summarylm.logging import logger
from summarylm.exception import CustomException


class DataValidationPipeline:
    """
    Pipeline for validating if data exists
    """
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_files_exist()
        except Exception as e:
            raise CustomException(e, sys) from e