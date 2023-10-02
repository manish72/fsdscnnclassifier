from CNNClassifier.config import ConfigurationManager
from CNNClassifier.components.stage_04_evaluation import Evaluation
from CNNClassifier import logger


def modelEvaluation():
    try:
        logger.info("Training Pipeline 4 -- model evaluation stage started")
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()
        logger.info("Training Pipeline 4 -- model evaluation stage completed")
    except Exception as e:
        raise e
