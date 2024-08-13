from src.mlProject import logger
from src.mlProject.pipeline.stage01_data_Injection import DataIngectionTrainingPipeline
from src.mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "Data injection Stage"

try:
    logger.info(f">>>>Stage Name {STAGE_NAME} Started <<<<")
    data_injection =DataIngectionTrainingPipeline()
    data_injection.main()
    logger.info(f">>>>Stage Name {STAGE_NAME} Completd <<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e  

try:
    logger.info(f">>>>Stage Name {STAGE_NAME} Started <<<<")
    data_validation =DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>Stage Name {STAGE_NAME} Completd <<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e  