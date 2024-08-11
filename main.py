from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataingestionTrainingPipeline

STAGE_NAME = "Data Imgestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataingestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e