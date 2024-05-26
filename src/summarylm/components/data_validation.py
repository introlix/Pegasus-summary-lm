import os
import sys
from summarylm.logging import logger
from summarylm.exception import CustomException
from summarylm.entity import DataValidationConfig


class DataValidation:
    """
    Class for validating if all data files exists in train, test, validation folders

    Args:
        config (DataValidationConfig): Contain all config for data validation

    Returns:
        validation_status (bool): true if data exists else false
    """
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            logger.info("Entered validate_all_files_exist method of DataValidation class.")
            validation_status = None

            for data in self.config.ALL_REQUIRED_DATA:
                all_files = os.listdir(os.path.join("artifacts", "data_ingestion", data))

                for file in all_files:
                    if file not in self.config.ALL_REQUIRED_FILES:
                        validation_status = False

                        with open(self.config.STATUS_FILE, 'w') as f:
                            f.write(f"Validation status: {validation_status}")
                    else:
                        validation_status = True

                        with open(self.config.STATUS_FILE, 'w') as f:
                            f.write(f"Validation status: {validation_status}")
                        
            logger.info("Completed validate_all_files_exist method of DataValidation class.")

            return validation_status
        except Exception as e:
            raise CustomException(e, sys) from e