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