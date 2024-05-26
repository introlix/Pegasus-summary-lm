import sys
from summarylm.config.configuration import ConfigurationManager
from summarylm.components.data_ingestion import DataIngestion
from summarylm.logging import logger
from summarylm.exception import CustomException


class DataIngestionPipeline:
    """
    Pipeline for data ingestion
    """
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_data()
        except Exception as e:
            raise CustomException(e, sys) from e