from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_injection import DataIngestion
from src.mlProject import logger

STAGE_NAME = "Data Injection Pipeline"

class DataIngectionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f">>>>Stage Name {STAGE_NAME} Started <<<<")
        obj =DataIngectionTrainingPipeline()
        obj.main()
        logger.info(f">>>>Stage Name {STAGE_NAME} Completd <<<<<\n\nx========x")
    except Exception as e:
        logger.exception(e)
        raise e    

