from mlflow_project import logger
from mlflow_project.pipeline.data_ingestion_pipeline import (
    STAGE_NAME_01,
    DataIngestionPipeline,
)
from mlflow_project.pipeline.data_transformation_pipeline import (
    STAGE_NAME_03,
    DataTransformationPipeline,
)
from mlflow_project.pipeline.data_validation_pipeline import (
    STAGE_NAME_02,
    DataValidationPipeline,
)
from mlflow_project.pipeline.model_evaluation_pipeline import (
    STAGE_NAME_05,
    ModelEvaluationPipeline,
)
from mlflow_project.pipeline.model_trainer_pipeline import (
    STAGE_NAME_04,
    ModelTrainerPipeline,
)

try:
    # Data Ingestion Pipeline
    logger.info(f"{STAGE_NAME_01} has started")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.forward()
    logger.info(f"{STAGE_NAME_01} has completed")

    # Data Validation Pipeline
    logger.info(f"{STAGE_NAME_02} has started")
    data_validation_pipeline = DataValidationPipeline()
    data_validation_pipeline.forward()
    logger.info(f"{STAGE_NAME_02} has completed")

    # Data Transformation Pipeline
    logger.info(f"{STAGE_NAME_03} has started")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.forward()
    logger.info(f"{STAGE_NAME_03} has completed")

    # Model Training Pipeline
    logger.info(f"{STAGE_NAME_04} has started")
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.forward()
    logger.info(f"{STAGE_NAME_04} has completed")

    # Model Evaluation Pipeline
    logger.info(f"{STAGE_NAME_05} has started")
    model_evaluation_pipeline = ModelEvaluationPipeline()
    model_evaluation_pipeline.forward()
    logger.info(f"{STAGE_NAME_05} has completed")

except Exception as e:
    logger.exception(e)
    raise e
