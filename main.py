# credit_risk_pipeline/main.py
from src.config import Config
from src.components.data_Ingestion import DataLoader
from src.components import cleaner


# Load raw data using secured config
data_path = Config.get_data_path()
data = DataLoader(data_path).load()

print(data.head())
