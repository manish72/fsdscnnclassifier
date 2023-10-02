from CNNClassifier.pipeline.stage_01_data_ingestion import dataIngestion
from CNNClassifier.pipeline.stage_02_prepare_base_model import prepareBaseModel
from CNNClassifier.pipeline.stage_03_train import modelTraining
from CNNClassifier.pipeline.stage_04_evaluation import modelEvaluation


if __name__ == '__main__':
    '''
        to execute the training pipeline
    '''
    dataIngestion()
    prepareBaseModel()
    modelTraining()
    modelEvaluation()