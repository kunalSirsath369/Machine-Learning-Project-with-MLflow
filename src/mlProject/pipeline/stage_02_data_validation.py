from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_validation import DataValiadtion
from src.mlProject import logger

STAGE_NAME = "Data Injection Pipeline"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__ == "__main__":
    try:
        logger.info(f">>>>Stage Name {STAGE_NAME} Started <<<<")
        obj =DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>Stage Name {STAGE_NAME} Completd <<<<<\n\nx========x")
    except Exception as e:
        logger.exception(e)
        raise e            