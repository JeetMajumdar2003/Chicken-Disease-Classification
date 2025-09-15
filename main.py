from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import TrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<<")
        data_ingestion_pipeline = DataIngestionTrainingPipeline()
        data_ingestion_pipeline.main()
        logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(f"Error in main pipeline: {e}")
        raise e
    



STAGE_NAME = "Prepare Base Model Stage"

if __name__ == "__main__":
    try:
        logger.info(f"***********************************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        pipeline = PrepareBaseModelTrainingPipeline()
        pipeline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(f"Error in stage {STAGE_NAME}: {e}")
        raise e
    


STAGE_NAME = "Training Stage"
if __name__ == "__main__":
    try:
        logger.info(f"***********************************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        pipeline = TrainingPipeline()
        pipeline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(f"Error in stage {STAGE_NAME}: {e}")
        raise e