from CNNClassifier.config import ConfigurationManager
from CNNClassifier.components.stage_03_train import Training
from CNNClassifier import logger

def modelTraining():
    try:
        logger.info("Training Pipeline 3 -- model training stage started")
        config = ConfigurationManager()
    
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()
        logger.info("Training Pipeline 3 -- model training stage completed")
    except Exception as e:
        raise e