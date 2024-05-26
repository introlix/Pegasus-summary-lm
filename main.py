import sys
from summarylm.pipeline.data_ingestion import DataIngestionPipeline
from summarylm.pipeline.data_validation import DataValidationPipeline
from summarylm.pipeline.data_transformation import DataTransformationPipeline
from summarylm.pipeline.model_trainer import ModelTrainerPipeline
from summarylm.pipeline.model_evaluation import ModelEvaluationPipeline
from summarylm.logging import logger
from summarylm.exception import CustomException

# data ingestion
STAGE_NAME = "Data Ingestion"

try:
    logger.info(f"Starting {STAGE_NAME} stage...")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f"Completed {STAGE_NAME} stage...")
except Exception as e:
    raise CustomException(e, sys) from e


# data validation
STAGE_NAME = "Data Validation"

try:
    logger.info(f"Starting {STAGE_NAME} stage...")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f"Completed {STAGE_NAME} stage...")
except Exception as e:
    raise CustomException(e, sys) from e


# data transformation
STAGE_NAME = "Data Transformation"

try:
    logger.info(f"Starting {STAGE_NAME} stage...")
    data_transformation= DataTransformationPipeline()
    data_transformation.main()
    logger.info(f"Completed {STAGE_NAME} stage...")
except Exception as e:
    raise CustomException(e, sys) from e


# model trainer
STAGE_NAME = "Model Trainer"

try:
    logger.info(f"Starting {STAGE_NAME} stage...")
    model_trainer= ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f"Completed {STAGE_NAME} stage...")
except Exception as e:
    raise CustomException(e, sys) from e

# model evaluation
STAGE_NAME = "Model Evaluation"

try:
    logger.info(f"Starting {STAGE_NAME} stage...")
    model_trainer= ModelEvaluationPipeline()
    model_trainer.main()
    logger.info(f"Completed {STAGE_NAME} stage...")
except Exception as e:
    raise CustomException(e, sys) from e