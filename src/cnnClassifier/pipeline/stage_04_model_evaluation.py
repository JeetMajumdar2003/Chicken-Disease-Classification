from cnnClassifier.components.model_evaluation import Evaluation
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier import logger


STAGE_NAME = "Model Evaluation Stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == "__main__":
    try:
        logger.info(f"***********************************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        pipeline = EvaluationPipeline()
        pipeline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(f"Error in stage {STAGE_NAME}: {e}")
        raise e