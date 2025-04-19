# Main training script
import pandas as pd
from src.cleaner import Cleaner
from src.preprocessor import Preprocessor
from src.features import FeatureEngineer
from src.model import ModelTrainer

# Load data
df = pd.read_csv('data/sample_data.csv')

# Clean data
cleaner = Cleaner()
df = cleaner.clean(df)

# Preprocess data
preprocessor = Preprocessor()
df = preprocessor.preprocess(df)

# Feature engineering
fe = FeatureEngineer()
df = fe.engineer(df)

# Train model
X = df[['feature1', 'feature2']]
y = df['label']
trainer = ModelTrainer()
model = trainer.train(X, y)