import os
import sys
from summarylm.logging import logger
from summarylm.exception import CustomException
from summarylm.entity import DataTransformationConfig
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk, concatenate_datasets, DatasetDict


class DataTransformation:
    """
    Class for transforming data into valid format for training

    Args:
        config (DataTransformationConfig): Contain all config for data transformation
    """
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_data_into_right_format(self, datasets: list) -> DatasetDict:
        """
        Function to remove & rename columns and convert it into right format to train

        Args:
            datasets (list): list of all dataset path
        
        Returns:
            DatasetDict: Contains train, test, and validation sets
        """
        try:
            logger.info("Entered convert_data_into_right_format method of DataTransformation class.")
            # loading all datasets
            loaded_datasets = {}
            print("Loading the dataset")
            for data in datasets:
                loaded_datasets[data] = load_from_disk(data)

            dataset1 = loaded_datasets[datasets[0]]
            dataset2 = loaded_datasets[datasets[1]]
            print("Dataset loaded")

            # removing unwanted columns from dataset1
            dataset1_train = dataset1['train'].select_columns(['article', 'summary'])
            dataset1_test = dataset1['test'].select_columns(['article', 'summary'])
            dataset1_validation = dataset1['validation'].select_columns(['article', 'summary'])

            # renaming data column name of dataset1
            dataset1_train = dataset1_train.rename_column('article', 'text')
            dataset1_test = dataset1_test.rename_column('article', 'text')
            dataset1_validation = dataset1_validation.rename_column('article', 'text')

            # renaming data column name of dataset2
            dataset2_train = dataset2['train'].rename_column('document', 'text')
            dataset2_test = dataset2['test'].rename_column('document', 'text')
            dataset2_validation = dataset2['validation'].rename_column('document', 'text')

            # concatenate_datasets
            dataset_train = concatenate_datasets([dataset1_train, dataset2_train])
            dataset_test = concatenate_datasets([dataset1_test, dataset2_test])
            dataset_validation = concatenate_datasets([dataset1_validation, dataset2_validation])

            # loading the dataset into DatasetDict
            dataset = DatasetDict({
                "train": dataset_train,
                "validation": dataset_validation,
                "test": dataset_test,
            })
            return dataset
        
        except Exception as e:
            raise CustomException(e, sys) from e

    def convert_examples_to_features(self, example_batch):
        """
        Method to convert data into data into features

        Args:
            example_batch: dataset after loading it from datasets library
        Returns:
            input_ids: A list of token ids representing the dialogue
            attention_mask: List of indices specifying which tokens should be attended to by the model
            labels: A list of token ids representing the summary
        """
        try:
            logger.info("Entered convert_examples_to_features method of DataTransformation class.")
            input_encodings = self.tokenizer(example_batch['text'], max_length = 1024, truncation = True)
    
            with self.tokenizer.as_target_tokenizer():
                target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True)
        
            return {
                'input_ids': input_encodings['input_ids'],
                'attention_mask': input_encodings['attention_mask'],
                'labels': target_encodings['input_ids']
            }
        except Exception as e:
            raise CustomException(e, sys) from e
            
    
    def convert(self):
        data1 = os.path.join(self.config.data_path, self.config.ALL_REQUIRED_DATA[0])
        data2 = os.path.join(self.config.data_path, self.config.ALL_REQUIRED_DATA[1])

        dataset = self.convert_data_into_right_format([data1, data2])
        dataset_pt = dataset.map(self.convert_examples_to_features, batched=True)
        dataset_pt.save_to_disk(os.path.join(self.config.root_dir, "dataset"))