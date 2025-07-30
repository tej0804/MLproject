from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation

from src.components.model_trainer import ModelTrainer

if __name__=="__main__":
    ingestion =DataIngestion()
    train_data,test_data=ingestion.initiate_data_ingestion()

    print("[MAIN] Data ingestion complete")

    data_transformation=DataTransformation()

    print("[MAIN] starting transformation")
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)
    print("[MAIN] data transformation completed")


    print("[INFO] Starting model training...")
    modeltrainer=ModelTrainer()
    
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
    print("[INFO] Model training completed.")