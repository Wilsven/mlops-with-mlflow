import os

from dotenv import load_dotenv

from mlflow_project import logger
from mlflow_project.constants import *
from mlflow_project.entity.config_entity import (
    DataIngestionConfig,
    DataTransformationConfig,
    DataValidationConfig,
    ModelEvaluationConfig,
    ModelTrainerConfig,
)
from mlflow_project.utils.common import create_directories, read_yaml

load_dotenv()

MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI")
MLFLOW_TRACKING_USERNAME = os.getenv("MLFLOW_TRACKING_USERNAME")
MLFLOW_TRACKING_PASSWORD = os.getenv("MLFLOW_TRACKING_PASSWORD")


class ConfigurationManager:
    def __init__(
        self,
        config_file_path: Path = CONFIG_FILE_PATH,
        params_file_path: Path = PARAMS_FILE_PATH,
        schema_file_path: Path = SCHEMA_FILE_PATH,
    ):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Creates the root directory and returns
        the configuration for data ingestion.

        Returns:
            DataIngestionConfig: Configuration for data ingestion.
        """
        data_ingestion = self.config.data_ingestion

        create_directories([data_ingestion.root_dir])

        file_path = os.path.join(data_ingestion.root_dir, ".gitkeep")
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                logger.info(
                    f"Creating file: .gitkeep in directory {data_ingestion.root_dir}"
                )
                pass

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(data_ingestion.root_dir),
            source_url=str(data_ingestion.source_url),
            local_data_file=Path(data_ingestion.local_data_file),
            unzip_dir=Path(data_ingestion.unzip_dir),
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        """
        Creates the root directory and returns
        the configuration for data validation.

        Returns:
            DataValidationConfig: Configuration for data validation.
        """
        data_validation = self.config.data_validation
        schema = self.schema.columns

        create_directories([data_validation.root_dir])

        file_path = os.path.join(data_validation.root_dir, ".gitkeep")
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                logger.info(
                    f"Creating file: .gitkeep in directory {data_validation.root_dir}"
                )
                pass

        data_validation_config = DataValidationConfig(
            root_dir=Path(data_validation.root_dir),
            unzip_data_path=Path(data_validation.unzip_data_path),
            status_file_path=Path(data_validation.status_file_path),
            data_schema=dict(schema),
        )

        return data_validation_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        """
        Creates the root directory and returns
        the configuration for data transformation.

        Returns:
            DataTransformationConfig: Configuration for data transformation.
        """
        data_transformation = self.config.data_transformation

        create_directories([data_transformation.root_dir])

        file_path = os.path.join(data_transformation.root_dir, ".gitkeep")
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                logger.info(
                    f"Creating file: .gitkeep in directory {data_transformation.root_dir}"
                )
                pass

        data_transformation_config = DataTransformationConfig(
            root_dir=Path(data_transformation.root_dir),
            unzip_data_path=Path(data_transformation.unzip_data_path),
            status_file_path=Path(data_transformation.status_file_path),
        )

        return data_transformation_config

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        """
        Creates the root directory and returns
        the configuration for model trainer.

        Returns:
            ModelTrainerConfig: Configuration for model trainer.
        """
        model_trainer = self.config.model_trainer
        target = self.schema.target

        create_directories([model_trainer.root_dir])

        file_path = os.path.join(model_trainer.root_dir, ".gitkeep")
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                logger.info(
                    f"Creating file: .gitkeep in directory {model_trainer.root_dir}"
                )
                pass

        model_trainer_config = ModelTrainerConfig(
            root_dir=Path(model_trainer.root_dir),
            train_data_path=Path(model_trainer.train_data_path),
            test_data_path=Path(model_trainer.test_data_path),
            model_name=str(model_trainer.model_name),
            alpha=float(self.params.ALPHA),
            l1_ratio=float(self.params.L1_RATIO),
            random_state=int(self.params.RANDOM_STATE),
            target_column=str(target.name),
        )

        return model_trainer_config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        """
        Creates the root directory and returns
        the configuration for model evaluation.

        Returns:
            ModelEvaluationConfig: Configuration for model evaluation.
        """
        model_evaluation = self.config.model_evaluation
        target = self.schema.target

        create_directories([model_evaluation.root_dir])

        file_path = os.path.join(model_evaluation.root_dir, ".gitkeep")
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                logger.info(
                    f"Creating file: .gitkeep in directory {model_evaluation.root_dir}"
                )
                pass

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=Path(model_evaluation.root_dir),
            test_data_path=Path(model_evaluation.test_data_path),
            model_path=Path(model_evaluation.model_path),
            metrics_file_path=Path(model_evaluation.metrics_file_path),
            alpha=float(self.params.ALPHA),
            l1_ratio=float(self.params.L1_RATIO),
            random_state=int(self.params.RANDOM_STATE),
            target_column=str(target.name),
            mlflow_uri=str(MLFLOW_TRACKING_URI),
        )

        return model_evaluation_config
