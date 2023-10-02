from CNNClassifier.config import ConfigurationManager
from CNNClassifier.components import PrepareBaseModel
from CNNClassifier import logger

def prepareBaseModel():
    try:
        logger.info("Training Pipeline 2 -- prepare base model stage started")
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
        logger.info("Training Pipeline 2 -- prepare base model stage completed")
    except Exception as e:
        raise e