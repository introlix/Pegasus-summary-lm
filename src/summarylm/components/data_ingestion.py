import os
import sys
import zipfile
from pathlib import Path
from datasets import load_dataset

from summarylm.entity import DataIngestionConfig
from summarylm.utils.common import get_size
from summarylm.logging import logger
from summarylm.exception import CustomException

class DataIngestion:
    """
    Class for download and unzip data and store it into artifact folder

    Args:
        config (DataIngestionConfig): Contain all config for data ingestion

    Returns:
        None
    """
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        """
        Function to download data from gcloud
        """
        try:
            for i in range(len(self.config.LOCAL_DATA_FILE)):
                if not os.path.exists(self.config.LOCAL_DATA_FILE[i]):
                    dataset = load_dataset(self.config.ALL_HUGGINGFACE_DATA[i])
                    dataset.save_to_disk(self.config.LOCAL_DATA_FILE[i])
                    logger.info(f"{self.config.ALL_HUGGINGFACE_DATA[i]} downloaded!")
                else:
                    logger.info(f"File already exists of size: {get_size(Path(self.config.LOCAL_DATA_FILE[i]))}")

        except Exception as e:
            raise CustomException(e, sys) from e