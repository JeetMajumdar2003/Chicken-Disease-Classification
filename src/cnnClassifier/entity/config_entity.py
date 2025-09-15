from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """Entity class for data ingestion configuration.
    
    Attributes:
        root_dir: The root directory for data ingestion.
        source_URL: The URL to download the data from.
        local_data_file: The local path to save the downloaded data file.
        unzip_dir: The directory to extract the downloaded zip file.
    """
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    """Entity class for prepare base model configuration.
    
    Attributes:
        root_dir: The root directory for the model to be saved.
        base_model_path: The path to the base model.
        updated_base_model_path: The path to the updated base model.
        params_image_size: The image size parameters.
        params_learning_rate: The learning rate for the model.
        params_include_top: Whether to include the top layer of the model.
        params_weights: The weights to be used for the model.
        params_classes: The number of output classes for the model.
    """
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int


@dataclass(frozen=True)
class PrepareCallbacksConfig:
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: Path