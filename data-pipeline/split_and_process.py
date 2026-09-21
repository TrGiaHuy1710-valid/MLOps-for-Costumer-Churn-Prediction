import pandas as pd 
import numpy as np 
from pathlib import Path 

BASE_DIR = Path(__file__).resolve().parent

RAW_DIR = BASE_DIR / 'data' / 'raw'
PROCESSED_DIR = BASE_DIR / 'data' / 'processed'
FEAST_DATA = BASE_DIR / 'churn_feature_store' / 'churn_feature' / 'feature_repo' / 'data'

for d in (RAW_DIR, PROCESSED_DIR, FEAST_DATA):
    d.mkdir(parents=True, exist_ok=True)


# 1) split 10 files (mô phỏng "data theo perod" trong thực tế) từ file raw data
df = pd.read_csv(RAW_DIR / 'customer_churn_dataset-training-master.csv')


for i, chunk in enumerate(np.array_split(df, 10), start=1):
    chunk = pd.DataFrame(chunk, columns=df.columns)
    chunk.to_csv(RAW_DIR / f'train_period_{i}.csv', index=False)

# 2) process data: remove duplicates, fill missing values, and save to processed directory - in period 1
raw = pd.read_csv(RAW_DIR / 'train_period_1.csv')
raw = raw.drop_duplicates()
raw = raw.dropna() 


# 2.1 TODO: ADD MORE PRCESSING STEPS HERE


raw.to_csv(PROCESSED_DIR / 'processed_period_1.csv', index=False)

# 3) add event_timestamp + create_timestamp for feast feature store, then save as parquet file
proc = pd.read_csv(PROCESSED_DIR / 'processed_period_1.csv')
proc['event_timestamp'] = pd.Timestamp.now()
proc['create_timestamp'] = pd.Timestamp.now()
proc.to_parquet(FEAST_DATA / 'processed_period_1.parquet', index=False)

print("Done: ", proc.shape, "rows and columns")
